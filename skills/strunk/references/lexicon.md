# Lexicon: words and expressions commonly misused, on screen

Part 1 is Strunk's chapter V (1918, public domain), kept to the entries that still appear in interface text, each with his verdict and the screen case. Part 2 is this skill's extension: the words interface writers reach for that Strunk did not live to see. Part 3 is the needless-phrase list that `scripts/copy_check.py` flags under rule 13. The rule numbers are the 1918 numbers (see `composition.md`).

Strunk's own instruction for this chapter: when one of these words slips in, "his proper course will probably be not to patch up the sentence by substituting one word or set of words for another, but to recast it completely."

## Part 1. From Strunk, chapter V

| word | Strunk | on screen |
|---|---|---|
| all right | "Always written as two words." Idiomatic only as a detached "Agreed." | A button reading "Alright" is misspelled; "OK" is the conventional token, but a button should name the action (rule 15 in `composition.md`). |
| as to whether | "*Whether* is sufficient." | "Decide as to whether you want to continue" is "Decide whether to continue", and better "Continue?" |
| case | "In these two senses, the word is usually unnecessary." "In many cases" is "Many of". | "In case of an error" is "If something fails"; "In this case" usually deletes. |
| certainly | "Used indiscriminately by some writers, much as others use *very*, to intensify any and every statement." | Delete. "Your data is certainly safe" convinces nobody. |
| character, nature | "Often simply redundant": "acts of a hostile character" is "hostile acts". | "Errors of a temporary nature" is "temporary errors". |
| claim (verb) | Means *lay claim to*; not a synonym of *say*. | "Claim your reward" is the one correct use; "The app claims the file is missing" is not. |
| data | "A plural, like *phenomena* and *strata*." | Modern usage treats it as a mass noun ("Your data is encrypted"); the 4th edition softens on this. Pick one form across the product (consistency) and prefer the concrete noun anyway: "your photos", "your messages", not "your data". |
| dependable | "A needless substitute for *reliable*." | Marketing word; delete from product copy. |
| due to | Correct only as a predicate adjective; not an adverbial *because of*. | "Upload failed due to a network error" is "Couldn't upload: no connection". |
| effect | As noun, *result*; vague in "an Oriental effect". | "This setting has no effect" is fine; "effects" as a vague noun is not. |
| etc. | "Not to be used if ... the reader would be left in doubt as to any important particulars." Never after *such as*. | Never in an interface. The reader cannot ask what else. List the items or give the count. |
| fact, the fact that | "Should be revised out of every sentence in which it occurs." | "Due to the fact that your session expired" is "Your session expired". |
| factor, feature | "Hackneyed"; "usually adds nothing to the sentence." | "This feature lets you..." is "You can...". Name the thing the user does, not the category of thing it is. |
| however (first in clause) | In the sense *nevertheless*, "not to come first in its sentence." | Rarely needed on screen at all; a second sentence usually does the turn: "Saved. Sharing is off." |
| interesting | "Instead of announcing that what you are about to tell is interesting, make it so." | Same for "exciting", "amazing", "great news". Delete the announcement. |
| kind of, sort of | Not a substitute for *rather* or *something like*. | "Something kind of went wrong" is evasion; say what went wrong. |
| less | "Should not be misused for *fewer*." Quantity vs number. | "Less than 3 items" is "Fewer than 3 items"; "less than 10 MB" is right. |
| literal, literally | "Often incorrectly used in support of exaggeration." | Delete. |
| lose out, try out, sign up | "Meant to be more emphatic than *lose*, but actually less so." | *Sign up* has become the idiom for creating an account and is acceptable where the product uses it consistently. "Try out" is "Try". |
| most (for almost) | "Not to be used for *almost*." | "Most done" is "Almost done". |
| one of the most | "Threadbare and forcible-feeble." | Marketing opener; never in the interface. |
| people | "The people" is political; use "persons" for a counted number (the 4th edition relaxes this). | "3 people" is current usage; keep it. |
| phase | A stage of transition; not a synonym of *aspect*. | Fine for "Phase 2 of setup"; wrong in "the phase of the problem". |
| possess | "Not to be used as a mere substitute for *have* or *own*." | "You possess 3 licenses" is "You have 3 licenses". |
| respective, respectively | "May usually be omitted with advantage." | "Enter your email and password in their respective fields" is "Enter your email and password". |
| so (intensifier) | "Avoid, in writing, the use of *so* as an intensifier." | "So easy", "so fast": delete. |
| state (for say) | "Not to be used as a mere substitute for *say*." | "Please state your reason" is "Why?" or "Reason". |
| system | "Frequently used without need." | "The system was unable to" is "We couldn't"; "Your system settings" is "Settings". |
| thanking you in advance | Sounds as if "it will not be worth my while to write to you again." | "Thanks for your patience" before the user has shown any is the screen version. Delete, or thank after. |
| very | "Use this word sparingly. Where emphasis is necessary, use words strong in themselves." | Delete. "Very important" is "Important" or the reason it matters. |
| while (for and, but, although) | "Avoid the indiscriminate use of this word." | "While we save your changes" is a correct temporal use; "While this plan is cheaper" is *although*. |
| worth while | "Overworked as a term of vague approval." | Delete. |
| would, should, shall | Conditional and future usage; largely obsolete distinctions. | Not a screen problem. Use "will" for promises the product can keep and the imperative for instructions. |

