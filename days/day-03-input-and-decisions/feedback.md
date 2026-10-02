# Day 3 — Feedback

**Score: 8/8 ✔** All checks pass. Three answers pass with today's values but would give the wrong result with others, so they're worth a second look.

## What went well

- Conversions, `str(epochs)` with `+`, and the `and` / `or` / `not` trio were all right.
- Your `grade` checks run from the highest threshold down, which is the whole trick of `elif`.
- The one-line `"positive" if sentiment >= 0.5 else "negative"` is a good use of a conditional expression.

## Worth fixing

- **Exercise 3:** `0 < confidence < 1` leaves out 0 and 1 themselves. "Inclusive" means `0 <= confidence <= 1`; a confidence of exactly `1.0` is valid.
- **Exercise 7:** `int(user_age_text.strip())` crashes with a `ValueError` if the user types `abc`. The task asked for an `isdigit()` check first, with `age = 0` otherwise.
- **Exercise 8:** try `raw_temperature = "-1"`. It comes out as `"balanced"`, because `-1 <= 1.0` is true. Rule out invalid values first, or write `0 <= temperature <= 1.0`.

## Style

- Python doesn't need brackets around a condition: `if accuracy >= 0.9:` rather than `if(accuracy >= 0.9):`. That's the Dart habit showing.
- `True if age >= 18 else False` is just `age >= 18`: the comparison already is a boolean.

## Tip

Passing checks only prove the values you tested. Change the input (`"abc"`, `"-1"`, `""`) and rerun to see how your code behaves at the edges.
