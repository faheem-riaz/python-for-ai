"""Day 5 exercises: Collections (lists, tuples and sets).

Replace each `...` with your answer, then run:

    python3 exercises.py

Lines that start with # are instructions; you don't need to change them.
Some answers are several lines: write them where the `...` is.
"""

# 1. `layers` holds the size of each layer in a neural network.
#    Use indexing and slicing (not numbers you typed yourself) to set:
#    - `input_size` to the first item,
#    - `output_size` to the last item (use a negative index),
#    - `hidden_sizes` to a list of everything in between.
layers = [784, 512, 256, 128, 10]
input_size = layers[0]
output_size = layers[-1]
hidden_sizes = layers[1:-1]

# 2. Change `pipeline` using list methods so that it ends up as exactly:
#    ['load', 'clean', 'tokenize', 'train', 'evaluate']
#    - add "evaluate" at the end,
#    - put "clean" in at position 1,
#    - remove "debug",
#    - replace "tokenise" with "tokenize" by assigning to its position.
pipeline = ["load", "tokenise", "debug", "train"]
pipeline.append("evaluate")
pipeline.insert(1, "clean")
pipeline.remove("debug")
del pipeline[2]
pipeline.insert(2, "tokenize")



# 3. Statistics for a training run, using built-in functions (no loops needed):
#    - `lowest` and `highest`: the smallest and largest loss,
#    - `average`: the mean loss, rounded to 2 decimal places,
#    - `best_three`: a NEW list of the three smallest losses, smallest first.
#    `losses` itself must stay in its original order.
losses = [0.52, 0.31, 0.47, 0.29, 0.38, 0.33]
lowest = min(losses)
highest = max(losses)
average = round(sum(losses) / len(losses), 2)
best_three = sorted(losses)[:3]

# 4. `raw_scores` is a list of strings. With a loop and `append`, fill:
#    - `scores` with every score as a float,
#    - `passed` with only the scores that are 0.5 or higher (as floats).
raw_scores = "0.91 0.45 0.78 0.30 0.66 0.50".split()
scores = []
passed = []
for text in raw_scores:
    float_value = float(text)
    scores.append(float_value)
    if float_value >= 0.5:
        passed.append(float_value) 



# 5. Tuples.
#    - Unpack `image_shape` in one line into the variables `batch`, `channels`, `height`, `width`.
#    - Set `pixels` to height times width.
#    - Swap `train_size` and `test_size` in one line (someone mixed them up).
image_shape = (32, 3, 224, 224)
train_size = 2000
test_size = 8000
batch, channels, height, width = image_shape
pixels = height * width
train_size, test_size = test_size, train_size

# 6. `results` is a list of (model name, accuracy) tuples. Loop over it, unpacking each tuple, to set:
#    - `best_model` and `best_accuracy`: the name and accuracy of the most accurate model,
#    - `strong_models`: a list of the names with an accuracy of 0.85 or more, in their original order.
results = [("gpt", 0.91), ("bert", 0.88), ("t5", 0.79), ("llama", 0.93), ("elmo", 0.72)]
best_model = ""
best_accuracy = 0.0
strong_models = []
for model_name, model_accuracy in results:
    if best_accuracy < model_accuracy:
        best_accuracy = model_accuracy
        best_model = model_name
    if model_accuracy >= 0.85:
        strong_models.append(model_name)

    
    

# 7. Sets. Both variables below are lists of words.
#    - `vocabulary`: a set of the distinct words in `train_words`,
#    - `vocabulary_size`: how many distinct words that is,
#    - `unseen`: a set of the words in `test_words` that never appear in `train_words`,
#    - `shared_sorted`: a sorted LIST of the words that appear in both.
train_words = "the cat sat on the mat and the dog sat on the rug".split()
test_words = "the bird sat on the cat and sang".split()
vocabulary = set(train_words)
vocabulary_size = len(vocabulary)
unseen = set(test_words) - vocabulary
shared_sorted = sorted(vocabulary & set(test_words))