## Part 2. Extension for the interface

Words that violate a Strunk rule without being in his list. The column says which rule.

| word or phrase | rule | use instead |
|---|---|---|
| utilize, leverage (verb) | 12, fancy words (`style.md`) | use |
| finalize, prioritize, incentivize, operationalize | fancy words | finish, rank, reward; or recast |
| in order to | 13 | to |
| prior to | 13, fancy words | before |
| at this time, currently, at the moment | 13 | delete; the present tense already says it |
| please | 13 | delete from instructions and labels ("Enter your email"); keep only when asking a favor the user may refuse ("Please rate the app") |
| successfully | 13 | delete: "Saved", not "Saved successfully"; a verb in the past tense already succeeded |
| simply, just, easily, quickly | 13, do not explain too much | delete; they claim the task is easy, which the user judges |
| note that, please note, be aware that, keep in mind | 13 | delete the frame; say the thing |
| you can, you may, you are able to | 13 | the imperative or the fact: "Edit later from Settings" |
| it is recommended that, we recommend | 13, 10 | the imperative, or name who recommends and why |
| there is / there are | 10 | the thing as subject: "No results" not "There are no results" |
| was unable to, could not be, failed to be | 10 | the actor: "Couldn't save", "Your bank declined the card" |
| process, perform, execute, initiate | 10 (verb buried in a noun) | the verb: "Sync", "Pay", "Start" |
| invalid, incorrect, wrong | 11 | the positive instruction: "Use 8 or more characters", "Enter the code from the email" |
| something went wrong, an error occurred, unexpected error | 12 | what went wrong, or if the product truly does not know, what to do: "Try again in a minute" |
| are you sure? | 12 | the question with its object: "Delete 3 photos?" |
| item(s), element(s), object(s), entry, record | 12 | the real noun: photo, invoice, message, contact |
| changes | 12 | often the real noun: "Save profile", "Discard edits to Budget" |
| submit | 12 | what submitting does: "Send", "Pay $12", "Create account" |
| OK, Cancel (as the only pair) | 15 | the answers to the question: "Delete" / "Keep", "Leave" / "Stay" |
| learn more (bare) | 12 | what the link opens: "How fees are calculated" |
| click here | 12, 16 | the destination as the link text |
| oops, whoops, uh oh, yikes | breezy manner (`style.md`) | the fact |
| awesome, amazing, great job, yay, woohoo | overstatement | the fact: "Done", "Sent" |
| sorry (reflexive) | place yourself in the background | delete unless the product caused harm and will fix it; then say what it will do |
| we're excited to, we're thrilled | place yourself in the background | delete; the product's feelings are not the topic |
| seamless, powerful, robust, intuitive, effortless | overstatement, fancy words | the specific fact, or nothing |
| hopefully | the 4th edition flags it | delete |
| impact (verb), -wise suffixes | the 4th edition flags them | affect; recast |
| contact us | 12 | the channel: "Email support", "Call 0800 ...", "Chat with us" |
| login (verb), log into | consistency | pick one: "Sign in" (verb) / "sign-in" (noun), product-wide |

## Part 3. Phrases the linter flags

The script reports these with the shorter form and the rule it files them under; the writer decides. Each row is a regular expression target in `copy_check.py`, case-insensitive, matched on word boundaries. Severity is `warn` unless marked `note`.

| phrase | rule | shorter |
|---|---|---|
| in order to | 13 | to |
| in order for | 13 | for |
| the fact that | 13 | (recast) |
| due to the fact that, owing to the fact that | 13 | because |
| in spite of the fact that | 13 | although |
| as to whether | 13 | whether |
| there is no doubt but that | 13 | no doubt |
| for the purpose of | 13 | to, for |
| in the event that | 13 | if |
| at this time, at this point in time, at the present time | 13 | now, or delete |
| at the moment, currently | 13 | delete |
| subsequent to | 13 | after |
| in a timely manner | 13 | promptly, or a time |
| a number of | 13 | several, or the number |
| is able to, are able to, be able to, has the ability to | 13 | can |
| please note that, please be aware that, note that, keep in mind that | 13 | delete |
| it is recommended that | 13 | (imperative) |
| successfully | 13 | delete |
| simply, easily | 13 | delete |
| just (note) | 13 | delete unless it means *only* |
| make use of | 13 | use |
| in the process of | 13 | delete |
| which is, who is, that is, which was, who was (note) | 13 | often delete |
| you can (note), please (note) | 13 | the imperative; keep *please* for a favour |
| prior to | V.14 | before |
| utilize, leverage, commence, facilitate, endeavor, initiate, terminate, finalize, prioritize | V.14 | use, use, start, help, try, start, end, finish, rank |
| very, really, quite, rather, pretty (before a word), somewhat, a bit, a little | V.8 | delete, or a stronger word, or the number |
| hopefully, literally, etc., respective(ly), in many cases | ch. V | delete or recast |
