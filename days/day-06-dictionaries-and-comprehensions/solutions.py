"""Day 6 reference solutions. Try the exercises first, then compare."""

config = {"model": "tiny-gpt", "learning_rate": 0.01, "epochs": 5, "debug": True}
model_name = config["model"]
batch_size = config.get("batch_size", 32)   # the key is missing, so get() gives the default
config["learning_rate"] = 0.001             # existing key: the value is replaced
config["batch_size"] = 64                   # new key: the pair is added
del config["debug"]                         # config.pop("debug") works too
setting_count = len(config)

labels = ["cat", "dog", "cat", "bird", "dog", "cat", "fish", "cat"]
label_counts = {}
for label in labels:
    label_counts[label] = label_counts.get(label, 0) + 1   # 0 the first time we see a label
most_common = ""
most_common_count = 0
for label, count in label_counts.items():
    if count > most_common_count:
        most_common = label
        most_common_count = count

usage = {"gpt": 1200, "bert": 300, "llama": 2500, "t5": 800}
price_per_1000 = {"gpt": 0.5, "bert": 0.1, "llama": 0.2, "t5": 0.25}
total_tokens = sum(usage.values())
costs = {}
heavy_users = []
for model, tokens in usage.items():
    costs[model] = round(tokens / 1000 * price_per_1000[model], 2)   # same key, other dictionary
    if tokens > 1000:
        heavy_users.append(model)
heavy_users.sort()

messages = [
    {"role": "system", "content": "You are a helpful tutor."},
    {"role": "user", "content": "What is a token?"},
    {"role": "assistant", "content": "A token is a small piece of text."},
    {"role": "user", "content": "How many tokens fit in a context window?"},
]
first_role = messages[0]["role"]            # first the list position, then the key
messages.append({"role": "assistant", "content": "It depends on the model."})
user_questions = []
turns_per_role = {}
for message in messages:
    role = message["role"]
    turns_per_role[role] = turns_per_role.get(role, 0) + 1
    if role == "user":
        user_questions.append(message["content"])

raw_words = ["  Hello", "WORLD ", " Tokens  ", "ai"]
scores = [0.91, 0.45, 0.78, 0.3]
cleaned = [word.strip().lower() for word in raw_words]
lengths = [len(word) for word in cleaned]
long_words = [word for word in cleaned if len(word) > 4]            # `if` at the end filters
grades = ["pass" if score >= 0.5 else "fail" for score in scores]   # `if/else` at the front chooses

animals = ["dog", "cat", "bird", "cat", "dog", "fish"]
unique_labels = sorted(set(animals))
label_to_id = {label: number for number, label in enumerate(unique_labels)}
id_to_label = {number: label for label, number in label_to_id.items()}   # swap key and value
encoded = [label_to_id[animal] for animal in animals]
first_letters = {animal[0] for animal in animals}                   # a set: duplicates disappear

accuracies = {"gpt": 0.91, "bert": 0.88, "t5": 0.79, "llama": 0.93, "elmo": 0.72}
strong = {name: accuracy for name, accuracy in accuracies.items() if accuracy >= 0.85}
as_percent = {name: round(accuracy * 100) for name, accuracy in accuracies.items()}
pairs = sorted([(accuracy, name) for name, accuracy in accuracies.items()], reverse=True)
ranking = [name for accuracy, name in pairs]   # tuples sort by their first item

corpus = "the model reads the tokens and the model writes tokens"
new_sentence = "the model writes poems and reads tokens"
word_counts = {}
for word in corpus.split():
    word_counts[word] = word_counts.get(word, 0) + 1
word_to_id = {word: number for number, word in enumerate(sorted(word_counts), start=1)}
word_to_id["<unk>"] = 0                        # id 0 is reserved for unknown words
token_ids = [word_to_id.get(word, 0) for word in new_sentence.split()]
id_to_word = {number: word for word, number in word_to_id.items()}
decoded = " ".join([id_to_word[token_id] for token_id in token_ids])
