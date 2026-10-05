# Day 4 — Feedback

**Score: 8/8 ✔** All checks pass, and this time there's nothing hiding behind the ticks: the logic is right in every exercise.

## What went well

- **Exercise 7** is the hardest one and you got the order right: `STOP` first, then the `isdigit()` check, then the sum.
- **Exercise 6:** converting with `float(data)` once and reusing the result is cleaner than converting twice.
- **Exercise 8:** early stopping with `break`, and the report built after the loop, exactly as intended.
- You wrote `+= 1` everywhere. No `++` in sight.

## Worth fixing

- **Exercise 7:** the `else:` after `continue` isn't needed. `continue` already skips the rest of the round, so `token_total += int(st)` can sit at the loop's own indentation level. That is the whole benefit of `continue`: less nesting.

## Style

- Names: `fl`, `st`, `data` and `i` make the reader work. `loss`, `item`, `raw_loss` and `epoch` say what they hold.
- Spacing: Python's convention is `start=1` (no spaces around `=` in an argument) and `max_epochs + 1` (spaces around operators).

## Tip

When a loop variable *means* something, name it that: `for epoch in range(1, max_epochs + 1)`. Then `epochs_run = epoch` reads like a sentence.
