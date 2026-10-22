---
name: strunk
description: >-
  UX writing on The Elements of Style. Use when writing, rewriting, or reviewing
  ANY text a user reads in a product: button labels, error messages, empty states,
  confirmation dialogs, toasts and status lines, tooltips, form labels and hints,
  onboarding screens, push and in-app notifications, settings, titles, release
  notes; when asked for microcopy, UI copy, product copy, content design, a
  strings-file audit, a terminology table, or to "make it Strunk". Also use when
  the user pastes an en.json, Localizable.strings, strings.xml or .po file, or
  asks what a button should say, how to word an error, or whether a dialog reads
  right. Three modes - write (default), review of pasted copy or a screen, and
  audit of a strings file with a deterministic linter.
---

# Strunk

Request: "$ARGUMENTS"

Doctrine from Strunk's *The Elements of Style* (1918, public domain, quoted) and White's additions (1959 and later, paraphrased), read for the interface. Where the book is silent (scanning, button pairs, error anatomy, who speaks, length) the gap is filled from named secondary sources, listed at the end, and marked as such. The book outranks the secondary sources; the user's product outranks both: an existing terminology table or voice statement wins over this skill's defaults.

Scripts live at `${CLAUDE_SKILL_DIR}/scripts`. Use that absolute path, double-quoted, in every command.

## The rules, read for the screen

Rule numbers are the 1918 edition's; the 4th edition adds four (10 is 14, 13 is 17). `references/composition.md` has the text and the full gloss.

1. **One message, one job** (rule 8). An error says what happened and what to do. A dialog asks one question. A screen carries one idea, and its title names it.
2. **The fact first** (rule 9, and the one deviation from rule 18). Readers scan the first two words of a line and move on. Titles, labels, notifications, and the first sentence of any message lead with the object or the outcome: "Payment declined", "3 unread", "Invoice #214 paid". Only a sentence the user will read through puts the action at the end.
3. **Name the actor** (rule 10). "Your bank declined the card", not "Payment could not be processed". The passive is allowed when the user is the implied actor and naming them adds nothing: "File deleted". Cut "there is / there are"; dig the verb out of "perform a sync".
4. **Say what to do, not what is wrong** (rule 11). "Use at least 8 characters", not "Password is not long enough". A negative fact may stand ("No internet connection"), followed by the remedy.
5. **The object and the number** (rule 12). "Delete 3 photos?", not "Are you sure?". "Couldn't upload budget.xlsx: 14 MB, limit 10 MB", not "Something went wrong". When the product knows the particular, the message shows it.
6. **Omit needless words** (rule 13). Write the whole message, then remove every word whose removal does not change what the user will do next. "Please", "successfully", "currently", "simply", "in order to", "note that", "you can" nearly always go. "Make every word tell" is not "make it short": "Delete 3 photos" tells; "Delete" alone does not.
7. **Parallel form** (rule 15). Menu items all verbs or all nouns. Steps in one grammatical shape. Dialog buttons answer the question in its own words: "Delete photos / Keep photos", never "OK / Cancel".
8. **Related words together** (rule 16). The label beside its control, the error beside its field, the verb beside its object, "only" beside the word it limits.
9. **One tense per kind of message** (rule 17). Results in the past participle or the present fact, instructions in the imperative, promises in "we'll" only when the product can keep them.
10. **One word for one thing** (4th edition rule 12). Sign in, not log in on one screen and login on another. The terminology table in `references/elements.md` is a deliverable of every write and audit.
11. **The product in the background** (White 1, 13, 17). Nobody speaks by default: imperatives and facts. "We" only to promise a later action. The user's "me/my" only for consent and ownership. Never two speakers on one screen. `references/voice.md`.
12. **No breeziness, no overstatement, no qualifiers, no fancy words** (White 9, 7, 8, 14). No "Oops", no emoji in errors, no "Awesome!", no "a little while", no "utilize". Warmth comes from being specific and useful, not from exclamation marks. `references/style.md`.

White's own caveat applies: these are cautions, not laws, and all of them bend to clarity (reminder 16). When a short, positive, active string is ambiguous, write the longer one.

Banned without discussion: "Are you sure?", "Something went wrong" as the whole message, "Oops", "Please" in an instruction, "successfully", "Invalid X" as the whole error, "Learn more" as the whole link, "OK / Cancel" on a destructive dialog, a title that reads "Error".

## Workflow: write (default)

