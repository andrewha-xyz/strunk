# Elements: what each kind of interface text is for, and which rules bite

Each entry gives the element's job, its anatomy, the Strunk rules (1918 numbers, `composition.md`) and White reminders (V.n, `style.md`) that most often fail there, a length budget with the strength of its source, and a before/after pair. Budgets are secondary: Strunk's rule is "make every word tell," and the numbers below are what platform guides and reading research say a reader will take in. The sources are listed at the end of SKILL.md.

The before/after pairs are invented. They are not from any real product.

## Button

Job: name the action that happens when it is pressed, so the user can predict the result before pressing. A button is an answer to the question "what will this do?"

Anatomy: verb, plus the object when the object is not obvious from the screen. The 4th-edition and platform convention: buttons start with a verb (Apple HIG Writing; Microsoft; Mailchimp). bureau.ru (Бирман, 2017-04-18) makes the same split: a command is a verb, a navigation item is a noun naming its destination. "New X" reads as a verb in interfaces and works only for clearly repeatable objects (bureau.ru 2018-04-03); otherwise "Open account", "Add user".

Rules that bite: 13 (the verb and nothing else), 12 (the object when the verb alone is ambiguous: "Delete" what?), 15 (pairs in parallel form, answering the question), V.21 (the standard verb for the standard action), V.9 (no "Let's go!").

Budget: one or two words describing the result (Apple Alerts); "a couple short words" (Microsoft). No end punctuation (Microsoft, Material). Trailing ellipsis only when the button opens a further step that needs input (Apple; bureau.ru 2017-05-02).

| before | after | rule |
|---|---|---|
| Submit | Send message | 12 |
| Click here to continue | Continue | 13, 12 |
| Let's do it! | Start | V.9, V.21 |
| Yes / No | Delete photo / Keep photo | 15 |
| Proceed to checkout | Check out | 13 |
| Export (one screen), Download (next screen) | one of them, product-wide; or name the outcome: Save to device | 4th.12 (bureau.ru 2024-02-11) |

## Link

Job: name what is behind it, so the reader can decide without clicking. Readers see about the first two words of a link (NN/g, First 2 Words).

Rules that bite: 12 (the destination, not "here" or "more"), 18-deviation (the informative word first), 13.

"Learn more", "Read more", "Details", "Click here" are empty link text; several on one page are indistinguishable (bureau.ru 2022-09-13 and 2010-11-23; NN/g F-pattern). Put the link on the phrase that names the content: "How fees are calculated", "Terms of the offer". Better still, put the content there.

| before | after | rule |
|---|---|---|
| To see our pricing, click here | Pricing | 12, 13 |
| Learn more | How we use your location | 12 |
| More details about the offer | Offer terms: ends 31 Mar, new customers only | 12, V.11 |

## Menu and navigation item

Job: name a place or a category. Nouns, parallel across the menu (bureau.ru 2017-05-02; rule 15). Commands in a menu are verbs, parallel among themselves ("Edit, Share, Delete"). Do not mix the two forms in one list without a separator.

| before | after | rule |
|---|---|---|
| Go to settings · Your profile · Help me | Settings · Profile · Help | 15, 13 |
| Edit · Sharing · Delete this | Edit · Share · Delete | 15 |

## Dialog and confirmation

Job: ask one question whose answer the product needs before it can act, and offer the answers.

Anatomy: title = the question with its object ("Delete 3 photos?"); message, only if it adds something the title did not (the consequence: "They'll be removed from all your devices"); buttons = the two answers in the same form, the destructive one named for its result. Never "Are you sure?" (rule 12); never a title "Error" or "Warning" (Apple Alerts; bureau.ru 2015-04-19). "OK" only when the dialog is purely informational (Apple). The "Cancel / Cancel order" trap is solved by putting the substance of each choice on its button: "Back to editing" / "Discard changes" (bureau.ru 2024-12-03, in English).

Before writing the dialog, ask whether it should exist. Routine confirmations train people to confirm without reading; undo with clear feedback is the better design where it can be built (NN/g Confirmation Dialogs; bureau.ru 2018-06-19, 2024-02-13). Reserve dialogs for rare, costly or irreversible actions.

