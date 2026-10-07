# Day 6 — Dictionaries and comprehensions

**Time:** about 35 minutes to read, 25 minutes for the exercises.

## What you'll learn

- Looking values up by name with a **dictionary**
- Reading safely with `get`, and adding, changing and removing pairs
- Looping over keys, values and both at once with `items()`
- The counting pattern, which is behind every word-frequency table
- Nesting: dictionaries inside lists, the shape of almost all real-world data
- Building lists, dictionaries and sets in one line with **comprehensions**

Yesterday's containers find things by *position* (lists, tuples) or just tell you whether something is *there* (sets). Today's finds things by *name*. Ask a list "what's at position 3?"; ask a dictionary "what's the learning rate?" or "what's the id of the word *cat*?".

---

## Part 1 — Dictionaries

### Creating a dictionary

A dictionary holds **key: value** pairs, written in curly brackets:

```python
config = {"model": "tiny-gpt", "learning_rate": 0.01, "epochs": 5}

print(config)        # {'model': 'tiny-gpt', 'learning_rate': 0.01, 'epochs': 5}
print(len(config))   # 3   three pairs
```

It's Python's version of Dart's `Map`. The type is called `dict`, and that's what everyone calls it. Longer dictionaries are usually written one pair per line:

```python
config = {
    "model": "tiny-gpt",
    "learning_rate": 0.01,
    "epochs": 5,
}
```

The comma after the last pair is optional, and it's a habit worth picking up: adding a line later doesn't touch the line above.

An empty dictionary is `{}`. That's why an empty *set* had to be written `set()` yesterday.

### Reading a value

Put the key in square brackets, where a list would take a position:

```python
config = {"model": "tiny-gpt", "learning_rate": 0.01, "epochs": 5}

print(config["model"])    # tiny-gpt
print(config["epochs"])   # 5
```

Asking for a key that isn't there is an error:

```python
print(config["batch_size"])   # KeyError: 'batch_size'
```

There are two ways to avoid that. `in` checks whether a **key** exists, and `get` reads a value but gives you a fallback when the key is missing:

```python
print("epochs" in config)             # True
print("batch_size" in config)         # False

print(config.get("epochs"))           # 5
print(config.get("batch_size"))       # None   no error
print(config.get("batch_size", 32))   # 32     your own default
```

Use `config["key"]` when the key *must* be there, so a typo fails loudly. Use `get` when a missing key is normal and you have a sensible default.

Note that `in` looks at keys only: `"tiny-gpt" in config` is `False`.

### Adding, changing and removing

Assigning to a key does both jobs. If the key exists, its value is replaced; if not, the pair is added:

```python
config = {"model": "tiny-gpt", "epochs": 5}

config["epochs"] = 10          # existing key: value replaced
config["batch_size"] = 32      # new key: pair added

print(config)   # {'model': 'tiny-gpt', 'epochs': 10, 'batch_size': 32}
```

So a key can appear only once. Keys are unique, like the items of a set; values can repeat freely.

`update` changes or adds several pairs at once, from another dictionary:

```python
config.update({"epochs": 20, "seed": 42})
print(config)   # {'model': 'tiny-gpt', 'epochs': 20, 'batch_size': 32, 'seed': 42}
```

To remove a pair, `pop` gives you the value back and `del` doesn't:

```python
seed = config.pop("seed")
print(seed)     # 42

del config["batch_size"]
print(config)   # {'model': 'tiny-gpt', 'epochs': 20}
```

Both raise a `KeyError` when the key is missing. `config.pop("seed", None)` removes the key if it's there and stays quiet if it isn't.

A dictionary remembers the order in which its pairs were added, as you can see in the outputs above. You still can't ask for "the second pair" with `config[1]`: that would look for a key equal to `1`.

### What can be a key?

Keys are usually strings, but numbers and tuples work as well:

```python
id_to_label = {0: "cat", 1: "dog", 2: "bird"}
print(id_to_label[1])    # dog

pixel_values = {(0, 0): 255, (0, 1): 128}
print(pixel_values[(0, 1)])   # 128
```

`id_to_label[1]` looks like list indexing, but it's a lookup of the key `1`.

