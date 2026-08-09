# Lessons — Agents From Scratch

The transferable principles, not the build-by-build story. Each entry earned by
something that actually broke, in a real run, and generalizes past the build that
found it. Bugs specific to one build stay in that build's own README; this file is
for the pattern underneath.

New entries get added after every build, at the top.

---

## Build 1 — the loop

**A tool's description is its entire interface to the model. The model never sees
your code.** It only sees the string in `SCHEMA`. A vague description
("search the repo for a string") is indistinguishable, from the model's side, from a
vague spec handed to a new engineer — it will do something reasonable-sounding that
isn't what you meant. When a tool misbehaves, check the description before you
suspect the model.

**Log every step, not just the final answer.** The final answer in Build 1 was
correct. The log was what showed it got there by accident — 5 of 6 searches wasted,
zero source files actually read. Without a log, a correct answer for the wrong
reason looks identical to a correct answer for the right reason. You can't tell them
apart from the outside.

**Good documentation is now infrastructure for AI, not just for humans.** The agent
solved the task by reading `CLAUDE.md` — a file written for a different tool
entirely. Any doc in a repo is now a resource any agent can find and use, whether
you intended that or not. Worth writing docs *knowing* they'll be read this way.

**An agent can repeat an identical call and not notice.** `list_files` ran twice in
one 11-call trace, returning the same result both times. Nothing about the loop
prevents wasted, redundant work — that has to be designed in, not assumed.

**Hard truncation is a design decision with consequences, not a neutral default.**
`read_file()` cropping at 2,000 characters means the agent's view of every file is
partial. Fine for Build 1 — worth remembering it's a choice, and revisiting once a
build actually needs to read something long.

---

## How to add to this file

After a build ships: one entry, dated by build number, only for things that would
change how you build *the next* thing — not a recap of what happened (that's the
build's own README) and not a bug tracked for a specific future fix (that's the
"Known bugs" list in the build folder). This file is the accumulated judgment, kept
short enough that build 20 can still skim build 1.
