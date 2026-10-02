# Day 4 — Loops

**Time:** about 35 minutes to read, 25 minutes for the exercises.

## What you'll learn

- Repeating code while a condition is true with `while`
- Walking through a sequence with `for`
- Counting with `range` (start, stop and step)
- The accumulator pattern: building up a total, a count or a string
- Getting positions with `enumerate` and pairing sequences with `zip`
- Leaving a loop early with `break` and skipping a round with `continue`

Yesterday your programs learned to choose. Today they learn to repeat. Almost everything in AI is a loop: training runs for many epochs, each epoch goes through many batches, and an LLM produces its answer one token at a time.

---

## Part 1 — `while`

### Repeat while a condition is true

A `while` loop looks like an `if`, but when the block finishes, Python goes back up and checks the condition again:

```python
loss = 1.0
epoch = 0

while loss > 0.3:
    epoch += 1
    loss = loss / 2
    print(f"epoch {epoch}: loss {loss}")

print("Training finished")
```

```text
epoch 1: loss 0.5
epoch 2: loss 0.25
Training finished
```

The rules are the same as for `if`: a **colon** at the end of the line, and an **indented** block. Step by step:

1. `1.0 > 0.3` is true, so the block runs. `loss` becomes `0.5`.
2. `0.5 > 0.3` is true, so the block runs again. `loss` becomes `0.25`.
3. `0.25 > 0.3` is false. Python skips the block and carries on below it.

If the condition is false the very first time, the block never runs at all.

### Infinite loops

Something inside the block must eventually make the condition false. If nothing does, the loop runs forever:

```python
count = 0
while count < 3:
    print(count)    # forgot count += 1, so count stays 0 for ever
```

This prints `0` endlessly. When it happens to you (it will), press **Ctrl+C** in the terminal to stop the program.

Python has no `count++` like Dart. Write `count += 1`.

### When to use `while`

Use `while` when you **don't know in advance** how many rounds you need: "keep going until the loss is low enough", "keep asking until the answer is valid". When you do know, or when you're going through a collection of things, `for` is the better tool.

---

## Part 2 — `for` and `range`

### `for` walks through a sequence

A `for` loop takes the items of a sequence one at a time and runs the block once for each:

```python
for letter in "GPT":
    print(letter)
```

```text
G
P
T
```

`letter` is the **loop variable**. You choose its name; Python gives it the next item at the start of each round. It works like Dart's `for (final letter in letters)`.

Strings give you one character at a time. The list you get from `split()` (Day 2) gives you one piece at a time:

```python
prompt = "explain neural networks simply"

for word in prompt.split():
    print(word, len(word))
```

```text
explain 7
neural 6
networks 8
simply 6
```

### `range`: counting

To repeat something a fixed number of times, loop over `range`:

```python
for i in range(3):
    print(f"round {i}")
```

```text
round 0
round 1
round 2
```

`range(3)` produces `0, 1, 2`: three numbers, starting at 0, and **3 itself is not included**. It's the same "up to but not including" rule as slicing.

`range` takes up to three arguments, exactly like a slice's `start:stop:step`:

| Call | Produces |
| --- | --- |
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(10, 0, -3)` | 10, 7, 4, 1 |

A typical training loop counts epochs from 1, so the stop value is one more than the last epoch you want:

```python
epochs = 3

for epoch in range(1, epochs + 1):
    print(f"Epoch {epoch}/{epochs}")
```

```text
Epoch 1/3
Epoch 2/3
Epoch 3/3
```

`range` only works with whole numbers: `range(0.5)` is a `TypeError`.

If you don't need the loop variable, the convention is to call it `_`:

```python
for _ in range(3):
    print("retrying...")
```

### The accumulator pattern

A loop on its own just repeats. To get a *result* out of it, create a variable **before** the loop and update it **inside** the loop. This is the pattern you'll write most often.

A running total:

```python
total = 0

for number in range(1, 6):
    total += number

print(total)   # 15   (1 + 2 + 3 + 4 + 5)
```

Counting things that match a condition (a loop with an `if` inside):

```python
text = "attention is all you need"
spaces = 0

for character in text:
    if character == " ":
        spaces += 1

print(spaces)   # 4
```

Building a string:

```python
shout = ""

for word in "stop the training".split():
    shout += word.upper() + "! "

print(shout)           # STOP! THE! TRAINING! 
print(shout.strip())   # STOP! THE! TRAINING!
```

The first version ends with a space, because every round adds one. `strip()` removes it.

Tracking the best value seen so far:

```python
scores = "0.61 0.84 0.79".split()
best = 0.0

for raw_score in scores:
    score = float(raw_score)   # split() gives strings, so convert first
    if score > best:
        best = score

print(best)   # 0.84
```

Watch the indentation in these examples. The line that sets up the variable (`total = 0`) must be **outside** the loop; put it inside and it's reset on every round. The final `print` is also outside, so it runs once, at the end.

### Loops inside loops

A loop's block can contain another loop. The inner loop runs completely for each round of the outer one:

```python
for epoch in range(1, 3):
    for batch in range(1, 4):
        print(f"epoch {epoch}, batch {batch}")