The rule is that a key must be something that can't change. Strings, numbers and tuples qualify; a list doesn't:

```python
bad = {[0, 0]: 255}   # TypeError: unhashable type: 'list'
```

Values have no such rule. A value can be anything, including a list or another dictionary.

### Looping over a dictionary

A `for` loop over a dictionary gives you its **keys**:

```python
accuracies = {"gpt": 0.91, "bert": 0.88, "llama": 0.93}

for name in accuracies:
    print(name, accuracies[name])
```

```text
gpt 0.91
bert 0.88
llama 0.93
```

Usually you want the key and the value together. `items()` gives you (key, value) tuples, which you unpack in the loop exactly like yesterday's list of tuples:

```python
for name, accuracy in accuracies.items():
    print(f"{name:<6} {accuracy:.0%}")
```

```text
gpt    91%
bert   88%
llama  93%
```

This is the loop you'll write most often. There are three views in total, and `list()` lets you see them:

```python
print(list(accuracies.keys()))     # ['gpt', 'bert', 'llama']
print(list(accuracies.values()))   # [0.91, 0.88, 0.93]
print(list(accuracies.items()))    # [('gpt', 0.91), ('bert', 0.88), ('llama', 0.93)]
```

`values()` is handy with yesterday's built-in functions:

```python
print(max(accuracies.values()))                     # 0.93
print(sum(accuracies.values()) / len(accuracies))   # 0.9066666666666667
```

And because looping gives keys, so do `sorted` and `list`:

```python
print(sorted(accuracies))   # ['bert', 'gpt', 'llama']
```

### The counting pattern

This is the most useful thing a dictionary does. To count how often each item appears, keep a dictionary from item to count:

```python
labels = ["cat", "dog", "cat", "bird", "cat"]
counts = {}

for label in labels:
    if label in counts:
        counts[label] += 1
    else:
        counts[label] = 1

print(counts)   # {'cat': 3, 'dog': 1, 'bird': 1}
```

The first time a label shows up there's nothing to add to, hence the `if`. `get` with a default of `0` folds those four lines into one:

```python
counts = {}

for label in labels:
    counts[label] = counts.get(label, 0) + 1

print(counts)   # {'cat': 3, 'dog': 1, 'bird': 1}
```

Read it as "the count so far, or 0 if there isn't one yet, plus 1". It's the accumulator pattern again, with one running total per key. Counting words in text this way is the starting point of classic language processing (you'll meet it again as "bag of words" on Day 30).

### Building a dictionary from two lists

`zip` pairs items up, and `dict()` turns pairs into a dictionary:

```python
names = ["gpt", "bert", "llama"]
scores = [0.91, 0.88, 0.93]

accuracies = dict(zip(names, scores))
print(accuracies)   # {'gpt': 0.91, 'bert': 0.88, 'llama': 0.93}
```

### Dictionaries and lists, nested

A dictionary describes **one thing** by its named fields. A **list of dictionaries** describes many things, and it's the shape nearly all real data arrives in. A conversation with an LLM, for example, is sent as a list of messages like this:

```python
messages = [
    {"role": "system", "content": "You are a helpful tutor."},
    {"role": "user", "content": "What is a token?"},
    {"role": "assistant", "content": "A small piece of text."},
]

print(messages[1]["content"])   # What is a token?

for message in messages:
    print(f"{message['role']}: {message['content']}")
```

```text
What is a token?
system: You are a helpful tutor.
user: What is a token?
assistant: A small piece of text.
```

`messages[1]["content"]` reads left to right, like yesterday's `image[0][1]`: take item 1 of the list, then the value under `"content"`. Notice the single quotes for the keys inside the f-string. The f-string itself uses double quotes, so the keys use the other kind.

Values can be lists or dictionaries too:

```python
run = {
    "model": "tiny-gpt",
    "losses": [0.9, 0.5, 0.3],
    "optimizer": {"name": "adam", "learning_rate": 0.001},
}

print(run["losses"][-1])                   # 0.3
print(run["optimizer"]["learning_rate"])   # 0.001

run["losses"].append(0.25)
print(len(run["losses"]))                  # 4
```

