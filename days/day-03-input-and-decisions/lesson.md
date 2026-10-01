# Day 3 — Input and Decisions

**Time:** about 35 minutes to read, 25 minutes for the exercises.

## What you'll learn

- Reading what the user types with `input`
- Converting between types: `int()`, `float()`, `str()`, `bool()`
- Booleans, comparison operators and chained comparisons
- Combining conditions with `and`, `or` and `not`
- Making decisions with `if`, `elif` and `else`
- Truthiness: which values Python treats as "false"

Up to now your programs ran the same way every time. Today they start reacting: to what a user types, to a model's score, to whether an API key is set.

---

## Part 1 — Input and type conversion

### `input`

`input` pauses the program, waits for the user to type something and press Enter, and gives you back what they typed:

```python
name = input("What's your name? ")
print(f"Hello, {name}!")
```

Running it looks like this (the user typed `Faheem`):

```text
What's your name? Faheem
Hello, Faheem!
```

The text you pass to `input` is the **prompt**. End it with a space so the user's typing doesn't touch it.

### `input` always gives you a string

This is the most important thing about `input`: whatever the user types, you get a **`str`**. Even if they type `5`:

```python
epochs = input("How many epochs? ")   # user types 5
print(type(epochs))                   # <class 'str'>
print(epochs * 2)                     # 55   (string repetition, not maths!)
```

To do maths with it, you have to convert it first.

### Converting types

Each type's name doubles as a converter:

```python
print(int("5"))        # 5
print(float("0.001"))  # 0.001
print(float("3"))      # 3.0
print(str(42))         # 42   (now the text "42")
print(int(3.9))        # 3    int() cuts off the decimals; it doesn't round
print(round(3.9))      # 4    use round() if you want rounding
```

So the usual pattern is to convert straight away:

```python
epochs = int(input("How many epochs? "))
print(epochs * 2)    # 10 if the user typed 5
```

`int()` and `float()` ignore spaces at the ends, so `int(" 29 ")` is `29`. But they can't convert text that isn't a number:

```python
int("five")
```

```text
ValueError: invalid literal for int() with base 10: 'five'
```

Watch out for this one too: `int("3.5")` is *also* a `ValueError`, because `"3.5"` isn't a whole number. Use `float("3.5")` for that.

`str()` goes the other way. It's how you join numbers onto text with `+` (though an f-string is usually neater):

```python
steps = 500
print("Ran " + str(steps) + " steps")   # Ran 500 steps
print(f"Ran {steps} steps")             # same result
```

On Day 8 you'll learn to handle bad input properly with `try` / `except`. Today you'll use a simpler check: `str.isdigit()`, which you'll meet in a moment.

---

## Part 2 — Booleans and comparisons

### `True` and `False`

A **boolean** (`bool`) has only two values: `True` and `False`, with capital letters. Dart's `bool` is the same idea; just remember the capitals.

```python
is_training = True
print(type(is_training))   # <class 'bool'>
```

### Comparison operators

Comparisons ask a question and answer with a boolean:

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `==` | equal to | `3 == 3` | `True` |
| `!=` | not equal to | `3 != 3` | `False` |
| `<` | less than | `0.2 < 0.5` | `True` |
| `>` | greater than | `0.2 > 0.5` | `False` |
| `<=` | less than or equal to | `5 <= 5` | `True` |
| `>=` | greater than or equal to | `4 >= 5` | `False` |

Don't mix up `=` and `==`. One `=` **assigns** a value; two `==` **compares** values.

```python
loss = 0.42
target = 0.5
reached_target = loss <= target
print(reached_target)   # True
```

Comparisons work on strings too, but they're **case-sensitive**:

```python
print("yes" == "yes")   # True
print("Yes" == "yes")   # False
print("Yes".lower() == "yes")   # True   normalise first, then compare
```

A number and the same number written as text are **not** equal: `5 == "5"` is `False`. This is a classic bug with `input`, and one more reason to convert right away.

Remember from Day 2 that floats are approximations, so `0.1 + 0.2 == 0.3` is `False`. Compare rounded values instead: `round(0.1 + 0.2, 2) == 0.3` is `True`.

### Chained comparisons

Python lets you chain comparisons the way you would in maths:

```python
confidence = 0.87
print(0 <= confidence <= 1)   # True   "is confidence between 0 and 1?"
```

This means `0 <= confidence and confidence <= 1`. Most languages (Dart included) can't do this.

### `in` and handy string checks

You saw `in` on Day 2. It asks "does this contain that?":

```python
prompt = "Translate this into French"
print("French" in prompt)       # True
print("German" not in prompt)   # True
```

A few string methods answer yes/no questions, which makes them useful for checking input:

```python
print("2026".isdigit())     # True    only the digits 0-9
print("20.5".isdigit())     # False   the dot isn't a digit
print("-3".isdigit())       # False   neither is the minus sign
print("".isdigit())         # False   an empty string has no digits
print("hello".isalpha())    # True    only letters
```

### `and`, `or`, `not`

Combine booleans with plain English words (Dart uses `&&`, `||` and `!`):

- `a and b` is `True` only if **both** are true.
- `a or b` is `True` if **at least one** is true.
- `not a` flips `True` to `False` and back.

```python
has_api_key = True
tokens_used = 950
token_limit = 1000

can_call_api = has_api_key and tokens_used < token_limit
print(can_call_api)        # True
print(not can_call_api)    # False

is_flagged = False
low_confidence = 0.35 < 0.5
needs_review = is_flagged or low_confidence
print(needs_review)        # True
```

`not` is applied first, then `and`, then `or`. As with maths, add brackets when you combine them so nobody has to remember that.

