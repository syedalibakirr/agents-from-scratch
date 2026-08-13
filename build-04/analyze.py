#!/usr/bin/env python3
"""
Build 04 — analyze the tool-description-wording experiment.

Parses every run file in runs/, filters to Q2, excludes crashed/timed-out runs,
and prints per-condition tool-call stats plus a Fisher's exact test (1-call vs
more-than-1-call) comparing A vs B and A vs C. No scipy — Fisher's exact is
implemented directly with math.comb.
"""
import math
import os
import re

RUNS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs")

FILE_CONDITIONS = {
    "A_original_round1.md": "A",
    "A_original_round2.md": "A",
    "B_info_dropped_round1.md": "B",
    "B_info_dropped_round2.md": "B",
    "C_paraphrase.md": "C",
}

CONDITION_LABELS = {
    "A": "A - original",
    "B": "B - info dropped",
    "C": "C - paraphrase",
}

RUN_RE = re.compile(r"^## Q(\d+) .*$", re.MULTILINE)


def parse_runs(text):
    """Split a results file into per-run blocks, keyed by question number."""
    headers = list(RUN_RE.finditer(text))
    runs = []
    for i, m in enumerate(headers):
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        q_num = int(m.group(1))
        block = text[start:end]
        runs.append((q_num, block))
    return runs


def tool_call_count(block):
    m = re.search(r"\*\*Tool call count:\*\*\s*(\d+)", block)
    return int(m.group(1)) if m else None


def tools_called_block(block):
    m = re.search(
        r"\*\*Tools called, in order:\*\*\s*```(.*?)```", block, re.DOTALL
    )
    return m.group(1) if m else ""


def final_answer_block(block):
    m = re.search(r"\*\*Final answer \(verbatim\):\*\*\s*```(.*?)```", block, re.DOTALL)
    return m.group(1) if m else ""


def is_excluded(final_answer):
    return "agent crashed" in final_answer or "TIMED OUT" in final_answer


def load_condition_data():
    data = {"A": [], "B": [], "C": []}
    for fname, condition in FILE_CONDITIONS.items():
        path = os.path.join(RUNS_DIR, fname)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        for q_num, block in parse_runs(text):
            if q_num != 2:
                continue
            answer = final_answer_block(block)
            if is_excluded(answer):
                continue
            count = tool_call_count(block)
            if count is None:
                continue
            used_read_file = "read_file(" in tools_called_block(block)
            data[condition].append({"calls": count, "read_file": used_read_file})
    return data


def fisher_exact_two_tailed(a, b, c, d):
    """Two-tailed Fisher's exact test for a 2x2 table [[a,b],[c,d]]."""
    n = a + b + c + d
    row1, row2 = a + b, c + d
    col1, col2 = a + c, b + d

    def table_p(x):
        y1 = row1 - x
        y2 = col1 - x
        y3 = row2 - y2
        return (
            math.comb(row1, x)
            * math.comb(row2, y3)
            / math.comb(n, col1)
        )

    observed_p = table_p(a)
    lo = max(0, col1 - row2)
    hi = min(row1, col1)
    total = 0.0
    for x in range(lo, hi + 1):
        p = table_p(x)
        if p <= observed_p * (1 + 1e-9):
            total += p
    return total


def split_1_vs_more(runs):
    one = sum(1 for r in runs if r["calls"] == 1)
    more = sum(1 for r in runs if r["calls"] > 1)
    return one, more


def print_table(data):
    for cond in ["A", "B", "C"]:
        runs = data[cond]
        calls = [r["calls"] for r in runs]
        n = len(calls)
        total = sum(calls)
        mean = total / n if n else 0.0
        more_than_one = sum(1 for c in calls if c > 1)
        read_file_count = sum(1 for r in runs if r["read_file"])

        print(f"\nCondition {CONDITION_LABELS[cond]}")
        print(f"  n              = {n}")
        print(f"  tool calls     = {calls}")
        print(f"  total          = {total}")
        print(f"  mean           = {mean:.2f}")
        print(f"  min            = {min(calls) if calls else 'n/a'}")
        print(f"  max            = {max(calls) if calls else 'n/a'}")
        print(f"  >1 call        = {more_than_one} of {n}")
        print(f"  used read_file = {read_file_count} of {n}")


def main():
    data = load_condition_data()
    print_table(data)

    a1, a2 = split_1_vs_more(data["A"])
    b1, b2 = split_1_vs_more(data["B"])
    c1, c2 = split_1_vs_more(data["C"])

    p_ab = fisher_exact_two_tailed(a1, a2, b1, b2)
    p_ac = fisher_exact_two_tailed(a1, a2, c1, c2)

    print("\nFisher's exact test (1-call vs more-than-1-call split), two-tailed")
    print(f"  A vs B: A=({a1},{a2}) B=({b1},{b2})  p = {p_ab:.3f}")
    print(f"  A vs C: A=({a1},{a2}) C=({c1},{c2})  p = {p_ac:.3f}")


if __name__ == "__main__":
    main()