If this looks like JSON to you, that's no accident: JSON maps onto Python dictionaries and lists almost one to one, which you'll use on Day 13.

One reminder from yesterday applies here too. `b = a` gives the same dictionary a second name; `a.copy()` makes a separate one.

---

## Part 2 — Comprehensions

### The pattern you keep writing

Yesterday you built lists like this:

```python
losses = [0.9, 0.5, 0.3]
percentages = []

for loss in losses:
    percentages.append(round(loss * 100))

print(percentages)   # [90, 50, 30]
```

Three lines to say "make a list of `round(loss * 100)` for every loss". A **list comprehension** says it in one:

```python
percentages = [round(loss * 100) for loss in losses]

print(percentages)   # [90, 50, 30]
```

The square brackets say "this makes a list". Inside, you write **what each item should be**, then the `for` that supplies the values:

```text
[ expression   for item in collection ]
  what to put  where the items come from
```

Dart has the same idea: `[for (var loss in losses) (loss * 100).round()]`. Python puts the expression first, the way you'd say it in English.

Any expression works, and so does anything you can loop over:

```python
raw = "0.91 0.45 0.78".split()

scores = [float(text) for text in raw]
print(scores)    # [0.91, 0.45, 0.78]

words = ["Tokens", "ARE", "small"]
print([word.lower() for word in words])   # ['tokens', 'are', 'small']
print([len(word) for word in words])      # [6, 3, 5]
print([n * n for n in range(5)])          # [0, 1, 4, 9, 16]
```

### Filtering with `if`

Add an `if` at the end to keep only some of the items:

```python
scores = [0.91, 0.45, 0.78, 0.30]

confident = [score for score in scores if score >= 0.5]
print(confident)   # [0.91, 0.78]
```

That replaces yesterday's loop with an `if` and an `append` inside it. You can transform and filter in the same comprehension:

```python
words = ["the", "tokenizer", "is", "fast"]

shouted = [word.upper() for word in words if len(word) > 3]
print(shouted)   # ['TOKENIZER', 'FAST']
```

### Choosing with `if` / `else`

A filter drops items. To keep every item but choose between two results, use Day 3's conditional expression as the expression at the **front**:

```python
scores = [0.91, 0.45, 0.78, 0.30]

labels = ["positive" if score >= 0.5 else "negative" for score in scores]
print(labels)   # ['positive', 'negative', 'positive', 'negative']
```

The position tells you which is which. An `if` at the end is a filter, and the result may be shorter. An `if ... else` at the front is a choice, and the result has the same length as the input.

### Comprehensions with `enumerate`, `zip` and `items`

Everything that works in a `for` loop works here, including unpacking:

```python
names = ["gpt", "bert", "llama"]
scores = [0.91, 0.88, 0.93]

print([f"{position}. {name}" for position, name in enumerate(names, start=1)])
# ['1. gpt', '2. bert', '3. llama']

print([name for name, score in zip(names, scores) if score > 0.9])
# ['gpt', 'llama']
```

### Dictionary comprehensions

Curly brackets with a `key: value` in front make a dictionary:

```python
words = ["cat", "tokenizer", "model"]

lengths = {word: len(word) for word in words}
print(lengths)   # {'cat': 3, 'tokenizer': 9, 'model': 5}
```

The most common use in AI code is giving every word or label a number. A model can't read `"cat"`; it needs an id:

```python
vocab = ["bird", "cat", "dog"]

word_to_id = {word: number for number, word in enumerate(vocab)}
print(word_to_id)          # {'bird': 0, 'cat': 1, 'dog': 2}
print(word_to_id["cat"])   # 1
```

Loop over `items()` to build a new dictionary from an old one. Swapping `key: value` round gives you the reverse lookup, from id back to word:

```python
id_to_word = {number: word for word, number in word_to_id.items()}
print(id_to_word)      # {0: 'bird', 1: 'cat', 2: 'dog'}
print(id_to_word[2])   # dog
```

Filtering works the same way as in a list comprehension:

```python
accuracies = {"gpt": 0.91, "bert": 0.88, "t5": 0.79}

strong = {name: accuracy for name, accuracy in accuracies.items() if accuracy >= 0.85}
print(strong)   # {'gpt': 0.91, 'bert': 0.88}
```

