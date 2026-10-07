"""Day 6 exercises: Dictionaries and comprehensions.

Replace each `...` with your answer, then run:

    python3 exercises.py

Lines that start with # are instructions; you don't need to change them.
Some answers are several lines: write them where the `...` is.
"""

# 1. `config` holds the settings for a training run.
#    - Set `model_name` to the value stored under "model" (use square brackets).
#    - Set `batch_size` with `get`, using 32 as the default ("batch_size" isn't in the dictionary yet).
#    Then change `config` itself:
#    - set "learning_rate" to 0.001,
#    - add the key "batch_size" with the value 64,
#    - remove "debug".
#    Finally set `setting_count` to the number of pairs now in `config`.
config = {"model": "tiny-gpt", "learning_rate": 0.01, "epochs": 5, "debug": True}
model_name = ...
batch_size = ...
...
setting_count = ...

# 2. Counting. With a loop, fill `label_counts` so that each label maps to how often it appears in `labels`.
#    Then, with a second loop over `label_counts.items()`, set `most_common` to the label
#    that appears most often and `most_common_count` to its count.
labels = ["cat", "dog", "cat", "bird", "dog", "cat", "fish", "cat"]
label_counts = {}
most_common = ""
most_common_count = 0
...

# 3. `usage` is the number of tokens each model used; `price_per_1000` is the price for 1000 tokens.
#    - `total_tokens`: all the tokens added up (no loop needed),
#    - `costs`: a dictionary from each model name to its cost, tokens / 1000 * price, rounded to 2 decimal places,
#    - `heavy_users`: a list of the models that used more than 1000 tokens, in alphabetical order.
usage = {"gpt": 1200, "bert": 300, "llama": 2500, "t5": 800}
price_per_1000 = {"gpt": 0.5, "bert": 0.1, "llama": 0.2, "t5": 0.25}
total_tokens = ...
costs = {}
heavy_users = []
...

# 4. A conversation with an LLM is a list of dictionaries.
#    - Set `first_role` to the role of the first message.
#    - Append one more message to `messages`: role "assistant", content "It depends on the model."
#    Then, looping over all five messages:
#    - fill `user_questions` with the content of every message whose role is "user",
#    - fill `turns_per_role` so that each role maps to its number of messages.
messages = [
    {"role": "system", "content": "You are a helpful tutor."},
    {"role": "user", "content": "What is a token?"},
    {"role": "assistant", "content": "A token is a small piece of text."},
    {"role": "user", "content": "How many tokens fit in a context window?"},
]
first_role = ...
user_questions = []
turns_per_role = {}
...

# 5. List comprehensions. Each answer is ONE line.
#    - `cleaned`: every word of `raw_words` without its surrounding spaces and in lower case,
#    - `lengths`: the length of every word in `cleaned`,
#    - `long_words`: only the words in `cleaned` with more than 4 letters,
#    - `grades`: "pass" for every score of 0.5 or more, "fail" for the others.
raw_words = ["  Hello", "WORLD ", " Tokens  ", "ai"]
scores = [0.91, 0.45, 0.78, 0.3]
cleaned = ...
lengths = ...
long_words = ...
grades = ...

# 6. Models need numbers, not words, so every label gets an id.
#    - `unique_labels`: a sorted list of the distinct items in `animals`,
#    - `label_to_id`: a dictionary comprehension giving each label its position in `unique_labels`,
#    - `id_to_label`: the same dictionary the other way round (a comprehension over label_to_id.items()),
#    - `encoded`: a list with the id of every item in `animals`, in order,
#    - `first_letters`: a set comprehension with the first letter of every item in `animals`.
animals = ["dog", "cat", "bird", "cat", "dog", "fish"]
unique_labels = ...
label_to_id = ...
id_to_label = ...
encoded = ...
first_letters = ...

# 7. Filtering, transforming and ranking a dictionary.
#    - `strong`: a dictionary with only the models whose accuracy is 0.85 or more,
#    - `as_percent`: every model mapped to its accuracy as a whole-number percentage (0.91 becomes 91),
#    - `ranking`: a list of the model names from most to least accurate.
#      Build a list of (accuracy, name) tuples, sort it with reverse=True, then take the names.
accuracies = {"gpt": 0.91, "bert": 0.88, "t5": 0.79, "llama": 0.93, "elmo": 0.72}
strong = ...
as_percent = ...
ranking = ...

# 8. A better tokenizer. Yesterday's used `index`, which searches the whole list for every word.
#    A dictionary looks a word up instantly, and `get` can deal with words it has never seen.
#    - `word_counts`: each word of `corpus` mapped to how often it appears,
#    - `word_to_id`: the distinct words of `corpus` in alphabetical order, numbered from 1
#      ("and" is 1, "model" is 2, ...), plus the extra pair "<unk>": 0 for unknown words,
#    - `token_ids`: the id of every word in `new_sentence`, in order; unknown words get 0,
#    - `id_to_word`: `word_to_id` the other way round,
#    - `decoded`: `token_ids` turned back into text, the words joined with single spaces.
corpus = "the model reads the tokens and the model writes tokens"
new_sentence = "the model writes poems and reads tokens"
word_counts = {}
...
word_to_id = ...
token_ids = ...
id_to_word = ...
decoded = ...


