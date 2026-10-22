# An approach to style: White's reminders, read for the interface

E. B. White's chapter V ("An Approach to Style") appears in the 1959 and later editions and is under copyright, so this file quotes nothing from it. The twenty-one reminders are listed by heading (headings are not protected) and glossed in this skill's words for interface text. Where a reminder overlaps a Strunk rule, the gloss points to `composition.md` rather than repeating it.

White's framing, paraphrased: style is what a writer is, not a coat of paint; the reminders are not rules but cautions, and all of them bend to the ear. The interface reader has a sharper version of that ear, because they are not reading for pleasure and will leave at the first word that wastes their time.

## 1. Place yourself in the background

The product is not the topic; the user's task is. Copy that says "We've redesigned", "We're excited", "We worked hard" moves the product into the foreground. Status copy says what is true for the user: "Sent", "3 unread", "Saved to Drafts". A product speaks in the first person only when it is the actor and the user needs to know it ("We'll email you a receipt"). Apology belongs here too: "Sorry" from a product that did nothing wrong is the product asking for attention.

## 2. Write in a way that comes naturally

Use the words the user would use to describe the task to a friend, in the order they would say them. If the team calls it "the ingestion pipeline" and the user calls it "importing", the screen says importing. A quick test: read the string aloud as if answering a question at a help desk.

## 3. Work from a suitable design

The same point as the 4th edition's rule 12 (`composition.md`, end): decide the pattern for each kind of message before writing the first one, and hold to it. Errors always: fact, then remedy. Confirmations always: question with its object, then the two answers in the same form. Empty states always: what this is, then the one action that fills it.

## 4. Write with nouns and verbs

The strength of a string is in its noun and its verb, not in its adjectives and adverbs. "Pay $12" has one of each and needs nothing else. "Quickly and securely complete your payment" has two adverbs doing the work the verb should do. A button is a verb and, when the object is not obvious, its noun.

## 5. Revise and rewrite

The write workflow in SKILL.md is this reminder as a procedure: write the whole message first, then cut. A string that survived one pass is not finished; read it in its element, on the screen, with the control beside it.

## 6. Do not overwrite

Overwriting on screen is the explanatory sentence after the one that already explained, the second adjective, the "In other words". If the first sentence told the user what to do, stop.

## 7. Do not overstate

"Awesome!", "You're all set!", "Amazing", "Perfect": each one spends the product's credibility on a routine event. When the user saves a file, "Saved" is the whole truth. Overstatement also appears as fake precision ("lightning fast", "bank-grade") and as superlatives in empty states. The 4th edition's note on this reminder is the one to remember: a single overstatement and the reader distrusts the rest.

## 8. Avoid the use of qualifiers

"Rather", "very", "little", "pretty", "quite", "somewhat", "a bit": White's list, and all of them in interface copy are either a hedge ("This may take a little while") or padding. State the number ("About 2 minutes") or say nothing.

## 9. Do not affect a breezy manner

The reminder most often broken by modern product copy. "Oops!", "Whoops, something broke", "Uh oh", emoji in an error, jokes in a loading state: breeziness is the writer performing ease at the user's expense, and the user hit the error. The fact and the remedy, in a plain voice, are what a person in difficulty wants from a product. Warmth is allowed; it comes from being useful and from using the user's words, not from exclamation marks.

## 10. Use orthodox spelling

One spelling convention across the product (US or UK), one spelling for each product term, no "thru", "lite", "nite", no invented compounds ("ReadyToShip"). Case conventions are part of this: sentence case or title case for titles, chosen once.

## 11. Do not explain too much

The screen already shows most of what prose would explain. A tooltip that restates the label ("Save: saves the document") explains the obvious. "Simply", "just", "easily" are the markers of over-explanation (`lexicon.md`, part 2). A link to a help page replaces three sentences of inline help; a well-named control replaces the tooltip.

## 12. Do not construct awkward adverbs

"Seamlessly", "effortlessly", "intuitively", "securely", "automagically": the adverb coined to carry a marketing claim. Cut it and state the fact that would justify it, if one exists.

## 13. Make sure the reader knows who is speaking

The interface has three possible speakers: the product ("we"), the user ("I", "my"), and nobody (the imperative and the plain fact). Decide once per product which one speaks in which kind of message and never mix them in one screen. A common failure: a checkbox labelled "Send me updates" (user speaks) next to a button "Save your preferences" (product speaks to user). `voice.md` sets this out.

## 14. Avoid fancy words

"Utilize", "leverage", "commence", "facilitate", "endeavor", "initiate", "terminate": each has a plain twin (use, use, start, help, try, start, end). Technical terms the user already knows are not fancy; "API key" is right for a developer and wrong for a shopper.

## 15. Do not use dialect unless your ear is good

Slang and regionalisms age fast and translate badly. "Y'all", "no worries", "sorted", "gonna" in product copy read as a costume to most of the audience.

## 16. Be clear

White's own summary of the chapter, and the test that outranks every other reminder: when clarity and any other rule conflict, clarity wins. If a short, positive, active sentence is ambiguous, write the longer one.

## 17. Do not inject opinion

"We think you'll love this", "Our favorite feature", "The best way to": the product's opinion is not information. Recommend with a reason or not at all ("Recommended: covers most households").

## 18. Use figures of speech sparingly

Metaphor in an interface becomes a term the user has to learn: "the vault", "your garden", "magic link". One metaphor can hold a product together; three compete. A metaphor in an error ("Houston, we have a problem") is breeziness (reminder 9) wearing a figure of speech.

## 19. Do not take shortcuts at the cost of clarity

Abbreviations, truncation with an ellipsis, icons without labels, "etc.": each saves space by moving work to the reader. When space forces a cut, cut words by rule 13, not letters.

## 20. Avoid foreign languages

"Voilà", "et cetera", "per se", "vis-à-vis", "ad hoc": decoration in English copy, and a hazard for localization. Technical loanwords the user already knows (menu, cache) are English now.

## 21. Prefer the standard to the offbeat

Product copy that strains to be different ("Make it rain" on a Pay button, "Yeet" on Delete) is remembered for the wrong reason. The standard token for the standard action is the right one unless the product has a strong reason, decided once, to be otherwise.