Rules that bite: 12, 15, 13, 11 (state the consequence as a fact), V.7 (no drama in a destructive dialog).

Budget: title at most two lines (Apple); message one or two sentences; buttons one or two words.

| before | after | rule |
|---|---|---|
| Are you sure you want to proceed? OK / Cancel | Delete 3 photos? They'll be removed from all your devices. · Delete photos / Keep photos | 12, 15 |
| Warning! Unsaved changes will be lost. Cancel / Cancel | Leave without saving? · Discard changes / Back to editing | 12, 15, V.7 |
| Sign out? Yes / No | Sign out of Acme on this phone? · Sign out / Stay signed in | 12, 15 |

## Error

Job: tell the user what did not happen and what to do next, at the place where it happened.

Anatomy, for a field error: the positive instruction ("Use at least 8 characters"), next to the field. For a system error: the failed outcome as the first words ("Payment declined", "Couldn't send"), then the cause if the product knows it and the user can act on it, then the next step with a time where there is one ("Try again in a minute"). bureau.ru (Ильяхов, 2015-04-19) gives this exact order and adds: if the cause is unknown, still say what the user can do. NN/g's error guidelines agree: precise description, constructive advice, no blame, preserve the user's input.

Rules that bite: 11 (instruction, not negation: "Enter a date like 14 Mar 2026", not "Invalid date"), 10 (name the actor: "Your bank declined the card"), 12 (the object and the number), 13 (no "please", no "an error occurred"), V.9 (no "Oops"), V.1 (no reflexive "Sorry"), 9 (the fact first, the digression never).

Budget: one line for a field error; one to two sentences for a system error; a title plus one sentence for an alert.

| before | after | rule |
|---|---|---|
| Invalid email | Enter an email like name@example.com | 11, 12 |
| Oops! Something went wrong. Please try again later. | Couldn't send. Check your connection and try again. | V.9, 12, 13 |
| Your payment could not be processed at this time due to an error. | Your bank declined the card. Try another card or call the number on the back. | 10, 13, 12 |
| Error: file upload failed | Couldn't upload budget.xlsx: it's 14 MB and the limit is 10 MB. | 12, 11 |
| Password is not long enough | Use at least 8 characters | 11 |
| We're sorry, but we are unable to find any results for your search. | No results for "invoce". Check the spelling or try a shorter word. | 13, V.1, 11 |

## Empty state

Job: say what this place will hold and give the one action that fills it. It is temporary, so it never carries information the user will need later (Apple HIG).

Anatomy: what this is, why it is empty if that is not obvious, the action. NN/g adds: never show "no records" while the list is still loading.

Rules that bite: 10 (no "There are no items"), 12 (the real noun), 13, V.7 (no "Nothing to see here!"), V.9.

Budget: one or two sentences and a button.

| before | after | rule |
|---|---|---|
| There are currently no items in your list. | No invoices yet. · Create invoice | 10, 12, 13 |
| Nothing here! Why not add something? | Your inbox is empty. | V.9, V.7, 12 |
| You haven't connected any accounts. Connect one to get started and unlock the full power of Acme. | No accounts connected. · Connect a bank | 13, V.7 |

## Status, toast, snackbar

Job: confirm that something the user did has happened, in the fewest words that name the result. "Successfully" is the word that never belongs here; a verb in the past tense already succeeded (bureau.ru 2015-04-19; rule 13). The best status names the concrete result: "Sent to Maria", "Saved to Drafts", "Transferred €120 to Savings". For a confirmation of the user's own action, a check mark plus the object can replace the sentence (bureau.ru 2021-12-07).

Rules that bite: 13, 12, 17 (one tense for all status strings), V.7 (no exclamation marks).

Budget: one line; two on a phone (legacy Material snackbar guidance). No end period on a one-line status (Google developer style; bureau.ru 2017-10-01). Choose the convention once and hold to it.

| before | after | rule |
|---|---|---|
| Your changes have been saved successfully! | Saved | 13, V.7 |
| Email was successfully verified. | ✓ name@example.com verified | 13, 12 |
| The transfer has been completed. | Sent €120 to Savings | 12, 10 |

## Tooltip and help text

Job: add the one fact the label could not carry. A tooltip that restates the label is over-explaining (V.11); a control that needs a tooltip to be understood may need a better label instead.