# ---------------------------------------------------------------------------
# Checks: don't edit below this line.
CHECKS = [
    ("model_name, batch_size and setting_count are right; config has been updated", lambda ns: ns["model_name"] == "tiny-gpt" and ns["batch_size"] == 32 and ns["config"] == {"model": "tiny-gpt", "learning_rate": 0.001, "epochs": 5, "batch_size": 64} and ns["setting_count"] == 4, 'config["model"] and config.get("batch_size", 32). Then config["learning_rate"] = 0.001, config["batch_size"] = 64 and del config["debug"]. setting_count is len(config), worked out after the changes.'),
    ("label_counts is right and most_common is cat (4)", lambda ns: ns["label_counts"] == {"cat": 4, "dog": 2, "bird": 1, "fish": 1} and ns["most_common"] == "cat" and ns["most_common_count"] == 4, "for label in labels: label_counts[label] = label_counts.get(label, 0) + 1. Then for label, count in label_counts.items(): if count > most_common_count, update both variables."),
    ("total_tokens, costs and heavy_users are right", lambda ns: ns["total_tokens"] == 4800 and ns["costs"] == {"gpt": 0.6, "bert": 0.03, "llama": 0.5, "t5": 0.2} and ns["heavy_users"] == ["gpt", "llama"], "sum(usage.values()). Then for model, tokens in usage.items(): costs[model] = round(tokens / 1000 * price_per_1000[model], 2), and append the model to heavy_users if tokens > 1000. Sort heavy_users at the end."),
    ("first_role, the new message, user_questions and turns_per_role are right", lambda ns: ns["first_role"] == "system" and len(ns["messages"]) == 5 and ns["messages"][-1] == {"role": "assistant", "content": "It depends on the model."} and ns["user_questions"] == ["What is a token?", "How many tokens fit in a context window?"] and ns["turns_per_role"] == {"system": 1, "user": 2, "assistant": 2}, 'messages[0]["role"]. Append {"role": "assistant", "content": "It depends on the model."} BEFORE the loop. In the loop, count message["role"] with the get pattern and append message["content"] when the role is "user".'),
    ("cleaned, lengths, long_words and grades are right", lambda ns: ns["cleaned"] == ["hello", "world", "tokens", "ai"] and ns["lengths"] == [5, 5, 6, 2] and ns["long_words"] == ["hello", "world", "tokens"] and ns["grades"] == ["pass", "fail", "pass", "fail"], '[word.strip().lower() for word in raw_words], [len(word) for word in cleaned], [word for word in cleaned if len(word) > 4] and ["pass" if score >= 0.5 else "fail" for score in scores].'),
    ("unique_labels, label_to_id, id_to_label, encoded and first_letters are right", lambda ns: ns["unique_labels"] == ["bird", "cat", "dog", "fish"] and ns["label_to_id"] == {"bird": 0, "cat": 1, "dog": 2, "fish": 3} and ns["id_to_label"] == {0: "bird", 1: "cat", 2: "dog", 3: "fish"} and ns["encoded"] == [2, 1, 0, 1, 2, 3] and type(ns["first_letters"]) is set and ns["first_letters"] == {"b", "c", "d", "f"}, "sorted(set(animals)). {label: number for number, label in enumerate(unique_labels)}. {number: label for label, number in label_to_id.items()}. [label_to_id[animal] for animal in animals]. {animal[0] for animal in animals}."),
    ("strong, as_percent and ranking are right", lambda ns: ns["strong"] == {"gpt": 0.91, "bert": 0.88, "llama": 0.93} and ns["as_percent"] == {"gpt": 91, "bert": 88, "t5": 79, "llama": 93, "elmo": 72} and all(type(value) is int for value in ns["as_percent"].values()) and ns["ranking"] == ["llama", "gpt", "bert", "t5", "elmo"], "{name: accuracy for name, accuracy in accuracies.items() if accuracy >= 0.85}. Use round(accuracy * 100) for the percentages. For ranking: pairs = sorted([(accuracy, name) for name, accuracy in accuracies.items()], reverse=True), then [name for accuracy, name in pairs]."),
    ("tokenizer: word_counts, word_to_id, token_ids, id_to_word and decoded are right", lambda ns: ns["word_counts"] == {"the": 3, "model": 2, "reads": 1, "tokens": 2, "and": 1, "writes": 1} and ns["word_to_id"] == {"<unk>": 0, "and": 1, "model": 2, "reads": 3, "the": 4, "tokens": 5, "writes": 6} and ns["token_ids"] == [4, 2, 6, 0, 1, 3, 5] and ns["id_to_word"] == {0: "<unk>", 1: "and", 2: "model", 3: "reads", 4: "the", 5: "tokens", 6: "writes"} and ns["decoded"] == "the model writes <unk> and reads tokens", 'Count with word_counts[word] = word_counts.get(word, 0) + 1. word_to_id = {word: number for number, word in enumerate(sorted(word_counts), start=1)}, then word_to_id["<unk>"] = 0. token_ids = [word_to_id.get(word, 0) for word in new_sentence.split()]. Swap keys and values for id_to_word, then " ".join([id_to_word[token_id] for token_id in token_ids]).'),
]

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from checker import run

    run(globals(), CHECKS)
