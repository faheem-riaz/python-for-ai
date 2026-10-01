# Day 2 — Feedback

**Score: 8/8 ✔** after a few rounds of fixes. That's the normal way to work: run, read the ✘, fix, run again.

## What went well

- `//` and `%` (exercises 1 and 3) were right first time, and so were `round(accuracy * 100, 1)` and the chained `raw_prompt.strip().lower()`.
- `filename[-8:-4]` and `filename[:-4]` count from the end, so they still work if the start of the filename changes. Your first try (`filename[15:19]`) was one position off, which is the most common slicing mistake. Counting from 0 takes practice.

## What the fixes taught you

- **`print` shows a value; `=` stores it.** `log_line = print(...)` stored `None`, because `print` returns nothing. This mix-up will come back when you write functions on Day 7, where `return` and `print` behave the same way.
- **`split()` first.** `"-".join(review)` joined every *character*; `"-".join(review.split())` joins words. `review.count("the")` found one `"the"`: it counts matching text, not words, and it's case-sensitive.
- **Exact strings are exact.** One extra space failed exercise 7. Checks (and tests on Day 14) compare character by character.

## Style

`( tokens / 1000000 )` is usually written `(tokens / 1_000_000)`: no spaces inside brackets, and underscores make the zeros easy to count.

## Tip

When a check fails, print the value to see what you actually have: `print(repr(log_line))`. `repr` adds quotes, so extra spaces and `None` show up straight away.
