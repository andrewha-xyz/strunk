# Voice: who is speaking

White's reminder 13, "Make sure the reader knows who is speaking," and reminder 1, "Place yourself in the background," together decide the voice of a product. This file turns them into a decision made once per product and applied to every string.

## The three speakers

An interface has three possible speakers, and most products need all three, each in its own kind of message.

1. **Nobody.** The imperative and the plain fact. "Enter your email." "Saved." "3 unread." This is the default speaker for instructions, labels, status, and most errors. It places the product in the background because it has no pronoun at all.
2. **The product, "we".** Allowed only when the product is the actor and the user needs to know it will act: "We'll email you a receipt", "We'll delete your account in 30 days". Apple's guidance is to avoid "we" altogether and write "Unable to load content" rather than "We're having trouble loading this content"; Material allows "we" only when the app acts on the user's behalf. This skill follows Apple's test: if the sentence works without "we", cut it. "We're excited", "We think you'll love", "We're sorry" never pass the test, because the product's feelings are not information (reminders 1 and 17; bureau.ru 2021-05-02 on cutting company-centred "we/our").
3. **The user, "I" and "my".** Only where the user is the one speaking: a checkbox they tick ("Send me a copy"), a possessive that marks ownership ("My account" versus "Your account"). Material's rule: first person only for ownership. Do not mix the user's voice and the product's voice in one screen: "Send me updates" (user) next to "Save your preferences" (product to user) is two speakers at once.

"You" is the product addressing the user and belongs with speaker 2 in spirit, but it is lighter than "we" and is the standard second person of every platform guide (Google, Microsoft, Material). Use it when the sentence needs a subject and the subject is the user; prefer the imperative, which has no pronoun, when it is an instruction. Possessives sparingly: "Favorites", not "Your Favorites" (Apple).

## The decision table

Fill this in once per product; the write workflow asks for it and the audit workflow checks against it.

| kind of message | speaker | form | example |
|---|---|---|---|
| instruction, field hint | nobody | imperative | Enter the 6-digit code |
| label, title, menu item | nobody | noun | Card number · Settings |
| status, result | nobody | past participle or fact | Saved · Sent to Maria |
| field error | nobody | imperative (the remedy) | Use at least 8 characters |
| system error | nobody, or actor | fact, then imperative | Your bank declined the card. Try another card. |
| promise of a later action | product | "we'll" + verb | We'll email you when it's ready |
| ownership | user | "my" | My orders |
| consent, preference | user | "me" | Send me a receipt |
| confirmation question | nobody | question with object | Delete 3 photos? |

## Tone without breeziness

White's reminder 9 bans the breezy manner; it does not ban warmth. The difference is where the warmth comes from.

Breeziness is the writer performing: "Oops!", "Yay!", "Hang tight!", jokes in errors, emoji, exclamation marks. It costs the user time and, at the moment of an error, trust (Apple HIG: skip "oops" and "uh-oh"). Mailchimp's voice guide says the same from the other side: clarity before entertainment, humor only if it comes naturally, otherwise straight-faced.

Warmth that survives the reminders comes from four things: using the user's own words for the task; stating the fact plainly and then the remedy, so the user is never left guessing; being specific where a vaguer product would hedge ("About 2 minutes", not "This may take a little while"); and not blaming. "Couldn't send. Check your connection and try again." is warm because it is useful.

Tone still varies by moment (Apple, Mailchimp): an error is calmer than a completed purchase, a destructive dialog is plainer than an onboarding title. The variation is in word choice and length, never in adding exclamation marks or adjectives.

## The voice statement

Three lines, written before the first string, kept with the terminology table:

1. **Who speaks by default.** Usually: nobody. The product says "we" only to promise a later action.
2. **Address.** "You" where a subject is needed; the imperative where it is not; one register throughout (bureau.ru 2022-03-06, on mixing ты and вы: in English the same failure is mixing "Hey there!" screens with "Please be advised" screens).
3. **Register.** Plain, specific, no slogans in the interface. Contractions allowed ("Couldn't", "We'll"); spelled-out forms only for emphasis.

Example, for an invented expense app: "Nobody speaks; 'we' only for promises. 'You' for subjects, imperative for instructions. Plain and specific; contractions on; no exclamation marks."

## Checks the linter runs for this file

`copy_check.py` flags "we're excited / thrilled / happy", "we think you'll love", reflexive "sorry", "oops" and its cousins, emoji, and double exclamation marks. It cannot tell "Send me a receipt" (right) from "Save your preferences" (right) on the same screen (wrong together); that is a review-workflow check against the decision table.
