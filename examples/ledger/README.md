# Ledger: a strings file, before and after

An invented expense-tracking app. `before.en.json` is the kind of file the audit workflow receives; `after.en.json` is the same keys rewritten by the rules in `../../skills/strunk`. `check-before.txt` and `check-after.txt` are the linter's output on each. The rewrite also produced the terminology table and voice statement below, which is what the workflow delivers alongside the strings.

Rule ids are the 1918 numbers (see `references/composition.md`); V.n is White's reminder n.

## What changed, by rule

| key | before | after | rule |
|---|---|---|---|
| auth.title | Welcome Back! | Sign in | V.7, 12; the title names the screen |
| auth.subtitle | Please log in to continue to your account | (removed) | 13; the title said it |
| auth.email_label | Please enter your e-mail address | Email | 13; labels are nouns |
| auth.password_error | Password is not long enough | Use at least 8 characters | 11 |
| auth.email_error | Invalid email | Enter an email like name@example.com | 11, 12 |
| auth.cta | Submit | Sign in | 12; the button names the result |
| auth.forgot | Click here if you forgot your password | Forgot password | 12, 13 |
| auth.signup_link | Don't have an account? Register here | Create account | 13, 4th.12 (one term) |
| auth.generic_error | Oops! Something went wrong. Please try again later. | Couldn't sign in. Check your connection and try again. | V.9, 12, 13 |
| home.empty | There are currently no expenses in your list. Why not add one? | No expenses yet. | 10, 13, V.9; the Add button is the action |
| home.sync_status | Your data has been successfully synced! | Synced | 13, V.7 |
| home.sync_error | Sync could not be completed at this time due to a network error. | Couldn't sync: no connection. Your edits are saved on this phone and will sync when you're back online. | 10, 13, 12; the consequence the user needs |
| expense.delete_* | Are you sure? / OK / Cancel | Delete this expense? €42.50 at Lidl, 14 Mar. / Delete expense / Keep expense | 12, 15 |
| expense.amount_hint | Please enter the amount in order to continue | Amount | 13 |
| expense.category_tooltip | Category: select the category for this expense. | Groups this expense in reports and budgets. | V.11; the tooltip adds what the label lacks |
| expense.receipt_error | We're sorry, but we were unable to upload your receipt. The file might be too large. | Couldn't upload receipt.jpg: it's 14 MB and the limit is 10 MB. Choose a smaller photo. | V.1, 10, 12, 11 |
| settings.notify | Enable the notification feature | Notify me about new expenses | 13, V.14; describes the on state |
| settings.notify_only | Only notify me about large expenses | Notify me only about expenses over €100 | 16, 12 |
| settings.export, download_csv | Export / Download your data | Download as CSV (both) | 4th.12; one word, naming the outcome |
| settings.signout | Log Out | Sign out | 4th.12, V.10 |
| settings.delete_account_body | We're really sad to see you go 😢 Are you sure you want to proceed? | Deletes your 312 expenses and 4 budgets from all devices. This can't be undone. | V.1, V.9, V.8, 12 |
| onboarding.s1_* | Welcome to Ledger! We're thrilled... powerful, intuitive... easily and effortlessly | See where your money goes. Connect a bank and Ledger sorts each payment... | V.1, V.7, V.12, 13 |
| onboarding.s2–s4 | Step 1: Connecting your bank / Step 2: You set a budget / Step 3: Track! | Connect a bank / Set a budget / Track spending | 15 |
| onboarding.cta | Let's Go! | Connect a bank | V.9, 12 |
| push.budget_warn | Heads up! You have spent a very large portion... | Groceries: €380 of €400 spent, 9 days left | V.8, 12, front-loaded |
| push.renewal | Reminder: Don't forget that your subscription will renew soon. | Renews Sat 19 Feb, €4.99 | 11, 12, 13 |

## Terminology table

| thing | the word | not |
|---|---|---|
| entering the account | sign in | log in, login |
| creating an account | create account | register, sign up |
| leaving the account | sign out | log out |
| removing an expense or the account for good | delete | remove |
| getting the data out | download as CSV | export |
| one recorded payment | expense | item, entry, transaction |

## Voice statement

Nobody speaks; "we" never (the sync error says "your edits are saved", not "we saved"). "You/your" for subjects, imperative for instructions, "me" on consent checkboxes. Plain and specific; contractions on; no exclamation marks; sentence case; no end period on one-line strings.
