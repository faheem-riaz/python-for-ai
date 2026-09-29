# Day 2 — Numbers and Strings

**Time:** about 35 minutes to read, 25 minutes for the exercises.

## What you'll learn

- How `int` and `float` behave, and why `0.1 + 0.2` isn't exactly `0.3`
- Every arithmetic operator, including `//` (floor division) and `%` (remainder)
- Rounding with `round`, and shortcuts like `+=`
- Indexing and slicing strings
- The string methods you'll use constantly: `strip`, `lower`, `replace`, `split` and friends
- f-strings: the modern way to put values inside text

Almost everything in AI boils down to numbers (weights, losses, probabilities) and text (prompts, documents, labels). Today you get comfortable with both.

---

## Part 1 — Numbers

### `int` and `float`

You met both types yesterday. An `int` is a whole number; a `float` has a decimal point.

```python
epochs = 10          # int
learning_rate = 0.01 # float
print(type(epochs), type(learning_rate))
```

```text
<class 'int'> <class 'float'>
```

When you mix them, the result is a `float`:

```python
print(3 + 1.5)   # 4.5
print(2 * 1.0)   # 2.0
```

Python ints have **no size limit**. Try `2 ** 200` in the REPL: you get the exact 61-digit answer.

Two handy ways to write big and small numbers:

```python
parameters = 7_000_000_000   # underscores are ignored; they just help you read
print(parameters)            # 7000000000

learning_rate = 3e-4         # scientific notation: 3 × 10⁻⁴
print(learning_rate)         # 0.0003
```

Scientific notation always gives a `float`, even for whole numbers: `1e3` is `1000.0`.

### The arithmetic operators

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `+` | add | `7 + 2` | `9` |
| `-` | subtract | `7 - 2` | `5` |
| `*` | multiply | `7 * 2` | `14` |
| `/` | divide | `7 / 2` | `3.5` |
| `//` | floor division | `7 // 2` | `3` |
| `%` | remainder (modulo) | `7 % 2` | `1` |
| `**` | power | `7 ** 2` | `49` |

`/` **always** returns a float, even when the division is exact: `10 / 5` is `2.0`.

### `//` and `%`: the pair you'll use every day

`//` divides and throws away the fractional part (it rounds *down*). `%` gives you what's left over.

Think of splitting a dataset into batches:

```python
examples = 1000
batch_size = 64

full_batches = examples // batch_size
leftover = examples % batch_size

print(full_batches)  # 15
print(leftover)      # 40
```

15 full batches of 64 is 960 examples, with 40 left over for a smaller final batch. In general, `(a // b) * b + a % b == a`.

`%` is also how you check "every Nth time", and how you convert units:

```python
total_seconds = 3725
minutes = total_seconds // 60   # 62
seconds = total_seconds % 60    # 5
print(minutes, "min", seconds, "s")
```

```text
62 min 5 s
```

A number is even when `n % 2` is `0`; you'll use that trick with `if` tomorrow.

> **Careful with negatives.** `//` rounds *down*, towards minus infinity, not towards zero: `-7 // 2` is `-4`, and `-7 % 2` is `1`. You won't need this often, but it explains a surprising result if you ever see one.

### Order of operations

Python follows the usual maths rules: `**` first, then `*`, `/`, `//`, `%`, then `+` and `-`. Use brackets to be explicit:

```python
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20
print(-2 ** 2)       # -4   (the power happens before the minus sign)
print((-2) ** 2)     # 4
```

When in doubt, add brackets. They cost nothing and make your intent obvious.

### Floats are close, not exact

```python
print(0.1 + 0.2)
```

```text
0.30000000000000004
```

This isn't a Python bug. Computers store floats in binary, and most decimal fractions (like 0.1) can't be written exactly in binary, just as 1/3 can't be written exactly in decimal. Every language that uses standard floats (Dart included) prints the same thing.

The practical rules:

