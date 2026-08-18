import anthropic
c = anthropic.Anthropic()

def probe(model, label, **extra):
    tag = ("[" + model + "] " + label).ljust(46)
    try:
        c.messages.create(model=model, max_tokens=4,
                          messages=[{"role": "user", "content": "hi"}], **extra)
        print(tag, "ACCEPTED")
    except Exception as e:
        s = str(e)
        if "not_found" in s or "does not exist" in s:
            print(tag, "MODEL NOT AVAILABLE")
        else:
            i = s.find("message")
            print(tag, "REJECTED", s[i:i+55] if i > -1 else s[:55])

M = "claude-sonnet-5"
print("--- does any randomness lever survive on sonnet-5? ---")
for k in [1, 5, 40]:
    probe(M, "top_k=" + str(k), top_k=k)

print()
print("--- do older models still accept temperature=0? ---")
for m in ["claude-sonnet-4-5", "claude-haiku-4-5", "claude-3-7-sonnet-latest",
          "claude-3-5-sonnet-latest", "claude-3-5-haiku-latest"]:
    probe(m, "temperature=0.0", temperature=0.0)
