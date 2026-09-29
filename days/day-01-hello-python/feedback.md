# Day 1 — Feedback

**Score: 6/6 ✔** A clean first day. Every answer is correct.

## What went well

- `seconds_per_day = 60*60*24` lets Python do the maths, which is exactly the point of the exercise. Anyone reading it can see where 86400 comes from.
- `intro = "My name is " + my_name` reuses the variable instead of typing your name again. That habit pays off: change `my_name` once and everything built from it follows.
- `epochs = epochs + 1` is the update pattern you'll use in every training loop later on.

## One style note

Python's style guide (PEP 8) puts spaces around most operators, so the usual way to write these is:

```python
seconds_per_day = 60 * 60 * 24
tokens_estimate = len(sentence) / 4
```

Both versions run the same way. The spaced version is just easier to read, and it's what you'll see in most Python code.

## Tip

`tokens_estimate` came out as `7.25`, a `float`, because `/` always returns a float. Tomorrow you'll meet `//` and `round()`, two ways to turn that into a whole number of tokens.
