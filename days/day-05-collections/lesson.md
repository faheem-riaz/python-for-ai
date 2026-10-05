# Day 5 — Collections: lists, tuples and sets

**Time:** about 35 minutes to read, 25 minutes for the exercises.

## What you'll learn

- Storing many values in one variable with a **list**
- Reading, slicing and changing lists, and the methods you'll use daily (`append`, `pop`, `sort` and friends)
- Why `b = a` does not copy a list
- Grouping a fixed set of values in a **tuple**, and unpacking it
- Keeping only unique values in a **set**, and comparing sets with `|`, `&` and `-`
- Choosing the right container for the job

So far every variable has held one value. Real data comes in bulk: thousands of sentences, a loss for every epoch, a label for every image. Today you get the containers that hold it. You've already met one in passing: `split()` has been handing you lists since Day 2.

---

## Part 1 — Lists

### Creating a list

A list is an ordered collection of items, written in square brackets with commas between the items:

```python
losses = [0.9, 0.5, 0.3]
models = ["gpt", "bert", "llama"]
empty = []

print(losses)        # [0.9, 0.5, 0.3]
print(len(models))   # 3
print(len(empty))    # 0
```

It's Python's version of Dart's `List`. A list can mix types (`["gpt", 4, True]` is legal), but in practice you'll almost always keep one kind of thing in a list.

`list()` turns other sequences into a list, which is a handy way to *see* what `range` or `zip` produce:

```python
print(list("GPT"))            # ['G', 'P', 'T']
print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(0, 10, 5)))  # [0, 5]
```

### Indexing and slicing

Everything you learned about string positions on Day 2 works on lists, unchanged:

```python
layers = [784, 256, 128, 64, 10]

print(layers[0])     # 784               first item
print(layers[-1])    # 10                last item
print(layers[1:4])   # [256, 128, 64]    positions 1, 2, 3
print(layers[:2])    # [784, 256]        the first two
print(layers[-2:])   # [64, 10]          the last two
print(layers[::-1])  # [10, 64, 128, 256, 784]   reversed
```

Indexing gives you **one item**; slicing gives you a **new list**. Asking for a position that doesn't exist is an error:

```python
print(layers[5])   # IndexError: list index out of range
```

Slicing is how a dataset is divided into a training part and a test part:

```python
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
split_at = int(len(data) * 0.8)   # 8

train = data[:split_at]
test = data[split_at:]

print(train)   # [10, 20, 30, 40, 50, 60, 70, 80]
print(test)    # [90, 100]
```

### Lists can be changed

Here lists and strings part ways. A string can't be changed (Day 2); a list can. The word for this is **mutable**.

```python
models = ["gpt", "bert", "llama"]
models[1] = "t5"

print(models)   # ['gpt', 't5', 'llama']
```

### Adding items

```python
steps = ["load", "train"]

steps.append("evaluate")        # add one item at the end
print(steps)                    # ['load', 'train', 'evaluate']

steps.insert(1, "clean")        # put an item at position 1; the rest move right
print(steps)                    # ['load', 'clean', 'train', 'evaluate']

steps.extend(["save", "deploy"])   # add every item of another list
print(steps)                    # ['load', 'clean', 'train', 'evaluate', 'save', 'deploy']
```

`append` is the one you'll use constantly. Be careful not to mix up `append` and `extend`: `steps.append(["save", "deploy"])` would add **one** item, which is itself a list.

`+` joins two lists into a new one, and `*` repeats a list:

```python
print([1, 2] + [3, 4])   # [1, 2, 3, 4]
print([0] * 5)           # [0, 0, 0, 0, 0]
```

### Removing items

```python
tokens = ["the", "cat", "<pad>", "sat", "<pad>"]

tokens.remove("<pad>")    # removes the FIRST matching item
print(tokens)             # ['the', 'cat', 'sat', '<pad>']

last = tokens.pop()       # removes the last item and gives it back to you
print(last)               # <pad>
print(tokens)             # ['the', 'cat', 'sat']

first = tokens.pop(0)     # pop can take a position
print(first)              # the
print(tokens)             # ['cat', 'sat']

del tokens[0]             # delete by position, without getting the item back
print(tokens)             # ['sat']

tokens.clear()            # remove everything
print(tokens)             # []
```

