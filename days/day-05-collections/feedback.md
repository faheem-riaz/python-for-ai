# Day 5 — Feedback

**Score: 8/8 ✔** Every check passes, and the two hardest exercises (6 and 8) are correct on the first read.

## What went well

- **Exercise 8:** a clean tokenizer: `sorted(set(...))` for the vocabulary, `index` to encode, a second loop to decode. That's the whole idea behind real tokenizers.
- **Exercise 7:** `set(test_words) - vocabulary` and `vocabulary & set(test_words)` are exactly the right operators.
- **Exercise 4:** converting once into `float_value` and reusing it.
- **Naming:** `model_name`, `model_accuracy`, `decoded_words`. Much clearer than Day 4's `fl` and `st`.

## Worth fixing

- **Exercise 2:** you replaced "tokenise" with `del pipeline[2]` followed by `pipeline.insert(2, "tokenize")`. It works, but it moves every later item twice. Lists are mutable, so one assignment does it: `pipeline[2] = "tokenize"`.

## Style

- **Exercise 8:** `sentence.lower().split()` is written twice. Store it once (`words = sentence.lower().split()`) and build `vocab` from `words`.
- `for index in token_ids` works, but `index` is also a list method name; `token_id` says more.

## Tip

Today's lesson turns your Exercise 8 loops into one-liners, and replaces `vocab.index(word)` with a dictionary lookup that doesn't search the list each time.