- Floats are perfect for maths and ML, where tiny errors don't matter.
- Don't check floats for *exact* equality. Round them first, or check they're close.
- For real billing code, where every cent must add up exactly, programmers use other tools (such as Python's `decimal` module) instead of floats.

### `round`

`round(x)` rounds to the nearest whole number; `round(x, n)` keeps `n` decimal places:

```python
loss = 0.4567891
print(round(loss, 3))   # 0.457
print(round(loss))      # 0
print(round(7.25))      # 7
```

One surprise: exact halves round to the nearest **even** number. This is called banker's rounding, and it avoids always nudging results upwards:

```python
print(round(2.5))   # 2
print(round(3.5))   # 4
```

### Other built-ins for numbers

```python
print(abs(-3.2))          # 3.2    distance from zero
print(min(0.8, 0.3, 0.5)) # 0.3    smallest
print(max(0.8, 0.3, 0.5)) # 0.8    largest
```

### Shortcut assignment: `+=` and friends

Yesterday you wrote `epochs = epochs + 1`. Python has a shorter form:

```python
step = 0
step += 1        # same as step = step + 1
step += 1
print(step)      # 2

loss = 2.0
loss *= 0.5      # same as loss = loss * 0.5
print(loss)      # 1.0
```

The same works with `-=`, `/=`, `//=`, `%=` and `**=`. You'll see `+=` in almost every loop you write.

---

## Part 2 — Strings

A string is a sequence of characters. Single and double quotes are equivalent: pick one style and stick to it. If the text contains one kind of quote, wrap it in the other:

```python
answer = "It's a transformer"
```

For text over several lines, use triple quotes. You'll use these for long prompts:

```python
prompt = """You are a helpful assistant.
Answer in one sentence."""
print(prompt)
```

```text
You are a helpful assistant.
Answer in one sentence.
```

Inside a string, `\n` means "new line" and `\t` means "tab".

### Indexing: one character at a time

Each character has a position, its **index**, starting at **0**:

```text
 m   o   d   e   l
 0   1   2   3   4
-5  -4  -3  -2  -1
```

```python
word = "model"
print(word[0])    # m
print(word[4])    # l
print(word[-1])   # l   negative indexes count from the end
print(word[-2])   # e
```

`word[-1]` is the idiomatic way to get the last character, whatever the length.

Asking for an index that doesn't exist is an error:

```python
word[10]
```

```text
IndexError: string index out of range
```

### Slicing: a piece of a string

`text[start:stop]` gives the characters from `start` up to, **but not including**, `stop`:

```python
filename = "report_2026.csv"

print(filename[0:6])    # report
print(filename[:6])     # report   missing start means "from the beginning"
print(filename[7:11])   # 2026
print(filename[-3:])    # csv      missing stop means "to the end"
print(filename[:-4])    # report_2026   everything except the last 4 characters
```

A tip for the "not including" rule: `stop - start` is the length of the slice. `filename[7:11]` has 4 characters.

A third number sets the **step**:

```python
digits = "0123456789"
print(digits[::2])    # 02468   every second character
print(digits[::-1])   # 9876543210   a negative step walks backwards
```

Unlike indexing, slicing never raises an error: `"abc"[1:100]` just gives `"bc"`.

### Strings can't be changed

Strings are **immutable**: once created, they never change.

```python
word = "model"
word[0] = "M"
```

```text
TypeError: 'str' object does not support item assignment
```

Instead, you build a new string and point the variable at it:

```python
word = "M" + word[1:]
print(word)   # Model
```

### String methods

A **method** is a function that belongs to a value. You call it with a dot: `value.method()`. Because strings are immutable, string methods never change the original; they **return a new string**.

```python
title = "  Attention Is All You Need  "

print(title.strip())    # "Attention Is All You Need"   removes spaces at both ends
print(title.lower())    # "  attention is all you need  "
print(title.upper())    # "  ATTENTION IS ALL YOU NEED  "
print(title)            # unchanged: "  Attention Is All You Need  "
```

The `print` calls above show the text without the quotes; the quotes in the comments are there only so you can see the spaces.

You can **chain** methods, because each one returns a string:

```python
clean = title.strip().lower()
print(clean)    # attention is all you need
```

Cleaning text like this (trimming, lowercasing) is one of the first steps in almost every NLP pipeline.

More methods you'll reach for often:

```python
sentence = "the cat sat on the mat"

print(sentence.replace("cat", "dog"))   # the dog sat on the mat
print(sentence.count("at"))             # 3
print(sentence.find("sat"))             # 8    index where it starts (-1 if missing)
print(sentence.title())                 # The Cat Sat On The Mat
print(sentence.startswith("the"))       # True
print(sentence.endswith("."))           # False
print("sat" in sentence)                # True
```

`True` and `False` are **booleans**, the answers to yes/no questions. They're tomorrow's topic.

### `split` and `join`

`split()` breaks a string into pieces. With no argument, it splits on any whitespace:

```python
words = sentence.split()
print(words)        # ['the', 'cat', 'sat', 'on', 'the', 'mat']
print(len(words))   # 6
```

The result is a **list**, a collection you'll study properly on Day 5. For now, know that `len` counts its items.

Pass a separator to split on something else:

```python
row = "alice,0.92,passed"
print(row.split(","))   # ['alice', '0.92', 'passed']
```

`join` goes the other way. It's called on the *separator* and glues the pieces together:

```python
print("-".join(words))   # the-cat-sat-on-the-mat
```

Splitting text into words is a (very) simplified version of **tokenisation**, the first thing an LLM does with your prompt. Real tokenisers split into sub-word pieces, but the idea is the same.

---

## Part 3 — f-strings

Try to join text and a number with `+`:

```python
epoch = 3
print("Epoch " + epoch)
```

```text
TypeError: can only concatenate str (not "int") to str
```

`+` only joins strings to strings. The clean solution is an **f-string**: put `f` before the opening quote, and write any variable or expression inside `{}`:

```python
epoch = 3
loss = 0.4567891
print(f"Epoch {epoch}: loss {loss}")
print(f"Next epoch is {epoch + 1}")
```

```text
Epoch 3: loss 0.4567891
Next epoch is 4
```

If you know Dart, this is `'Epoch $epoch'` and `'${epoch + 1}'`, with `{}` instead of `$`.

### Formatting numbers

After the value, add `:` and a **format spec** to control how it looks:

```python
loss = 0.4567891
accuracy = 0.9234
tokens = 1234567

print(f"{loss:.3f}")       # 0.457        3 decimal places
print(f"{accuracy:.1%}")   # 92.3%        as a percentage, 1 decimal place
print(f"{tokens:,}")       # 1,234,567    thousands separators
print(f"{tokens:,.2f}")    # 1,234,567.00 both together
```

`.3f` means "fixed-point, 3 decimals". It changes only how the number is *shown*; the variable keeps its full value.

You can also line things up in columns: `<` aligns left, `>` right, and the number is the width:

```python
print(f"{'model':<8}|{'score':>6}")
print(f"{'small':<8}|{0.81:>6.2f}")
print(f"{'large':<8}|{0.9:>6.2f}")
```

```text
model   | score
small   |  0.81
large   |  0.90
```

Notice the single quotes inside the double-quoted f-string, so Python doesn't think the string has ended.

### The debugging trick: `=`

Add `=` after an expression and the f-string prints the expression *and* its value:

```python
batch_size = 32
print(f"{batch_size=}")
print(f"{batch_size * 4=}")
```

```text
batch_size=32
batch_size * 4=128
```

This is a quick way to inspect values while you're working something out.

---

## Putting it together

A small training-log line, using everything from today:

```python
run_name = "  Sentiment-Classifier "
total_steps = 2500
batch_size = 64
correct = 1837
seen = 2000
seconds = 754

name = run_name.strip().lower()
batches = total_steps // batch_size
accuracy = correct / seen
minutes = seconds // 60
secs = seconds % 60

print(f"[{name}] {batches} full batches | acc {accuracy:.1%} | {minutes}m {secs}s")
```

```text
[sentiment-classifier] 39 full batches | acc 91.8% | 12m 34s
```

## Recap

- `int` is a whole number, `float` has a decimal point; mixing them gives a `float`.
- `/` always returns a float. `//` rounds down and `%` gives the remainder.
- Floats are approximations: `0.1 + 0.2` isn't exactly `0.3`. Round before comparing.
- `round(x, n)` rounds to `n` places; exact halves go to the nearest even number.
- `x += 1` is short for `x = x + 1`.
- Strings are indexed from 0; `s[-1]` is the last character.
- `s[start:stop:step]` slices; `stop` is not included.
- Strings are immutable, so methods like `strip`, `lower` and `replace` return new strings.
- `split` breaks text into a list of pieces; `sep.join(pieces)` glues them back.
- f-strings put values into text: `f"{loss:.3f}"`, `f"{acc:.1%}"`, `f"{n:,}"`, `f"{x=}"`.

## Your exercises

Open `exercises.py`, replace each `...` with your answer, and run:

```bash
cd days/day-02-numbers-and-strings
python3 exercises.py
```

Each ✘ comes with a hint. When everything shows ✔, compare your answers with `solutions.py`.

**Tomorrow:** input and decisions: reading what the user types, converting between types, booleans and comparisons, and making your programs choose with `if`, `elif` and `else`.
