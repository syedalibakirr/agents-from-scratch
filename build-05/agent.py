"""
Build 3 — The flood test
Same agent as Build 1: a model, a loop, and three tools. No framework, no logic changed.

The only addition: set FLOOD=1 and 50 fake tool schemas get appended to the tool list
handed to the model. The fakes are never callable — if the model calls one anyway, it
gets an error back and the attempt is logged. Leave FLOOD unset and this runs exactly
like Build 1.

Run it like:
    python agent.py /path/to/a/repo/you/know  "What does this project do?"
    FLOOD=1 python agent.py /path/to/a/repo/you/know  "What does this project do?"

Success = a file called traces.jsonl appears with a few lines in it.
"""
import anthropic, json, os, sys

# ---- config ----
FLOOD = os.environ.get("FLOOD")            # set to any truthy value to flood the tool list

MODEL = "claude-sonnet-5"   # found in console → Build → Workbench → model dropdown
REPO  = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
TASK  = sys.argv[2] if len(sys.argv) > 2 else "What does this project do? Name the main entry file."

client = anthropic.Anthropic()       # reads ANTHROPIC_API_KEY from your environment
trace  = open("traces.jsonl", "w")
def log(kind, data):
    trace.write(json.dumps({"kind": kind, "data": data}, default=str) + "\n"); trace.flush()

# ---- the three tools: each takes a string, returns a string ----
def list_files(_=None):
    out = []
    for root, _d, files in os.walk(REPO):
        if "/." in root or "node_modules" in root: continue
        for f in files:
            out.append(os.path.relpath(os.path.join(root, f), REPO))
    return "\n".join(out[:200]) or "empty repo"

def read_file(path):
    try:
        return open(os.path.join(REPO, path), errors="ignore").read()[:2000]
    except Exception as e:
        return f"ERROR: {e}"

def search(query):
    hits = []
    for root, _d, files in os.walk(REPO):
        if "/." in root or "node_modules" in root: continue
        for f in files:
            try:
                for i, line in enumerate(open(os.path.join(root, f), errors="ignore"), 1):
                    if query.lower() in line.lower():
                        hits.append(f"{os.path.relpath(os.path.join(root,f), REPO)}:{i}: {line.strip()[:120]}")
            except Exception: pass
    # Capped at 40 hits, unsorted, with no notice to the model that results were
    # truncated — a known limitation, not an oversight. See build-05/README.md.
    # Addressing this (ranking, pagination, or a truncation notice) is later-build work.
    return "\n".join(hits[:40]) or "no matches"

# ---- the tool descriptions now live in tools.md, not here ----
def load_descriptions(path="tools.md"):
    here = os.path.dirname(os.path.abspath(__file__))
    text = open(os.path.join(here, path), encoding="utf-8").read()
    out, name = {}, None
    for line in text.splitlines():
        if line.startswith("## "):
            name = line[3:].strip()
            out[name] = ""
        elif name and line.strip():
            out[name] = (out[name] + " " + line.strip()).strip()
    return out

DESC = load_descriptions()
log("tool_descriptions", DESC)