`remove` raises a `ValueError` if the item isn't in the list, so check first when you aren't sure.

### Asking questions about a list

`in` and `not in` (Day 3) work on lists. `count` and `index` are methods:

```python
labels = ["cat", "dog", "cat", "bird", "cat"]

print("dog" in labels)        # True
print("fish" not in labels)   # True
print(labels.count("cat"))    # 3     how many times it appears
print(labels.index("bird"))   # 3     position of the first match
```

Like `remove`, `index` raises a `ValueError` when the item is missing.

For lists of numbers, three built-in functions do the work you did with accumulator loops yesterday:

```python
losses = [0.9, 0.5, 0.3, 0.4]

print(min(losses))                 # 0.3
print(max(losses))                 # 0.9
print(sum(losses))                 # 2.1
print(sum(losses) / len(losses))   # 0.525   the average
```

### Sorting

There are two ways to sort, and the difference matters:

```python
scores = [0.72, 0.91, 0.65]

ranked = sorted(scores)   # gives you a NEW sorted list
print(ranked)             # [0.65, 0.72, 0.91]
print(scores)             # [0.72, 0.91, 0.65]   the original is untouched

scores.sort()             # sorts the list itself, in place
print(scores)             # [0.65, 0.72, 0.91]
```

Both accept `reverse=True` for largest-first:

```python
print(sorted(scores, reverse=True))   # [0.91, 0.72, 0.65]
```

The classic mistake is `scores = scores.sort()`. Methods that change a list in place (`sort`, `append`, `reverse`, `extend`...) return `None`, so that line throws your list away and leaves `scores` as `None`. Either call `scores.sort()` on its own line, or write `scores = sorted(scores)`.

Strings sort alphabetically, with all capital letters before all lower-case ones:

```python
print(sorted(["llama", "GPT", "bert"]))   # ['GPT', 'bert', 'llama']
```

### Looping and building lists

A `for` loop goes through a list one item at a time, and everything from yesterday (`enumerate`, `zip`, `break`, `continue`) works with it:

```python
models = ["gpt", "bert", "llama"]

for position, model in enumerate(models, start=1):
    print(position, model)
```

```text
1 gpt
2 bert
3 llama
```

The accumulator pattern now has a new form: **start with an empty list and `append` to it**. This is how you transform or filter data:

```python
raw = "0.91 0.45 0.78".split()   # ['0.91', '0.45', '0.78']  strings!
scores = []

for text in raw:
    scores.append(float(text))

print(scores)   # [0.91, 0.45, 0.78]
```

```python
confident = []

for score in scores:
    if score >= 0.5:
        confident.append(score)

print(confident)   # [0.91, 0.78]
```

And `join` (Day 2) goes the other way, from a list of strings back to one string:

```python
print(" > ".join(["load", "train", "evaluate"]))   # load > train > evaluate
```

### Lists inside lists

A list item can be another list. A list of rows is how you represent a table, an image, or a batch of data:

```python
image = [
    [0, 255, 0],
    [255, 255, 255],
    [0, 255, 0],
]

print(image[1])      # [255, 255, 255]   the second row
print(image[0][1])   # 255               first row, second column
print(len(image))    # 3                 number of rows
```

`image[0][1]` reads left to right: take row 0, then item 1 of that row. From Day 15, NumPy arrays will do this job much faster, but the idea is the same.

### Two names, one list

This catches everyone once. Assigning a list to another variable does **not** copy it. Both names refer to the same list:

```python
a = [1, 2, 3]
b = a          # b is another name for the SAME list

b.append(4)

print(a)   # [1, 2, 3, 4]   a changed too!
print(b)   # [1, 2, 3, 4]
```

