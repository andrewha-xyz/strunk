---
tags: [strunk]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

i'm building a mobile wallet app called Pocket (iOS + Android). card payment at checkout can fail in 5 ways: bank declined the card, insufficient funds, network timeout on our side, 3-D Secure verification failed, card expired. i need the full error set for the checkout screen: title + body + the buttons for each (retry, change card, whatever makes sense). we're a serious fintech, no jokes, no emoji. write it up as errors.md showing each error in its element and also give me the strings as en.json (keys like checkout.error.declined.title). save both files here, next to each other.
