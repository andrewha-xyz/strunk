# Composition: Strunk's rules, read for the interface

Primary source: William Strunk Jr., *The Elements of Style* (1918), public domain, Project Gutenberg #37134. Rule numbers below are the 1918 numbers. The 4th edition (Strunk & White, 2000) opens the chapter with a new rule 12, "Choose a suitable design and hold to it," folds the 1918 topic-sentence rule (9) into its paragraph rule (13), and then numbers the rest by adding four: 1918 rule 10 is 4th-edition rule 14, and so on through rule 18 (22). Quotations are from the 1918 text. The interface gloss after each rule is this skill's, not the book's.

| 1918 | 4th ed. | rule |
|---|---|---|
| (none) | 12 | choose a suitable design and hold to it |
| 8 | 13 | one paragraph to each topic |
| 9 | (in 13) | begin with a topic sentence |
| 10 | 14 | use the active voice |
| 11 | 15 | put statements in positive form |
| 12 | 16 | use definite, specific, concrete language |
| 13 | 17 | omit needless words |
| 14 | 18 | avoid a succession of loose sentences |
| 15 | 19 | express co-ordinate ideas in similar form |
| 16 | 20 | keep related words together |
| 17 | 21 | in summaries, keep to one tense |
| 18 | 22 | place the emphatic words of a sentence at the end |