When you want an independent copy, ask for one:

```python
a = [1, 2, 3]
b = a.copy()   # a new list with the same items  (a[:] does the same)

b.append(4)

print(a)   # [1, 2, 3]
print(b)   # [1, 2, 3, 4]
```

Dart lists behave the same way, so this may already feel familiar.

---

## Part 2 — Tuples

### A list that can't change

A tuple is written with round brackets. Like a list it's ordered, and you can index, slice and loop over it. Unlike a list, it is **immutable**: once created, it can't be changed.

```python
shape = (224, 224, 3)   # height, width, colour channels

print(shape[0])     # 224
print(len(shape))   # 3
print(shape[:2])    # (224, 224)
```

```python
shape[0] = 512   # TypeError: 'tuple' object does not support item assignment
```

There's no `append`, `remove` or `sort` either. That's the point: a tuple says "these values belong together and won't change". Use one for a fixed group where each **position** has a meaning: an image size, a coordinate, a (name, score) pair. It's close to a Dart record like `(String, double)`.

The commas make the tuple, not the brackets. That has one odd consequence: a tuple with a single item needs a trailing comma.

```python
one = (5,)
not_a_tuple = (5)

print(type(one))           # <class 'tuple'>
print(type(not_a_tuple))   # <class 'int'>
```

### Unpacking

You can assign the items of a tuple to several variables in one line:

```python
shape = (224, 224, 3)
height, width, channels = shape

print(height)     # 224
print(channels)   # 3
```

The number of variables must match the number of items, otherwise you get a `ValueError`. Unpacking works with lists too, but it's most natural with tuples.

It also gives Python its neat way to swap two variables, with no temporary variable:

```python
train_loss = 0.8
val_loss = 0.2

train_loss, val_loss = val_loss, train_loss

print(train_loss, val_loss)   # 0.2 0.8
```

### You've been using tuples already

Yesterday's `for i, word in enumerate(words)` was unpacking. `enumerate` and `zip` produce tuples, and the two loop variables unpack each one:

```python
names = ["gpt", "bert"]
scores = [0.91, 0.88]

print(list(zip(names, scores)))   # [('gpt', 0.91), ('bert', 0.88)]
print(list(enumerate(names)))     # [(0, 'gpt'), (1, 'bert')]
```

A **list of tuples** is a very common shape for data: each tuple is one record, and the list holds all the records.

```python
results = [("gpt", 0.91), ("bert", 0.88), ("llama", 0.93)]

for name, score in results:
    print(f"{name:<6} {score:.0%}")
```

```text
gpt    91%
bert   88%
llama  93%
```

---

## Part 3 — Sets

### Only unique items

A set is written with curly brackets. It keeps **one copy** of each item and throws duplicates away:

```python
labels = {"cat", "dog", "cat", "bird", "dog"}

print(len(labels))      # 3
print(sorted(labels))   # ['bird', 'cat', 'dog']
```

A set has **no order**. You can't write `labels[0]`, and if you print a set of strings directly, the order can differ from one run to the next. When you need a stable order, use `sorted(...)`, which gives you a list.

The most common use is `set(...)` on a list, to remove its duplicates. In language models, the set of distinct words in your text is called the **vocabulary**:

```python
words = "the cat sat on the mat".split()
vocabulary = set(words)

print(len(words))           # 6
print(len(vocabulary))      # 5     "the" is only counted once
print(sorted(vocabulary))   # ['cat', 'mat', 'on', 'sat', 'the']
```

### Changing and checking a set

```python
seen = set()        # an empty set

seen.add("cat")
seen.add("dog")
seen.add("cat")     # already there: nothing happens

print(len(seen))         # 2
print("dog" in seen)     # True

seen.discard("dog")      # remove it if present
seen.discard("fish")     # not there: no error
print(seen)              # {'cat'}
```

An empty set must be written `set()`. Empty curly brackets `{}` create an empty *dictionary*, which is tomorrow's topic.