Python also stops as soon as it knows the answer. In `a and b`, if `a` is `False`, Python never looks at `b`. This is called **short-circuiting**, and you'll use it to avoid errors: `text != "" and text[0] == "#"` is safe even for an empty string, because `text[0]` is never reached.

---

## Part 3 — Decisions with `if`

### `if`

```python
loss = 0.42

if loss < 0.5:
    print("Good enough to deploy")

print("Done")
```

```text
Good enough to deploy
Done
```

Three details matter:

- The line ends with a **colon** `:`.
- The code that belongs to the `if` is **indented** (4 spaces is the standard). There are no braces like in Dart: the indentation *is* the block.
- The block ends when the indentation goes back. `print("Done")` isn't indented, so it always runs.

Getting the indentation wrong is an error:

```python
if loss < 0.5:
print("Good enough")
```

```text
IndentationError: expected an indented block after 'if' statement on line 1
```

### `else`

`else` runs when the condition is false:

```python
score = 0.31

if score >= 0.5:
    label = "positive"
else:
    label = "negative"

print(label)   # negative
```

### `elif`

For more than two options, add `elif` ("else if") branches. Python checks them **from top to bottom** and runs only the **first** one that's true:

```python
accuracy = 0.84

if accuracy >= 0.9:
    grade = "excellent"
elif accuracy >= 0.75:
    grade = "good"
elif accuracy >= 0.5:
    grade = "fair"
else:
    grade = "poor"

print(grade)   # good
```

`0.84 >= 0.5` is also true, but Python never gets that far: it stopped at `"good"`. That's why you order the checks from the most specific (highest) to the least. Put `>= 0.5` first and every score above 0.5 would come out as `"fair"`.

You can have as many `elif`s as you like, and `else` is optional.

### Nesting

An `if` block can contain another `if`. Each level indents another 4 spaces:

```python
has_api_key = True
tokens_used = 1200
token_limit = 1000

if has_api_key:
    if tokens_used < token_limit:
        print("Calling the API")
    else:
        print("Token limit reached")
else:
    print("Set your API key first")
```

```text
Token limit reached
```

Deep nesting gets hard to read quickly. Often `and`, or an `elif`, gives a flatter version.

### The one-line version

For a simple either/or value, Python has a **conditional expression**, like Dart's `condition ? a : b` but written in words:

```python
score = 0.73
label = "positive" if score >= 0.5 else "negative"
print(label)   # positive
```

Use it for short choices like this one; use a full `if` / `else` for anything longer.

### Truthiness

An `if` doesn't need an actual boolean. Python treats some values as "false-ish" (**falsy**) and everything else as **truthy**. The falsy values you'll meet most are:

- `False`
- `0` and `0.0`
- `""` (an empty string)
- `None` (Python's "no value", like Dart's `null`)

`bool()` shows you how Python sees a value:

```python
print(bool(""))        # False
print(bool("hi"))      # True
print(bool(0))         # False
print(bool(0.001))     # True
print(bool(" "))       # True   a space is still a character!
```

So the idiomatic way to check "did the user type anything?" is:

```python
answer = ""   # imagine this came from input() and the user just pressed Enter

if answer.strip():
    print(f"You said: {answer}")
else:
    print("You didn't type anything")
```

```text
You didn't type anything
```

Note that `bool("False")` is `True`: it's a non-empty string. To turn text like `"yes"` into a boolean, compare it: `answer.strip().lower() == "yes"`.

---

## Putting it together

A small script that checks settings for an LLM call. Save it as `settings.py` and try it with different inputs:

```python
raw_temperature = input("Temperature (0-2): ").strip()

if raw_temperature == "":
    temperature = 1.0
    print("No value given, using the default of 1.0")
else:
    temperature = float(raw_temperature)

if temperature < 0 or temperature > 2.0:
    style = "out of range"
elif temperature <= 0.3:
    style = "focused and predictable"
elif temperature <= 1.0:
    style = "balanced"
else:
    style = "creative (and more random)"

print(f"Temperature {temperature}: {style}")
```

Ruling out invalid values first keeps the remaining checks simple: by the time Python reaches `elif temperature <= 0.3`, it already knows the value is between 0 and 2.

One run (the user typed `0.2`):

```text
Temperature (0-2): 0.2
Temperature 0.2: focused and predictable
```

**Temperature** is a real setting on LLM APIs: low values make the model pick the most likely words, high values make it more varied. You'll use it for real on Day 36.

## Recap

- `input(prompt)` waits for the user and **always returns a `str`**.
- Convert with `int()`, `float()`, `str()`. Converting text that isn't a number raises `ValueError`; `int(3.9)` cuts off to `3`.
- `True` and `False` are booleans. `==`, `!=`, `<`, `>`, `<=`, `>=` compare and return one.
- `=` assigns, `==` compares. `5 == "5"` is `False`.
- Chain comparisons like maths: `0 <= x <= 1`.
- `and`, `or`, `not` combine conditions; Python stops evaluating as soon as it knows the answer.
- `if` / `elif` / `else` end with `:` and use indentation for their blocks. Only the first true branch runs.
- `a if condition else b` picks between two values in one line.
- Falsy values: `False`, `0`, `0.0`, `""`, `None`. Everything else is truthy.

## Your exercises

Open `exercises.py`, replace each `...` with your answer, and run:

```bash
cd days/day-03-input-and-decisions
python3 exercises.py
```

The exercises don't call `input()` (the checker can't type for you). Instead, variables like `user_text` stand in for what a user would type. Each ✘ comes with a hint. When everything shows ✔, compare your answers with `solutions.py`.

**Tomorrow:** loops: repeating work with `while` and `for`, counting with `range`, pairing things up with `enumerate` and `zip`, and controlling loops with `break` and `continue`.