TOOLS  = {"list_files": list_files, "read_file": read_file, "search": search}
SCHEMA = [
    {"name": "list_files", "description": DESC["list_files"],
     "input_schema": {"type": "object", "properties": {}}},
    {"name": "read_file", "description": DESC["read_file"],
     "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}},
    {"name": "search", "description": DESC["search"],
     "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
]

# ---- flood: 50 plausible, never-callable tool schemas ----
FAKE_TOOLS = [
    {"name": "query_database", "description": "Run a read-only SQL query against the primary application database and return the result rows.",
     "input_schema": {"type": "object", "properties": {"sql": {"type": "string"}, "database": {"type": "string"}}, "required": ["sql"]}},
    {"name": "send_email", "description": "Send an email via the configured transactional email provider.",
     "input_schema": {"type": "object", "properties": {"to": {"type": "string"}, "subject": {"type": "string"}, "body": {"type": "string"}}, "required": ["to", "subject", "body"]}},
    {"name": "resize_image", "description": "Resize an image file to the given width and height, preserving aspect ratio if only one is given.",
     "input_schema": {"type": "object", "properties": {"path": {"type": "string"}, "width": {"type": "integer"}, "height": {"type": "integer"}}, "required": ["path"]}},
    {"name": "create_calendar_event", "description": "Create an event on the user's primary calendar.",
     "input_schema": {"type": "object", "properties": {"title": {"type": "string"}, "start_time": {"type": "string"}, "end_time": {"type": "string"}}, "required": ["title", "start_time"]}},
    {"name": "translate_text", "description": "Translate a string of text from one language to another.",
     "input_schema": {"type": "object", "properties": {"text": {"type": "string"}, "target_language": {"type": "string"}}, "required": ["text", "target_language"]}},
    {"name": "fetch_weather", "description": "Get the current weather conditions and short-term forecast for a location.",
     "input_schema": {"type": "object", "properties": {"location": {"type": "string"}}, "required": ["location"]}},
    {"name": "run_sql_migration", "description": "Apply a pending database migration file to the target environment.",
     "input_schema": {"type": "object", "properties": {"migration_file": {"type": "string"}, "environment": {"type": "string"}}, "required": ["migration_file"]}},
    {"name": "compress_file", "description": "Compress a file or directory into a zip or tar.gz archive.",
     "input_schema": {"type": "object", "properties": {"path": {"type": "string"}, "format": {"type": "string"}}, "required": ["path"]}},
    {"name": "send_slack_message", "description": "Post a message to a Slack channel via the configured workspace bot.",
     "input_schema": {"type": "object", "properties": {"channel": {"type": "string"}, "text": {"type": "string"}}, "required": ["channel", "text"]}},
    {"name": "create_github_issue", "description": "Open a new issue on a GitHub repository.",
     "input_schema": {"type": "object", "properties": {"repo": {"type": "string"}, "title": {"type": "string"}, "body": {"type": "string"}}, "required": ["repo", "title"]}},
    {"name": "get_stock_price", "description": "Look up the latest quote for a stock ticker symbol.",
     "input_schema": {"type": "object", "properties": {"ticker": {"type": "string"}}, "required": ["ticker"]}},
    {"name": "generate_invoice", "description": "Generate a PDF invoice for a customer order.",
     "input_schema": {"type": "object", "properties": {"order_id": {"type": "string"}, "customer_email": {"type": "string"}}, "required": ["order_id"]}},
    {"name": "schedule_cron_job", "description": "Register a new scheduled job to run on a cron expression.",
     "input_schema": {"type": "object", "properties": {"cron_expression": {"type": "string"}, "command": {"type": "string"}}, "required": ["cron_expression", "command"]}},
    {"name": "deploy_service", "description": "Trigger a deployment of a service to the specified environment.",
     "input_schema": {"type": "object", "properties": {"service_name": {"type": "string"}, "environment": {"type": "string"}}, "required": ["service_name", "environment"]}},
    {"name": "rotate_api_key", "description": "Rotate the API key for a given third-party integration.",
     "input_schema": {"type": "object", "properties": {"integration": {"type": "string"}}, "required": ["integration"]}},
    {"name": "get_exchange_rate", "description": "Get the current exchange rate between two currencies.",
     "input_schema": {"type": "object", "properties": {"from_currency": {"type": "string"}, "to_currency": {"type": "string"}}, "required": ["from_currency", "to_currency"]}},
    {"name": "create_jira_ticket", "description": "Create a ticket in a Jira project.",
     "input_schema": {"type": "object", "properties": {"project": {"type": "string"}, "summary": {"type": "string"}, "issue_type": {"type": "string"}}, "required": ["project", "summary"]}},
    {"name": "purge_cache", "description": "Purge the CDN cache for a given URL path or the entire site.",
     "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": []}},
    {"name": "get_user_profile", "description": "Fetch a user's profile information from the identity provider.",
     "input_schema": {"type": "object", "properties": {"user_id": {"type": "string"}}, "required": ["user_id"]}},
    {"name": "ban_user", "description": "Ban a user account from the platform.",
     "input_schema": {"type": "object", "properties": {"user_id": {"type": "string"}, "reason": {"type": "string"}}, "required": ["user_id"]}},
    {"name": "generate_qr_code", "description": "Generate a QR code image encoding the given text or URL.",
     "input_schema": {"type": "object", "properties": {"data": {"type": "string"}}, "required": ["data"]}},
    {"name": "transcribe_audio", "description": "Transcribe an audio file to text.",
     "input_schema": {"type": "object", "properties": {"audio_path": {"type": "string"}, "language": {"type": "string"}}, "required": ["audio_path"]}},
    {"name": "post_tweet", "description": "Post a new tweet from the connected account.",
     "input_schema": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}},
    {"name": "get_traffic_analytics", "description": "Fetch website traffic analytics for a date range.",
     "input_schema": {"type": "object", "properties": {"start_date": {"type": "string"}, "end_date": {"type": "string"}}, "required": ["start_date", "end_date"]}},
    {"name": "create_stripe_charge", "description": "Create a one-time charge against a Stripe customer.",
     "input_schema": {"type": "object", "properties": {"customer_id": {"type": "string"}, "amount_cents": {"type": "integer"}}, "required": ["customer_id", "amount_cents"]}},
    {"name": "refund_payment", "description": "Issue a refund for a previously captured payment.",
     "input_schema": {"type": "object", "properties": {"payment_id": {"type": "string"}, "amount_cents": {"type": "integer"}}, "required": ["payment_id"]}},
    {"name": "lookup_dns_record", "description": "Look up DNS records for a domain name.",
     "input_schema": {"type": "object", "properties": {"domain": {"type": "string"}, "record_type": {"type": "string"}}, "required": ["domain"]}},
    {"name": "restart_server", "description": "Restart a named server or process in the infrastructure.",
     "input_schema": {"type": "object", "properties": {"server_name": {"type": "string"}}, "required": ["server_name"]}},
    {"name": "get_disk_usage", "description": "Get current disk usage statistics for a host.",
     "input_schema": {"type": "object", "properties": {"host": {"type": "string"}}, "required": ["host"]}},
    {"name": "create_s3_presigned_url", "description": "Generate a presigned URL for uploading or downloading an object from S3.",
     "input_schema": {"type": "object", "properties": {"bucket": {"type": "string"}, "key": {"type": "string"}, "operation": {"type": "string"}}, "required": ["bucket", "key"]}},
    {"name": "send_sms", "description": "Send an SMS text message to a phone number.",
     "input_schema": {"type": "object", "properties": {"to": {"type": "string"}, "body": {"type": "string"}}, "required": ["to", "body"]}},
    {"name": "get_calendar_availability", "description": "Get free/busy availability for a user's calendar over a date range.",
     "input_schema": {"type": "object", "properties": {"user_email": {"type": "string"}, "start_date": {"type": "string"}, "end_date": {"type": "string"}}, "required": ["user_email", "start_date"]}},
    {"name": "create_zoom_meeting", "description": "Schedule a new Zoom meeting and return the join link.",
     "input_schema": {"type": "object", "properties": {"topic": {"type": "string"}, "start_time": {"type": "string"}}, "required": ["topic", "start_time"]}},
    {"name": "moderate_content", "description": "Run automated moderation on a piece of text or image content and return a safety verdict.",
     "input_schema": {"type": "object", "properties": {"content": {"type": "string"}}, "required": ["content"]}},
    {"name": "get_geolocation", "description": "Resolve an IP address to an approximate geographic location.",
     "input_schema": {"type": "object", "properties": {"ip_address": {"type": "string"}}, "required": ["ip_address"]}},
    {"name": "create_docker_container", "description": "Start a new Docker container from an image.",
     "input_schema": {"type": "object", "properties": {"image": {"type": "string"}, "name": {"type": "string"}}, "required": ["image"]}},
    {"name": "scale_kubernetes_deployment", "description": "Scale a Kubernetes deployment to a target replica count.",
     "input_schema": {"type": "object", "properties": {"deployment": {"type": "string"}, "replicas": {"type": "integer"}}, "required": ["deployment", "replicas"]}},
    {"name": "get_npm_package_info", "description": "Fetch metadata for a package from the npm registry.",
     "input_schema": {"type": "object", "properties": {"package_name": {"type": "string"}}, "required": ["package_name"]}},
    {"name": "convert_currency_amount", "description": "Convert a monetary amount from one currency to another using live rates.",
     "input_schema": {"type": "object", "properties": {"amount": {"type": "number"}, "from_currency": {"type": "string"}, "to_currency": {"type": "string"}}, "required": ["amount", "from_currency", "to_currency"]}},
    {"name": "create_google_doc", "description": "Create a new Google Doc with the given title and initial content.",
     "input_schema": {"type": "object", "properties": {"title": {"type": "string"}, "content": {"type": "string"}}, "required": ["title"]}},
    {"name": "get_flight_status", "description": "Get the current status of a commercial flight by flight number.",
     "input_schema": {"type": "object", "properties": {"flight_number": {"type": "string"}, "date": {"type": "string"}}, "required": ["flight_number"]}},
    {"name": "book_hotel_room", "description": "Book a hotel room reservation for given dates.",
     "input_schema": {"type": "object", "properties": {"hotel_id": {"type": "string"}, "check_in": {"type": "string"}, "check_out": {"type": "string"}}, "required": ["hotel_id", "check_in", "check_out"]}},
    {"name": "get_crypto_price", "description": "Get the current market price of a cryptocurrency.",
     "input_schema": {"type": "object", "properties": {"symbol": {"type": "string"}}, "required": ["symbol"]}},
    {"name": "create_trello_card", "description": "Create a new card on a Trello board list.",
     "input_schema": {"type": "object", "properties": {"list_id": {"type": "string"}, "name": {"type": "string"}}, "required": ["list_id", "name"]}},
    {"name": "set_thermostat_temperature", "description": "Set the target temperature on a connected smart thermostat.",
     "input_schema": {"type": "object", "properties": {"device_id": {"type": "string"}, "temperature_f": {"type": "number"}}, "required": ["device_id", "temperature_f"]}},
    {"name": "get_calendar_holidays", "description": "List public holidays for a country within a date range.",
     "input_schema": {"type": "object", "properties": {"country_code": {"type": "string"}, "year": {"type": "integer"}}, "required": ["country_code", "year"]}},
    {"name": "encrypt_secret", "description": "Encrypt a plaintext value using the configured secrets manager and return a ciphertext handle.",
     "input_schema": {"type": "object", "properties": {"plaintext": {"type": "string"}}, "required": ["plaintext"]}},
    {"name": "get_build_status", "description": "Get the status of the latest CI build for a branch.",
     "input_schema": {"type": "object", "properties": {"repo": {"type": "string"}, "branch": {"type": "string"}}, "required": ["repo", "branch"]}},
    {"name": "add_dns_record", "description": "Add a new DNS record to a domain's zone file.",
     "input_schema": {"type": "object", "properties": {"domain": {"type": "string"}, "record_type": {"type": "string"}, "value": {"type": "string"}}, "required": ["domain", "record_type", "value"]}},
    {"name": "create_zendesk_ticket", "description": "Create a new customer support ticket in Zendesk.",
     "input_schema": {"type": "object", "properties": {"subject": {"type": "string"}, "description": {"type": "string"}, "requester_email": {"type": "string"}}, "required": ["subject", "description"]}},
]
assert len(FAKE_TOOLS) == 50, f"expected 50 fake tools, got {len(FAKE_TOOLS)}"