# 8. A tiny tokenizer. LLMs don't read words; they read numbers called token ids.
#    - `vocab`: a sorted list of the distinct words in `sentence` (lower-case it first, then split),
#    - `token_ids`: a list with, for every word of the lower-cased sentence in order,
#      that word's position in `vocab` (the `index` method finds it),
#    - `decoded`: turn `token_ids` back into text: look each id up in `vocab`
#      and join the words with single spaces.
sentence = "The model reads the tokens and the model writes tokens"
vocab = sorted(set(sentence.lower().split()))
token_ids = []
lower_case = sentence.lower().split()
for word in lower_case:
    token_ids.append(vocab.index(word))

decoded_words = []
for index in token_ids:
    decoded_words.append(vocab[index])

decoded = " ".join(decoded_words)


# ---------------------------------------------------------------------------
# Checks: don't edit below this line.
CHECKS = [
    ("input_size, output_size and hidden_sizes are right", lambda ns: ns["input_size"] == 784 and ns["output_size"] == 10 and ns["hidden_sizes"] == [512, 256, 128], "layers[0] is the first item, layers[-1] the last, and layers[1:-1] is everything in between."),
    ("pipeline is ['load', 'clean', 'tokenize', 'train', 'evaluate']", lambda ns: ns["pipeline"] == ["load", "clean", "tokenize", "train", "evaluate"], 'pipeline.append("evaluate"), pipeline.insert(1, "clean"), pipeline.remove("debug"). After the insert, "tokenise" is at position 2: pipeline[2] = "tokenize".'),
    ("lowest, highest, average and best_three are right; losses is unchanged", lambda ns: ns["lowest"] == 0.29 and ns["highest"] == 0.52 and ns["average"] == 0.38 and ns["best_three"] == [0.29, 0.31, 0.33] and ns["losses"] == [0.52, 0.31, 0.47, 0.29, 0.38, 0.33], "min(losses), max(losses), round(sum(losses) / len(losses), 2) and sorted(losses)[:3]. Use sorted(), not .sort(), so the original list keeps its order."),
    ("scores holds 6 floats and passed holds the 4 that are >= 0.5", lambda ns: ns["scores"] == [0.91, 0.45, 0.78, 0.3, 0.66, 0.5] and ns["passed"] == [0.91, 0.78, 0.66, 0.5] and all(type(score) is float for score in ns["scores"]), "for text in raw_scores: score = float(text); scores.append(score); then, if score >= 0.5: passed.append(score)."),
    ("image_shape is unpacked, pixels is 50176 and the sizes are swapped", lambda ns: (ns["batch"], ns["channels"], ns["height"], ns["width"]) == (32, 3, 224, 224) and ns["pixels"] == 50176 and ns["train_size"] == 8000 and ns["test_size"] == 2000, "batch, channels, height, width = image_shape. Then pixels = height * width, and train_size, test_size = test_size, train_size."),
    ("best_model is llama (0.93) and strong_models is ['gpt', 'bert', 'llama']", lambda ns: ns["best_model"] == "llama" and ns["best_accuracy"] == 0.93 and ns["strong_models"] == ["gpt", "bert", "llama"], "for name, accuracy in results: if accuracy > best_accuracy, update best_model and best_accuracy. In a separate `if accuracy >= 0.85:`, append the name to strong_models."),
    ("vocabulary, vocabulary_size, unseen and shared_sorted are right", lambda ns: type(ns["vocabulary"]) is set and ns["vocabulary"] == {"the", "cat", "sat", "on", "mat", "and", "dog", "rug"} and ns["vocabulary_size"] == 8 and type(ns["unseen"]) is set and ns["unseen"] == {"bird", "sang"} and ns["shared_sorted"] == ["and", "cat", "on", "sat", "the"], "vocabulary = set(train_words); len(vocabulary); set(test_words) - vocabulary for the unseen words; sorted(vocabulary & set(test_words)) for the shared ones."),
    ("tokenizer: vocab, token_ids and decoded are right", lambda ns: ns["vocab"] == ["and", "model", "reads", "the", "tokens", "writes"] and ns["token_ids"] == [3, 1, 2, 3, 4, 0, 3, 1, 5, 4] and ns["decoded"] == "the model reads the tokens and the model writes tokens", 'words = sentence.lower().split(); vocab = sorted(set(words)). Loop over words and append vocab.index(word) to token_ids. For decoded, build a list of vocab[token_id] for each id, then " ".join(...) it.'),
]

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from checker import run

    run(globals(), CHECKS)
