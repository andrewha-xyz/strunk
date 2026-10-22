# Review rubric

Use for the review workflow (a string, a screen, a flow, or a strings file). Report findings in severity order; each finding carries the rule id, the quoted text, and a concrete rewrite. Do not pad: a clean screen gets a short report.

## Order of severity

1. **Does the user know what to do?** The message fails if, after reading it, the user cannot tell what happened, which thing it concerns, or what to do next. Rules 12 (vague), 11 (negative where an instruction belongs), 10 (actor hidden), 9 (the fact not first). These outrank everything else.
2. **Consistency.** Two words for one thing, two speakers on one screen, two case conventions, two tenses for one kind of event. Rules 4th.12, 15, 17, V.10, V.13.
3. **Concision.** Needless words, needless sentences, explanation of the obvious. Rules 13, V.6, V.11.
4. **Voice.** Breeziness, overstatement, qualifiers, fancy words, product in the foreground, opinion. Reminders 9, 7, 8, 14, 1, 17.
5. **Form.** Punctuation, case within one string, ellipsis, abbreviations. Rule 3 of the usage chapter where it applies; V.10, V.19.

## Scores

Give each of the five groups one of: clean, minor, blocking. "Blocking" in group 1 means the string must not ship. Then one line of overall verdict.

## Finding format

```
[blocking] rule 12 · auth.error.generic · "Something went wrong"
  The user cannot tell whether to retry, wait, or give up.
  → "Couldn't sign in. Check your connection and try again."
```

## Checks per element

Run the questions for the element from `elements.md`:

- Button: verb? object when needed? pair in parallel, answering the question? standard word?
- Link: names the destination? informative word first?
- Dialog: question with its object? consequence stated as a fact? buttons are the two answers? should it exist at all (undo instead)?
- Error: failed outcome first? actor named? remedy as an instruction? no "oops", no "sorry", no "please"?
- Empty state: what this is, the action? no "there are no"?
- Status: result named, no "successfully", no exclamation mark, one tense?
- Tooltip: adds a fact the label lacks?
- Label: noun? hint next to it with the format or the benefit?
- Onboarding: one idea per screen, parallel steps, no claims?
- Notification: object first, one fact?
- Setting: describes the on state? "only" in the right place?

## With a strings file

Run `copy_check.py` first and attach its summary. Then read the strings the linter cannot judge: speakers across a screen, parallelism of button pairs, whether each error names its object. The linter's warns are candidates, not verdicts; say which ones you accept and which you reject, with the reason.
