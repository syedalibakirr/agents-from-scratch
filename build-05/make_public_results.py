#!/usr/bin/env python3
"""
Build 05: write the public results file.

run_test.py recorded every run's full answer, and those answers describe a
private codebase. The original is kept in runs_private/ (gitignored). This
script writes RESULTS_20_RUNS_DEFAULT.md with each answer replaced by its
length plus the folder the run named as the live backend, which is all the
answer split in the README needs. Tool calls, counts and sequences are
unchanged.

The folder each run named was read by hand from the original answers:
runs 3 and 10 answered `server`; the other 18 answered `python-backend`.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "runs_private", "RESULTS_20_RUNS_DEFAULT.md")
OUT = os.path.join(HERE, "RESULTS_20_RUNS_DEFAULT.md")

WRONG_RUNS = {3, 10}   # 1-based position in the file
HEAD_RE = re.compile(r"^## Q\d+ .*$", re.M)
ANSWER_RE = re.compile(r"(\*\*Final answer \(verbatim\):\*\*\s*```)\n?(.*)(```)", re.S)

TARGET_OLD = "**Target repo:** an external codebase (`~/Desktop/Cursor - LP`, not part of this repo), fixed across all 20 runs."
TARGET_NEW = "**Target repo:** Triptic's private codebase (the working repo; builds moved to copies from Build 07 on), fixed across all 20 runs."


def main():
    text = open(SRC, encoding="utf-8").read().replace(TARGET_OLD, TARGET_NEW)
    heads = list(HEAD_RE.finditer(text))
    out = [text[:heads[0].start()]]
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        block = text[m.start():end]
        run = i + 1
        named = "server" if run in WRONG_RUNS else "python-backend"

        def repl(a):
            body = a.group(2).strip()
            return (a.group(1).replace("**Final answer (verbatim):**", "**Final answer:**")
                    + f"\n[redacted: {len(body)} chars about a private codebase]\n"
                    + f"Named as the live backend: {named}\n" + a.group(3))

        out.append(ANSWER_RE.sub(repl, block, count=1))
    open(OUT, "w", encoding="utf-8").write("".join(out))
    print(f"wrote {OUT}: {len(heads)} runs")


if __name__ == "__main__":
    main()