```

```text
epoch 1, batch 1
epoch 1, batch 2
epoch 1, batch 3
epoch 2, batch 1
epoch 2, batch 2
epoch 2, batch 3
```

Two epochs times three batches gives six rounds. This is the real shape of a training loop, which you'll write on Day 33.

---

## Part 3 — `enumerate` and `zip`

### `enumerate`: the item *and* its position

Sometimes you need to know where you are in the sequence. Coming from other languages, you might reach for an index:

```python
words = "tokens go in".split()

for i in range(len(words)):
    print(i, words[i])
```

That works, but Python has a cleaner way. `enumerate` hands you the position and the item together:

```python
for i, word in enumerate(words):
    print(i, word)
```

```text
0 tokens
1 go
2 in
```

Notice the **two** loop variables separated by a comma: the first receives the position, the second the item.

Positions start at 0. To count from 1 instead, pass `start=1`:

```python
for epoch, loss in enumerate("0.9 0.5 0.3".split(), start=1):
    print(f"epoch {epoch}: loss {loss}")
```

```text
epoch 1: loss 0.9
epoch 2: loss 0.5
epoch 3: loss 0.3
```

### `zip`: two sequences side by side

`zip` pairs up the items of two sequences: first with first, second with second, and so on (like the teeth of a zip).

```python
predictions = "cat dog cat".split()
answers = "cat dog bird".split()

for predicted, actual in zip(predictions, answers):
    print(predicted, actual, predicted == actual)
```

```text
cat cat True
dog dog True
cat bird False
```

Comparing a model's predictions with the right answers, pair by pair, is exactly how accuracy is calculated. You'll do it in the exercises.

If one sequence is longer, `zip` stops at the end of the shorter one and ignores the rest:

```python
for letter, digit in zip("abc", "12"):
    print(letter, digit)
```

```text
a 1
b 2
```

---

## Part 4 — `break` and `continue`

### `break`: leave the loop now

`break` ends the loop immediately. Python jumps to the first line after the loop:

```python
for token in "The cat sat <end> ignore this".split():
    if token == "<end>":
        break
    print(token)

print("Done")
```

```text
The
cat
sat
Done
```

This is how an LLM stops writing: it keeps producing tokens until it produces a special "end" token.

`break` also gives you a second way to write a `while` loop: loop "forever" and break out when you're done. It's the standard pattern for asking until the input is valid:

```python
while True:
    answer = input("Batch size: ").strip()
    if answer.isdigit():
        break
    print("Please type a whole number.")

batch_size = int(answer)
print(f"Using batch size {batch_size}")
```

```text
Batch size: lots
Please type a whole number.
Batch size: 32
Using batch size 32
```

### `continue`: skip to the next round

`continue` skips the rest of the block for **this** round and moves on to the next item:

```python
for word in "the model and the data".split():
    if word == "the" or word == "and":
        continue
    print(word)
```

```text
model
data
```

Use it to get unwanted items out of the way at the top of the block, so the rest of the block isn't nested inside an `if`.

In nested loops, `break` and `continue` only affect the **innermost** loop they're in.

---

## Putting it together

A simulated training run with **early stopping**: stop when the loss is good enough, even if there are epochs left. Save it as `train.py` and try other values:

```python
max_epochs = 10
target_loss = 0.2
loss = 1.0
epochs_run = 0

for epoch in range(1, max_epochs + 1):
    loss = round(loss * 0.6, 3)   # pretend the model improves by 40% each epoch
    epochs_run = epoch
    print(f"Epoch {epoch:>2}: loss {loss:.3f}")

    if loss <= target_loss:
        print("Target reached, stopping early")
        break

print(f"Ran {epochs_run} of {max_epochs} epochs, final loss {loss}")
```

```text
Epoch  1: loss 0.600
Epoch  2: loss 0.360
Epoch  3: loss 0.216
Epoch  4: loss 0.130
Target reached, stopping early
Ran 4 of 10 epochs, final loss 0.13
```

Everything from today is here: `range` counts the epochs, `loss` and `epochs_run` are accumulators, and `break` ends the run early.

## Recap

- `while condition:` repeats its block as long as the condition is true. Make sure something in the block changes the condition; Ctrl+C stops a runaway loop.
- `for item in sequence:` runs its block once per item: characters of a string, pieces from `split()`, numbers from `range`.
- `range(stop)`, `range(start, stop)`, `range(start, stop, step)`: the stop value is never included.
- Accumulator pattern: set up a variable before the loop, update it inside, use it after.
- `enumerate(sequence, start=1)` gives position and item together; `zip(a, b)` gives matching pairs and stops at the shorter one.
- `break` leaves the loop; `continue` skips to the next round. Both act on the innermost loop.
- Use `for` when you know what you're looping over, `while` when you only know when to stop.

## Your exercises

Open `exercises.py`, replace each `...` with your answer, and run:

```bash
cd days/day-04-loops
python3 exercises.py
```

Most exercises need a loop of several lines where the `...` is. Each ✘ comes with a hint. When everything shows ✔, compare your answers with `solutions.py`.

**Tomorrow:** collections: lists, tuples and sets, the containers that hold your data.
