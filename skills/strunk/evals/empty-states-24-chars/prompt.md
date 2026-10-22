---
tags: [strunk]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

notes app (Jot). our design has a hard limit: empty-state title max 24 characters, body max 80 characters, one CTA button max 16 characters. need copy for 3 empty states: no notes yet, no search results (query is shown in the UI already), no tags created. plus 3 onboarding screens (title max 24, body max 80, button max 16): create a note, organize with tags, sync across devices. our terms are 'note', 'tag', 'notebook' - never 'item' or 'entry'. sentence case. write it to copy.md with the character counts shown next to each string.
