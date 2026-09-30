# Day 1 — Hello, Python

**Time:** about 20 minutes to read, 15 minutes for the exercises.

## What you'll learn

- Why Python is the language of AI
- Two ways to run Python code
- `print`, comments, values and variables
- How to read an error message without panicking

## Why Python for AI?

Almost every AI tool you've heard of can be used from Python: PyTorch and TensorFlow for deep learning, scikit-learn for classic machine learning, pandas and NumPy for data, and the official SDKs for LLM APIs like Claude. Python itself is slow at heavy maths, but those libraries do the heavy lifting in fast compiled code, and Python is the friendly language you use to drive them. Learn Python well and the whole AI ecosystem opens up.

## Running Python

You already have Python 3 on your Mac. Open **Terminal** and check:

```bash
python3 --version
```

There are two ways to run code.

**1. The interactive shell (REPL).** Type `python3` and press Enter. You'll see `>>>`. Type an expression and Python answers immediately:

```python
>>> 2 + 3
5
>>> "AI" * 3
'AIAIAI'
```

Type `exit()` (or press Ctrl+D) to leave. The REPL is great for quick experiments.

**2. A script file.** Save code in a file ending in `.py` and run the whole file:

```bash
python3 hello.py
```

Real programs live in files. That's how you'll do the exercises.

## Your first program: `print`

`print` shows something on the screen:

```python
print("Hello, AI!")
print(42)
print("The answer is", 42)
```

Output:

```text
Hello, AI!
42
The answer is 42
```

Notice that `print` can take several values separated by commas; it puts a space between them.

## Comments

Anything after `#` on a line is a **comment**. Python ignores it; it's for humans.

```python
# This line is ignored.
print("This runs")  # So is this part of the line.
```

Write comments to explain *why* you did something, not to repeat what the code obviously does.

## Values and their types

Every piece of data in Python is a **value**, and every value has a **type**. Today you'll meet three:

| Type | Example | What it is |
| --- | --- | --- |
| `str` | `"Hello"` or `'Hello'` | text (a *string*) |
| `int` | `42`, `-7` | a whole number |
| `float` | `3.14`, `0.5` | a number with a decimal point |

You can ask Python for a value's type:

```python
>>> type("Hello")
<class 'str'>
>>> type(42)
<class 'int'>
>>> type(3.14)
<class 'float'>
```

## Variables: giving values a name

A **variable** is a name that points to a value. You create one with `=`:

```python
model_name = "Claude"
layers = 12
learning_rate = 0.001

print(model_name)      # Claude
print(layers * 2)      # 24
```

Rules and habits for names:

- Letters, digits and underscores only, and they can't start with a digit (`layer2` is fine, `2layer` isn't).
- Names are case-sensitive: `Score` and `score` are different variables.
- Python style uses lowercase words joined by underscores: `learning_rate`, not `LearningRate`.

You can change what a variable points to at any time:

```python
epochs = 5
epochs = epochs + 1
print(epochs)  # 6
```

`epochs = epochs + 1` reads as "take the current value of `epochs`, add 1, and store the result back in `epochs`".

## A few operations to play with

```python
print(7 + 3)      # 10   addition
print(7 - 3)      # 4    subtraction
print(7 * 3)      # 21   multiplication
print(7 / 2)      # 3.5  division always gives a float
print(2 ** 10)    # 1024 power

print("data" + "set")   # dataset  (joining strings is called concatenation)
print("ha" * 3)         # hahaha
print(len("tokens"))    # 6        len() counts characters
```

You'll go deeper into numbers and strings tomorrow.

## Reading error messages

Errors are normal. Every programmer sees dozens a day. The trick is to read them from the **bottom up**.

```python
print(modle_name)
```

```text
Traceback (most recent call last):
  File "hello.py", line 1, in <module>
    print(modle_name)
          ^^^^^^^^^^
NameError: name 'modle_name' is not defined. Did you mean: 'model_name'?
```

- The **last line** tells you what went wrong: a `NameError`, because `modle_name` is a typo.
- The lines above tell you **where**: file `hello.py`, line 1.
- Python even suggests the fix.

Two errors you'll meet a lot at first:

- `NameError`: you used a name that doesn't exist yet (typo, or used before it was created).
- `SyntaxError`: the code isn't valid Python, such as a missing quote or bracket: `print("hi)`.

## Recap

- Python runs in the REPL (`python3`) or from a file (`python3 file.py`).
- `print(...)` shows values; `#` starts a comment.
- Values have types: `str`, `int`, `float`.
- `name = value` creates or updates a variable.
- Read errors from the bottom line up.

## Your exercises

Open `exercises.py`, replace each `...` with your answer, and run:

```bash
cd days/day-01-hello-python
python3 exercises.py
```

Each ✘ comes with a hint. When everything shows ✔, compare your answers with `solutions.py`.

**Tomorrow:** numbers and strings in depth: integer vs float maths, rounding, the two operators every programmer uses daily (`//` and `%`), slicing text and f-strings.