`in` works on lists and sets alike, but on a set it is far faster: Python jumps straight to the answer instead of checking the items one by one. With ten items you'll never notice. With a million, it's the difference between instant and painfully slow.

### Combining sets

Sets can be compared with each other, just like in maths:

```python
train_words = {"cat", "dog", "bird"}
test_words = {"dog", "fish"}

print(sorted(train_words | test_words))   # ['bird', 'cat', 'dog', 'fish']   union: in either
print(sorted(train_words & test_words))   # ['dog']                          intersection: in both
print(sorted(train_words - test_words))   # ['bird', 'cat']                  difference: in the first only
print(sorted(test_words - train_words))   # ['fish']
```

The last line answers a real question: *which words in the test data did the model never see during training?*

---

## Which one should I use?

| | List | Tuple | Set |
| --- | --- | --- | --- |
| Written as | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` |
| Empty | `[]` | `()` | `set()` |
| Keeps order | yes | yes | no |
| Can change | yes | no | yes |
| Duplicates | allowed | allowed | removed |
| Indexing `x[0]` | yes | yes | no |

- Reach for a **list** by default: an ordered collection you'll loop over, add to or sort.
- Use a **tuple** for a small fixed group of related values, such as a shape or a (name, score) pair.
- Use a **set** when you care about uniqueness or fast "is it in here?" checks.

You can convert between them at any time with `list(...)`, `tuple(...)` and `set(...)`.

---

## Putting it together

A small data-preparation script: remove duplicate examples, then split what's left into training and test data. Save it as `prepare.py` and try other data:

```python
examples = [
    ("great film", "positive"),
    ("boring plot", "negative"),
    ("great film", "positive"),      # a duplicate
    ("loved the cast", "positive"),
    ("too long", "negative"),
    ("boring plot", "negative"),     # another duplicate
    ("a masterpiece", "positive"),
]

seen = set()
unique = []

for text, label in examples:
    if text in seen:
        continue
    seen.add(text)
    unique.append((text, label))

split_at = int(len(unique) * 0.8)
train = unique[:split_at]
test = unique[split_at:]

labels = []
for text, label in train:
    labels.append(label)

print(f"{len(examples)} examples, {len(unique)} unique")
print(f"train: {len(train)}, test: {len(test)}")
print(f"positive in train: {labels.count('positive')}")
print(f"test set: {test}")
```

```text
7 examples, 5 unique
train: 4, test: 1
positive in train: 2
test set: [('a masterpiece', 'positive')]
```

All three containers are at work: a **list** of **tuples** holds the dataset, and a **set** remembers which texts have been seen. `set(examples)` would also remove the duplicates, but it would lose the order; the `seen` pattern keeps it.

## Recap

- A **list** `[a, b, c]` is ordered and mutable. Index and slice it exactly like a string.
- Add with `append`, `insert`, `extend`; remove with `remove`, `pop`, `del`; ask with `in`, `count`, `index`.
- `len`, `min`, `max` and `sum` work on lists; the average is `sum(x) / len(x)`.
- `sorted(x)` returns a new list; `x.sort()` changes `x` in place and returns `None`.
- Build a list with the accumulator pattern: start with `[]` and `append` inside a loop.
- `b = a` gives the same list a second name. Use `a.copy()` for an independent copy.
- A **tuple** `(a, b, c)` is ordered and immutable. Unpack it with `x, y, z = my_tuple`; swap with `a, b = b, a`.
- A **set** `{a, b, c}` is unordered and holds unique items. `set(my_list)` removes duplicates; `|`, `&` and `-` combine sets. An empty set is `set()`.

## Your exercises

Open `exercises.py`, replace each `...` with your answer, and run:

```bash
cd days/day-05-collections
python3 exercises.py
```

Several exercises need more than one line where the `...` is. Each ✘ comes with a hint. When everything shows ✔, compare your answers with `solutions.py`.

**Tomorrow:** dictionaries and comprehensions: looking values up by name, and building collections in a single line.