Rules that bite: V.11, 13, 12.

Budget: one sentence. Full sentences take a period (Microsoft); a fragment does not.

| before | after | rule |
|---|---|---|
| Save: click this to save your document. | (delete; the label says it) | V.11 |
| This setting allows you to control whether or not notifications are shown. | Shows a badge on the app icon for unread messages. | 13, 12 |

## Label, placeholder, field hint

Job: a label names what goes in the field. A hint says the format or the reason, when either is not obvious. A placeholder is not a label: it disappears when the user types and should carry nothing they need to remember.

Labels are nouns ("Email", "Card number"), not commands ("Enter your email") and not questions, unless the form is written as a conversation throughout. When the user may wonder why a field is asked, say the benefit in the hint: "Phone number, for password recovery" (bureau.ru 2014-01-26). Ask only for what the product needs (Mailchimp; bureau.ru).

Rules that bite: 13, 12, 15 (all labels in the same form), 16 (the hint next to its field), 11 (the format as an instruction, not "Invalid").

| before | after | rule |
|---|---|---|
| Please enter your e-mail address here | Email | 13 |
| Phone (required) | Phone, for delivery updates | 12, bureau.ru 2014-01-26 |
| Date (do not use slashes) | Date, like 14 Mar 2026 | 11 |

## Onboarding and first run

Job: get the user to the first useful action with the fewest screens. Each screen one idea (rule 8), the idea named in the title, the title front-loaded. Steps in parallel form (rule 15). No claims about how easy or powerful the product is (V.7, V.12); show the thing instead. The imperative that works on a button fails in a headline, where it gives the writer a false sense of work done (bureau.ru 2013-03-31): a headline states a fact about what the user will have.

Rules that bite: 8, 15, 13, V.7, V.12, V.1.

| before | after | rule |
|---|---|---|
| Welcome to Acme! We're thrilled to have you. Let's get you set up in just a few easy steps. | Connect a bank to see your spending | V.1, V.7, 13 |
| Step 1: Creating your profile · Step 2: You connect accounts · Step 3: Budget! | Create a profile · Connect accounts · Set a budget | 15 |

## Notification (push, in-app)

Job: one fact and, if there is one, the action. The first two words carry it; the OS truncates the rest. Front-load the object (deviation from rule 18): "Invoice #214 paid", not "You have received a payment for invoice #214".

Rules that bite: 18-deviation, 13, 12, V.7.

Budget: platform limits vary by device and vendor; a title of a few words and a body of one short sentence survive everywhere. Numbers from vendors conflict and are not law.

| before | after | rule |
|---|---|---|
| You have a new message from Maria in the Project X channel! | Maria, in Project X: "Can you review the draft?" | 18-dev, 13, V.7 |
| Reminder: Don't forget that your subscription will renew soon. | Renews Sat 19 Feb, €9.99 | 11, 12, 13 (bureau.ru 2022-05-01 on plannable dates) |

## Setting label

Job: describe what the setting does when it is on (Apple HIG), as a fact, in the user's words. One speaker for all settings on a screen (`voice.md`). Misplaced "only" is common here (rule 16).

| before | after | rule |
|---|---|---|
| Enable the notification feature | Notify me about mentions | 13, V.14, 12 |
| Only send me emails about security | Send me emails only about security | 16 |

## Title and heading

Job: name the screen or section so that it is recognizable from the first two words. Nouns for places, questions for dialogs, the fact for results. One case convention across the product (V.10). No end period (Microsoft, Mailchimp).

## Terminology table

Rule 4th.12 ("choose a suitable design and hold to it") is enforced by a table the team keeps. The write and audit workflows produce or update it. Format:

| thing | the word | not | notes |
|---|---|---|---|
| entering the account | sign in (verb), sign-in (noun) | log in, login | Apple and Google use sign in; pick what the user's market uses (bureau.ru 2012-12-16: copy native sites) |
| creating an account | create account | sign up, register, join | |
| removing a thing for good | delete | remove, trash, erase | "remove" for taking out of a list without deleting |
| stopping a flow | cancel | abort, dismiss | "close" for a panel with nothing pending |
| a saved-but-unsent message | draft | unsent, pending | |