if FLOOD:
    SCHEMA = SCHEMA + FAKE_TOOLS

def call_tool(name, arg):
    # flood guard: fake tools are never actually callable
    if name not in TOOLS:
        log("fake_tool_attempt", {"name": name, "input": arg})
        return f"ERROR: {name} is not available."
    return TOOLS[name](arg)

messages = [{"role": "user", "content": TASK}]

# ==== THE LOOP — this is the entire agent ====
while True:
    TEMP = float(os.environ.get("TEMP", "1.0"))
    resp = client.messages.create(model=MODEL, max_tokens=1024, tools=SCHEMA, messages=messages, temperature=TEMP)
    log("model_step", [b.model_dump() for b in resp.content])
    messages.append({"role": "assistant", "content": resp.content})

    if resp.stop_reason == "tool_use":
        results = []
        for block in resp.content:
            if block.type == "tool_use":
                arg = (list(block.input.values())[0] if block.input else None)
                out = call_tool(block.name, arg)[:2000]        # hard truncation
                print(f"  -> agent called {block.name}({block.input})")
                log("tool_call", {"name": block.name, "input": block.input, "output_preview": out[:200]})
                results.append({"type": "tool_result", "tool_use_id": block.id, "content": out})
        messages.append({"role": "user", "content": results})
    else:
        answer = "".join(b.text for b in resp.content if b.type == "text")
        log("final_answer", answer)
        print("\n=== AGENT ANSWER ===\n" + answer)
        break

trace.close()
print("\nDone. Open traces.jsonl and read every line — that's what your agent actually did.")
