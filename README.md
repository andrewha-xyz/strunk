# strunk

UX writing on *The Elements of Style*, for Claude Code. Strunk's composition rules and White's reminders mapped to the text a user actually reads: buttons, errors, empty states, dialogs, status lines, tooltips, labels, onboarding, notifications, settings. Three workflows (write, review, audit), a deterministic linter for strings files, and an invented example.

The book outranks the secondary sources; the user's own terminology table and voice statement outrank both.

## Install

As a plugin, from this repository's marketplace:

```
/plugin marketplace add andrewha-xyz/strunk
/plugin install strunk@andrewha-xyz
```

Or copy `skills/strunk` into `~/.claude/skills/strunk`. The script runs through `uv run --locked` and has no dependencies beyond Python 3.11.

## What is in it

```
skills/strunk/
├── SKILL.md                 the twelve rules read for the screen, three workflows, deviations, sources
├── references/
│   ├── composition.md       Strunk's rules 8–18 (1918 text, quoted) with the interface gloss
│   ├── style.md             White's 21 reminders (headings only, paraphrased) with the interface gloss
│   ├── lexicon.md           words commonly misused: Strunk's list on screen, the interface extension, the linter's phrase list
│   ├── elements.md          per element: job, anatomy, rules that bite, budget with source strength, before/after
│   ├── voice.md             who is speaking: three speakers, decision table, tone without breeziness, the voice statement
│   └── review-rubric.md     severity order, scores, finding format, checks per element
├── scripts/
│   ├── copy_check.py        linter: .json, .strings, strings.xml, .po, text, --text, stdin; --json; exit 0/1/2
│   └── tests/               pytest, 42 cases
└── evals/                   three test cases in the `claude plugin eval` layout
examples/ledger/             an invented expense app: before.en.json, after.en.json, linter output, the table of changes
```

## The linter

```
uv run --locked skills/strunk/scripts/copy_check.py examples/ledger/before.en.json
uv run --locked skills/strunk/scripts/copy_check.py --text "Oops! Something went wrong. Please try again."
```

Per string: needless words (rule 13), passive and hidden actor (10), negative where an instruction belongs (11), vague where the object belongs (12), OK/Cancel pairs (15), overstatement (V.7), qualifiers (V.8), breeziness and emoji (V.9), fancy words (V.14). Per file: two words for one thing (sign in / log in / login; delete / remove; export / download; 4th-edition rule 12), mixed case conventions and mixed ellipses (V.10). Severity `warn` exits 1; `note` is for the writer to look at; a file that cannot be parsed exits 2. Apple `.strings` are tokenized (comments outside strings, escapes, UTF-16), Android `strings.xml` follows the platform's whitespace and quoting rules and includes `string-array` and `plurals`, gettext `.po` keeps `msgctxt` in the key and lints every `msgstr[n]`. The linter finds candidates; it cannot see the screen, so the workflow says which warns to accept.

On the example: the before file gets 33 warns and 19 notes; the after file 0 warns and 4 notes.

## Sources and verification

Rule numbers in the skill are the 1918 edition's (rule 13 is "Omit needless words"); the 4th edition adds four (17). Both numbers are given in `references/composition.md`.

Primary:

- William Strunk Jr., *The Elements of Style*, 1918 (privately printed; the 1919 reprint). Public domain in the US. Project Gutenberg #37134: https://www.gutenberg.org/ebooks/37134 (plain text https://www.gutenberg.org/ebooks/37134.txt.utf-8). Read in full; quoted in `composition.md` and `lexicon.md`.
- Strunk & White, *The Elements of Style*, 4th edition, 2000. In copyright. Used for rule numbering, the headings of chapter V's twenty-one reminders, and paraphrase only; no body text is quoted. The US Copyright Office's note on the book's history: https://www.copyright.gov/history/lore/pdfs/201805%20CLore_MayJune2018.pdf

Secondary, for what the book does not cover. Fetched and read 2026-10-22 unless marked.

- Nielsen Norman Group. How Users Read on the Web (1997) https://www.nngroup.com/articles/how-users-read-on-the-web/ · F-Shaped Pattern of Reading on the Web (2017) https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ · First 2 Words (2009) https://www.nngroup.com/articles/first-2-words-a-signal-for-scanning/ · Error-Message Guidelines (2023) https://www.nngroup.com/articles/error-message-guidelines/ · Confirmation Dialogs (2018) https://www.nngroup.com/articles/confirmation-dialog/ · Empty States (2021) https://www.nngroup.com/articles/empty-state-interface-design/ · Plain Language Is for Everyone (2017) https://www.nngroup.com/articles/plain-language-experts/
- Apple Human Interface Guidelines, Writing https://developer.apple.com/design/human-interface-guidelines/writing and Alerts https://developer.apple.com/design/human-interface-guidelines/alerts (pages are script-rendered; the text was read from Apple's own JSON feed for the same pages).
- Google developer documentation style guide: highlights https://developers.google.com/style/highlights · tense https://developers.google.com/style/tense · numbers https://developers.google.com/style/numbers. Material writing guidelines: the current page https://m3.material.io/foundations/content-design/style-guide is script-only and was not readable by the fetch tool; the rules cited come from the legacy page https://m1.material.io/style/writing.html and are marked secondhand where used.
- Microsoft Writing Style Guide, top 10 tips https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice and scannable content https://learn.microsoft.com/en-us/style-guide/scannable-content/ · Windows app writing style https://learn.microsoft.com/windows/uwp/design/style/writing-style · Win32 error-message guidelines https://learn.microsoft.com/en-us/windows/win32/debug/error-message-guidelines
- Mailchimp Content Style Guide https://styleguide.mailchimp.com/ (voice and tone, writing principles, web elements, TL;DR, writing for translation). Its two pages disagree on button capitalization, so it is not cited on that point.
- bureau.ru, the advice column of Artyom Gorbunov's bureau (Ильяхов, Бирман), in Russian. Cited by date in the references, as `bureau.ru YYYY-MM-DD`, meaning https://bureau.ru/soviet/YYYYMMDD/. Only the advice that applies to English interface text is carried over; rules about Russian grammar, case endings, ты/вы, or typography are left out. Entries used: 2015-04-19 (status and error messages), 2017-04-18 and 2017-05-02 (verbs on buttons, nouns in navigation), 2018-04-03 ("New X"), 2024-12-03 (Cancel / Discard), 2018-06-19 and 2024-02-13 (confirmations versus undo), 2022-09-13 and 2010-11-23 (empty link text), 2024-02-11 (Export / Download, one rule), 2014-01-26 (field labels by benefit), 2021-12-07 (a check mark as confirmation), 2017-10-01 (no period on notifications), 2013-03-31 (imperatives in headlines), 2021-05-02 (cutting "we/our"), 2022-03-06 (one register), 2012-12-16 (sign in / log in, copy native sites), 2022-05-01 (plannable dates), 2018-09-16 (modal verbs), 2016-02-21 (infostyle and Strunk & White), 2014-12-14 (stop-word categories).
- Not used as sources, because no authoritative text could be verified online: Redish, *Letting Go of the Words*; Yifrah, *Microcopy*. Their themes overlap with the above and are not cited.

Length budgets in `elements.md` carry the strength of their source (official platform guide, reading research, vendor, or gap). No authoritative character count exists for tooltips or toasts; the skill says "one line, one idea" there rather than inventing a number.

## Examples

`examples/ledger` is an invented expense app. Nothing in it is from a real product.

## License

MIT.