### Set comprehensions

Curly brackets with a single expression (no colon) make a set, so duplicates disappear:

```python
words = ["The", "cat", "and", "the", "CAT"]

unique = {word.lower() for word in words}
print(sorted(unique))   # ['and', 'cat', 'the']
```

The brackets tell you what you get: `[...]` a list, `{key: value ...}` a dictionary, `{item ...}` a set.

### Ranking a dictionary

A dictionary has no `sort` method, and `sorted(accuracies)` sorts the *keys*. To rank by *value*, there's a useful fact about tuples: they sort by their first item (and by the second when the first items are equal). So build (value, key) tuples and sort those:

```python
accuracies = {"gpt": 0.91, "bert": 0.88, "llama": 0.93}

pairs = sorted([(accuracy, name) for name, accuracy in accuracies.items()], reverse=True)
print(pairs)     # [(0.93, 'llama'), (0.91, 'gpt'), (0.88, 'bert')]

ranking = [name for accuracy, name in pairs]
print(ranking)   # ['llama', 'gpt', 'bert']
```

Tomorrow you'll learn a neater way that uses a function.

### When not to use one

A comprehension is for **building a collection**. If the line gets long or needs two conditions and a calculation, a normal loop is easier to read, and nobody will think less of you for writing one. And when you aren't collecting anything, such as a loop that only prints, use a plain `for`.

A good test: if you can read it aloud in one breath ("the length of each word in words"), it's a fine comprehension.

---

## Putting it together

A word-frequency script: count the words in some text, give every word an id, and encode the text as numbers. Save it as `frequencies.py` and try your own text:

```python
text = "the cat sat on the mat and the dog sat on the rug"
words = text.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

pairs = sorted([(count, word) for word, count in counts.items()], reverse=True)
repeated = [word for count, word in pairs if count > 1]

word_to_id = {word: number for number, word in enumerate(sorted(counts))}
token_ids = [word_to_id[word] for word in words]

print(f"{len(words)} words, {len(counts)} distinct")
print(f"used more than once: {repeated}")
for count, word in pairs[:3]:
    print(f"{word:<5} {count} {'#' * count}")
print(f"ids: {token_ids}")
```

```text
13 words, 8 distinct
used more than once: ['the', 'sat', 'on']
the   4 ####
sat   2 ##
on    2 ##
ids: [7, 1, 6, 4, 7, 3, 0, 7, 2, 6, 4, 7, 5]
```

Compare this with yesterday's tokenizer. There, `vocab.index(word)` searched the list from the start for every single word. Here, `word_to_id[word]` jumps straight to the answer, just as `in` does on a set. Real tokenizers keep their vocabulary in a dictionary for exactly this reason.

## Recap

- A **dictionary** `{"key": value}` looks values up by key. Keys are unique and must be unchangeable (strings, numbers, tuples); values can be anything.
- `d[key]` reads and raises `KeyError` if the key is missing; `d.get(key, default)` never raises. `key in d` checks the keys.
- `d[key] = value` adds or replaces. Remove with `d.pop(key)` or `del d[key]`.
- Loop with `for key, value in d.items()`. `d.keys()` and `d.values()` give you one side only.
- Count with `counts[item] = counts.get(item, 0) + 1`.
- A list of dictionaries is the standard shape for records: `messages[1]["content"]`.
- **List comprehension:** `[expression for item in collection if condition]`. The `if` at the end filters; `a if condition else b` at the front chooses.
- **Dictionary comprehension:** `{key: value for ...}`. **Set comprehension:** `{item for ...}`.
- Reverse a lookup with `{value: key for key, value in d.items()}`.

## Your exercises

Open `exercises.py`, replace each `...` with your answer, and run:

```bash
cd days/day-06-dictionaries-and-comprehensions
python3 exercises.py
```

Several exercises need more than one line where the `...` is. Each ✘ comes with a hint. When everything shows ✔, compare your answers with `solutions.py`.

**Tomorrow:** functions: giving a piece of code a name so you can reuse it, with parameters, return values, defaults and `lambda`.
