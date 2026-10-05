"""Day 5 reference solutions. Try the exercises first, then compare."""

layers = [784, 512, 256, 128, 10]
input_size = layers[0]
output_size = layers[-1]
hidden_sizes = layers[1:-1]        # from position 1 up to, not including, the last

pipeline = ["load", "tokenise", "debug", "train"]
pipeline.append("evaluate")
pipeline.insert(1, "clean")        # everything after position 1 moves right
pipeline.remove("debug")
pipeline[2] = "tokenize"           # "tokenise" is at position 2 after the insert

losses = [0.52, 0.31, 0.47, 0.29, 0.38, 0.33]
lowest = min(losses)
highest = max(losses)
average = round(sum(losses) / len(losses), 2)
best_three = sorted(losses)[:3]    # sorted() leaves `losses` in its original order

raw_scores = "0.91 0.45 0.78 0.30 0.66 0.50".split()
scores = []
passed = []
for text in raw_scores:
    score = float(text)            # split() gives strings
    scores.append(score)
    if score >= 0.5:
        passed.append(score)

image_shape = (32, 3, 224, 224)
train_size = 2000
test_size = 8000
batch, channels, height, width = image_shape    # one variable per item
train_size, test_size = test_size, train_size   # swap without a temporary variable
pixels = height * width

results = [("gpt", 0.91), ("bert", 0.88), ("t5", 0.79), ("llama", 0.93), ("elmo", 0.72)]
best_model = ""
best_accuracy = 0.0
strong_models = []
for name, accuracy in results:     # unpack each (name, accuracy) tuple
    if accuracy > best_accuracy:
        best_model = name
        best_accuracy = accuracy
    if accuracy >= 0.85:
        strong_models.append(name)

train_words = "the cat sat on the mat and the dog sat on the rug".split()
test_words = "the bird sat on the cat and sang".split()
vocabulary = set(train_words)      # duplicates disappear
vocabulary_size = len(vocabulary)
unseen = set(test_words) - vocabulary                 # in test but not in train
shared_sorted = sorted(vocabulary & set(test_words))  # in both; sorted() gives a list

sentence = "The model reads the tokens and the model writes tokens"
words = sentence.lower().split()
vocab = sorted(set(words))         # distinct words, in alphabetical order
token_ids = []
for word in words:
    token_ids.append(vocab.index(word))
decoded_words = []
for token_id in token_ids:
    decoded_words.append(vocab[token_id])
decoded = " ".join(decoded_words)
