import anthropic
c = anthropic.Anthropic()
M = "claude-sonnet-5"

def probe(label, **extra):
    try:
        c.messages.create(model=M, max_tokens=4,
                          messages=[{"role": "user", "content": "hi"}], **extra)
        print(label.ljust(24), "ACCEPTED")
    except Exception as e:
        s = str(e)
        i = s.find("message")
        print(label.ljust(24), "REJECTED", s[i:i+70] if i > -1 else s[:70])

probe("(no temperature)")
for t in [1.0, 0.999, 0.9, 0.7, 0.5, 0.3, 0.1, 0.0]:
    probe("temperature=" + str(t), temperature=t)
probe("top_p=0.5", top_p=0.5)
probe("top_p=0.1", top_p=0.1)