0. **Name the element and the moment.** Which element from `references/elements.md` (button, error, empty state, dialog, status, tooltip, label, onboarding, notification, setting, title)? What was the user doing, what just happened, what must they do next? Who speaks on this screen (`references/voice.md`)? Hard limits: characters, lines, platform. If the product has a terminology table or voice statement, read it first; if not, draft the three-line voice statement and start a table.
1. **Write the longest honest version.** What happened, why (if the user can act on it), what to do. One paragraph, no style yet. This is the message the cut is measured against.
2. **Cut by rule 13.** Remove every word whose removal does not change the user's next action. Keep the object, the number, the actor when it is not the user, and the verb of the next step.
3. **Actor** (rule 10): is the subject the one who did it?
4. **Positive** (rule 11): is every instruction an instruction?
5. **Concrete** (rule 12): does it name the thing and the number the product knows?
6. **Parallel and consistent** (rules 15, 4th.12): do pairs and lists share a form; is every term the table's term?
7. **Front-load**: are the first two words the ones that matter?
8. **Voice pass** (White): read it aloud as a help-desk answer. Cut the breeziness, the claims, the qualifiers, the "we".
9. **Lint and render.** Run the script on the strings, then show each string in its element: a button with its chrome, a dialog with its title and both buttons, an error beside its field. Never deliver a bare string without saying where it sits.
   ```
   uv run --locked "${CLAUDE_SKILL_DIR}/scripts/copy_check.py" --text "Couldn't send. Check your connection and try again."
   uv run --locked "${CLAUDE_SKILL_DIR}/scripts/copy_check.py" en.json
   ```
   The linter finds candidates; say which warns you accept and which you reject, and why.

Output: a table of element → copy, each row with the rule ids applied and a note when a constraint forced a choice; the terminology table (new or updated); the voice statement if drafted. Offer alternatives only when a genuine question of tone or product decision is open, and say what decides it. Show before/after when rewriting.

## Workflow: review

For pasted copy, a screenshot description, a flow, or a strings file. Use `references/review-rubric.md`. Findings in severity order: does the user know what to do > consistency > concision > voice > form. Each finding: rule id, quoted string, rewrite. With a strings file, run the linter first and attach its summary. A clean screen gets a short report.

## Workflow: audit

For a strings file (`.json` flat or nested, Apple `.strings`, Android `strings.xml`, gettext `.po`) or a plain-text file of one string per paragraph.

```
uv run --locked "${CLAUDE_SKILL_DIR}/scripts/copy_check.py" path/to/en.json
uv run --locked "${CLAUDE_SKILL_DIR}/scripts/copy_check.py" path/to/en.json --json
```

The script reports per string (rules 10, 11, 12, 13, 15, White 7, 8, 9, 14) and per file (4th.12 terminology collisions, V.10 mixed case and mixed ellipsis), plus words per string. Exit 0 when nothing warns. Then do what it cannot: check speakers per screen, button pairs, whether each error names its object, and build or update the terminology table from the collisions it found. Deliver: the linter summary, the accepted findings with rewrites, the terminology table.

## Screen deviations from the book

- Emphasis goes first, not last, in anything scanned (rule 18; NN/g on reading on screen).
- Fragments are right for labels, titles, buttons, and one-line status; full sentences for errors, dialog bodies, tooltips that explain.
- Numerals always, even below ten, in interface text (Strunk's rule for dates and serial numbers, extended; NN/g); spelled-out numbers only in running prose such as help articles.
- Serial comma stays (Strunk rule 2; Google, Microsoft, Material).
- Contractions are allowed and usually better ("Couldn't send").
- Case: one convention per element type, chosen once (sentence case is the modern platform default); no end period on buttons, labels, titles, one-line status; a period on full sentences.

## Sources

Primary: William Strunk Jr., *The Elements of Style*, 1918, public domain, Project Gutenberg #37134 (quoted in `references/composition.md` and `references/lexicon.md`). Strunk & White, 4th edition, 2000: headings and rule numbers only; White's chapter V is paraphrased in `references/style.md`, never quoted.

Secondary, for what the book does not cover, cited by name in the references: Nielsen Norman Group (How Users Read on the Web 1997; F-Shaped Pattern 2017; First 2 Words 2009; Error-Message Guidelines 2023; Confirmation Dialogs 2018; Empty States 2021; Plain Language 2017); Apple Human Interface Guidelines, Writing and Alerts; Google developer documentation style guide (highlights, tense, numbers) and Material writing guidelines; Microsoft Writing Style Guide (top 10 tips, scannable content) and Windows app writing style; Mailchimp Content Style Guide; the bureau.ru advice column (Ильяхов, Бирман), cited by date, with only the advice that applies to English carried over. URLs and verification status are in the repository README.