(The 4th edition's rule 12 has no 1918 counterpart. It is the consistency rule and is treated at the end of this file.)

## Rule 8. Make the paragraph the unit of composition: one paragraph to each topic.

Strunk: "The object of treating each topic in a paragraph by itself is, of course, to aid the reader. The beginning of each paragraph is a signal to him that a new step in the development of the subject has been reached."

Interface gloss. The paragraph's job in prose is the message's job on screen: one message, one job. An error says what happened and what to do next; it does not also upsell, apologize twice, and link to the help center. A dialog asks one question. A screen carries one idea, and its title names it. When a message needs two paragraphs, it is usually two messages or a help page.

Strunk also says single sentences should not stand as paragraphs, with exceptions for "textbooks, guidebooks, and other works in which many topics are treated briefly." An interface is such a work: nearly every string is a one-sentence paragraph, and that is right.

## Rule 9. Begin each paragraph with a topic sentence, end it in conformity with the beginning.

Strunk: the reader should "discover the purpose of each paragraph as he begins to read it." "Ending with a digression, or with an unimportant detail, is particularly to be avoided."

Interface gloss. The first words of a title, a notification, or an error are its topic sentence; the reader decides from them whether to read on. "Payment declined" is a topic sentence; "We're sorry, but unfortunately" is not. The end of the message is the last thing the reader sees before acting, so it is the action, never a disclaimer or a link to something else.

## Rule 10. Use the active voice.

Strunk: "The active voice is usually more direct and vigorous than the passive." Of the passive without an agent ("My first visit to Boston will always be remembered") he says "it becomes indefinite: is it the writer, or some person undisclosed, or the world at large" that remembers. He also allows the passive "which is frequently convenient and sometimes necessary," when the thing acted upon is the topic.

Interface gloss. The passive hides the actor, and in an interface the actor is the whole story: did the user do it, did the product do it, or did a third party? "Payment could not be processed" hides who declined and leaves the user to guess whether to retry. "Your bank declined the card" names the actor and implies the remedy. Allowed passives: when the object is the topic and the actor is nobody in particular ("File deleted", "3 items selected"), because the user is the implicit actor and naming them adds nothing.

Strunk's second point under this rule is the verb buried in a noun: "A survey of this region was made in 1900" versus "This region was surveyed in 1900." In interface text the buried verb shows up as "Perform a sync", "Complete the verification process", "Make a selection": say "Sync", "Verify", "Choose one".

His third point is the expletive opener: "There were a great number of dead leaves lying on the ground" versus "Dead leaves covered the ground." "There are no items in your cart" is weaker than "Your cart is empty"; "There was a problem saving" is weaker than "Couldn't save".

## Rule 11. Put statements in positive form.

Strunk: "Make definite assertions. Avoid tame, colorless, hesitating, non-committal language. Use the word *not* as a means of denial or in antithesis, never as a means of evasion." And: "the reader is dissatisfied with being told only what is not; he wishes to be told what is."

Interface gloss. This is the rule for every instruction, validation message, and error. The user wants to know what to do, and a negative tells them only what went wrong. "Password is not long enough" becomes "Use at least 8 characters". "You cannot upload files larger than 10 MB" becomes "Choose a file under 10 MB". "Invalid date" becomes "Enter a date like 14 Mar 2026". Strunk's own pairs transfer directly: "did not remember" is "forgot"; "not important" is "trifling".

Two honest exceptions. First, antithesis is strong, and Strunk says so ("Not charity, but simple justice"): a confirmation can read "Delete the draft, not the published post". Second, some facts are negative and must be stated: "No internet connection" is the fact; the positive form is the remedy that follows it ("Connect to Wi-Fi to continue"). Say the fact in as few words as it takes, then say what to do.

## Rule 12. Use definite, specific, concrete language.

Strunk: "Prefer the specific to the general, the definite to the vague, the concrete to the abstract." His examples: "A period of unfavorable weather set in" versus "It rained every day for a week." He quotes Spencer: "we do not think in generals, but in particulars."

Interface gloss. Vagueness in an interface is "Something went wrong", "Are you sure?", "An error occurred", "Invalid input", "Item", "Changes". Each of these makes the user supply the particular from memory. The concrete version names the object and the number: "Delete 3 photos?", "Couldn't send to Maria", "Enter the 6-digit code from your authenticator app", "Saved to Drafts". When the product knows the particular (the file name, the count, the card's last four digits, the time), the message shows it.

Strunk's "all the significant details are given, and not vaguely" is the test for an error: does the user now know which thing, what state it is in, and what will happen if they act?

## Rule 13. Omit needless words.

Strunk: "Vigorous writing is concise. A sentence should contain no unnecessary words, a paragraph no unnecessary sentences, for the same reason that a drawing should have no unnecessary lines and a machine no unnecessary parts. This requires not that the writer make all his sentences short, or that he avoid all detail and treat his subjects only in outline, but that he make every word tell."

His list of expressions to cut, all still common in interface text:

| Strunk's example | shorter |
|---|---|
| the question as to whether | whether |
| there is no doubt but that | no doubt |
| used for fuel purposes | used for fuel |
| he is a man who | he |
| in a hasty manner | hastily |
| this is a subject which | this subject |
| His story is a strange one. | His story is strange. |
| owing to the fact that | since, because |
| in spite of the fact that | though |
| call your attention to the fact that | remind you |
| I was unaware of the fact that | I did not know |

"In especial the expression *the fact that* should be revised out of every sentence in which it occurs." He adds that *who is*, *which was* are often superfluous, and that "a single complex idea, step by step, in a series of sentences" should usually be one sentence.

Interface gloss. This is the rule the whole skill turns on, because a word on screen costs attention that the control next to it needs. The cut is a procedure, not a mood: write the complete message first (what happened, why, what to do), then remove every word whose removal does not change what the user will do next. Words that nearly always go: "please" in instructions, "successfully" after a verb that already succeeded ("Saved"), "currently", "in order to", "simply", "just", "easily", "you can", "note that", "please be aware that", "at this time", "it is recommended that". Words that stay: the object's name, the number, the actor when it is not the user, and the verb of the next action.

Strunk's caveat applies: the rule does not mean short, it means every word tells. "Delete" on a destructive button is too short when the question was "Delete 3 photos?"; "Delete 3 photos" tells.

## Rule 14. Avoid a succession of loose sentences.

Strunk: a series of two-clause sentences joined by *and*, *but*, *so*, *which* "soon becomes monotonous and tedious," with "mechanical symmetry and sing-song."

Interface gloss. Interface text rarely runs long enough for this to bite, but onboarding and help text do: "Tap the plus to add a note, and then you can tag it, and it will sync to your other devices" is three sentences wearing one coat. Give each step its own sentence, or a list.

## Rule 15. Express co-ordinate ideas in similar form.

Strunk: "expressions of similar content and function should be outwardly similar. The likeness of form enables the reader to recognize more readily the likeness of content and function." And of the writer who varies form for its own sake: "he seems unable or afraid to choose one form of expression and hold to it." Correlatives (*either ... or*, *first, second*) "should be followed by the same grammatical construction."

Interface gloss. Parallelism is the structural rule of menus, tabs, settings, lists of steps, and button pairs. Menu items are all verbs or all nouns ("Edit, Share, Delete", not "Edit, Sharing, Delete this"). Steps in onboarding start with the same part of speech. The buttons of a dialog answer its question in the same form: "Delete 3 photos?" is answered by "Delete" and "Keep", not by "OK" and "Cancel". Strunk's last paragraph under this rule is also a UI rule: when there are many similar ideas, "he had best avoid difficulty by putting his statements in the form of a table."

## Rule 16. Keep related words together.

Strunk: "The position of the words in a sentence is the principal means of showing their relationship." Modifiers "should come, if possible, next to the word they modify." His example: "He only found two mistakes" versus "He found only two mistakes."

Interface gloss. On screen the rule has a spatial half and a verbal half. Spatial: a label sits next to the control it names, a hint next to the field it hints, a count next to the thing counted, an error next to the field that caused it. Verbal: the thing the user acts on sits next to the action. "Changes to your notification preferences for this project will be saved" separates the verb from the user by eleven words; "Save notification settings for this project" keeps them together. Misplaced *only* is as common in settings copy as in prose: "Only notify me about mentions" means something different from "Notify me only about mentions".

## Rule 17. In summaries, keep to one tense.

Strunk: "Shifting from one tense to the other gives the appearance of uncertainty and irresolution."

Interface gloss. A product speaks in one tense per kind of message. Status and results are present or past-as-done ("Saved", "2 of 5 uploaded"); instructions are imperative ("Choose a plan"); futures are promised only when the product can keep them ("We'll email you when it's ready"). A screen that mixes "Your file has been uploaded", "Uploading complete", and "File will now upload" is three tenses for one event.

## Rule 18. Place the emphatic words of a sentence at the end.

Strunk: "The proper place in the sentence for the word, or group of words, which the writer desires to make most prominent is usually the end." The prominent element is "the logical predicate, that is, the *new* element in the sentence." He adds: "The other prominent position in the sentence is the beginning."

Interface gloss, and the one place this skill departs from the letter of the book. Strunk wrote for readers who read a sentence through. Interface text is scanned: readers take the first one or two words of a line and move on (see the secondary sources on reading on screen in SKILL.md). So for titles, labels, list items, and notifications the emphatic word goes first, the position Strunk calls the other prominent one. "Payment declined" not "Your payment was declined"; "3 new messages" not "You have 3 new messages"; "Wi-Fi off" not "Your connection to Wi-Fi is currently off". For a full sentence that the user will read through, such as the body of an error or a confirmation, the end still belongs to the action: "To keep your files, cancel; to remove them, delete."

## Choose a suitable design and hold to it (4th edition rule 12)

Not in the 1918 text; White's addition. Its sense is that a piece of writing has a shape chosen in advance and kept. In an interface the shape is the vocabulary and the patterns: one word for one thing across the product (sign in, not log in on one screen and login on another; delete, not remove and trash by turns), one structure for every error, one structure for every empty state, one case convention. The deliverable that carries this rule is the terminology table in `elements.md`; the check that enforces it is the collision report in `scripts/copy_check.py`.
