"""Day 2 exercises: Numbers and Strings.

Replace each `...` with your answer, then run:

    python3 exercises.py

Lines that start with # are instructions; you don't need to change them.
Use the variables you're given rather than typing the answers as fixed numbers or text.
"""

# 1. You have `total_examples` training examples and a `batch_size`.
#    Set `full_batches` to how many *full* batches you can make (an int, not a float),
#    and `leftover` to how many examples are left over for a final, smaller batch.
total_examples = 1000
batch_size = 32
full_batches = total_examples // batch_size
leftover = total_examples % batch_size

# 2. A classifier got `correct` answers right out of `total`.
#    Set `accuracy` to the fraction correct (a float between 0 and 1),
#    then `accuracy_pct` to that as a percentage rounded to 1 decimal place (e.g. 87.4).
correct = 874
total = 1000
accuracy = correct / total
accuracy_pct = round(accuracy * 100, 1)

# 3. A training run took `run_seconds` seconds. Split it into whole `hours`,
#    the remaining whole `minutes`, and the remaining `seconds`, using // and %.
#    (There are 3600 seconds in an hour.)
run_seconds = 7384
hours = run_seconds // 3600
minutes = run_seconds % 3600 // 60
seconds = run_seconds % 60

# 4. Use slicing on `filename` to set:
#    - `extension` to the last three characters ("csv")
#    - `year` to the four digits of the year ("2026")
#    - `stem` to everything except the final ".csv"
filename = "training_data_2026.csv"
extension = filename[-3:]
year = filename[-8:-4]
stem = filename[:-4]

# 5. User input often arrives messy. Set `clean_prompt` to `raw_prompt` with the
#    spaces at both ends removed and every letter in lowercase (chain two methods).
raw_prompt = "   Summarise THIS Article, Please.   "
clean_prompt = raw_prompt.strip().lower()

# 6. A very simple "tokeniser": set `word_count` to the number of words in `review`,
#    and `hyphenated` to the same words joined with "-" instead of spaces.
review = "The model was fast and the answers were accurate"
word_count = len(review.split())
hyphenated = "-".join(review.split())

# 7. Build a training-log line with an f-string. Using the variables below,
#    `log_line` must be exactly:  Epoch 3/10 - loss: 0.123
#    (show the loss with 3 decimal places using a format spec).
epoch = 3
total_epochs = 10
loss = 0.123456
log_line = f"Epoch {epoch}/{total_epochs} - loss: {loss:.3f}"

# 8. An LLM API charges `price_per_million` dollars per million tokens.
#    Set `cost` to what `tokens` tokens cost, then `cost_label` to an f-string like
#    "$0.0375 for 12,500 tokens" (cost with 4 decimals, tokens with a thousands comma).
tokens = 12_500
price_per_million = 3.0
cost = ( tokens / 1000000 ) * price_per_million
cost_label = f"${cost:.4f} for {tokens:,} tokens"


# ---------------------------------------------------------------------------
# Checks: don't edit below this line.
CHECKS = [
    ("full_batches and leftover are correct", lambda ns: type(ns["full_batches"]) is int and ns["full_batches"] == 31 and ns["leftover"] == 8, "Use total_examples // batch_size and total_examples % batch_size."),
    ("accuracy and accuracy_pct are correct", lambda ns: ns["accuracy"] == 0.874 and ns["accuracy_pct"] == 87.4, "accuracy = correct / total; then round(accuracy * 100, 1)."),
    ("run_seconds split into 2 h 3 min 4 s", lambda ns: (ns["hours"], ns["minutes"], ns["seconds"]) == (2, 3, 4), "hours = run_seconds // 3600; minutes = (run_seconds % 3600) // 60; seconds = run_seconds % 60."),
    ("extension, year and stem sliced correctly", lambda ns: (ns["extension"], ns["year"], ns["stem"]) == ("csv", "2026", "training_data_2026"), "Negative indexes help: filename[-3:], filename[-8:-4], filename[:-4]."),
    ("clean_prompt is trimmed and lowercase", lambda ns: ns["clean_prompt"] == "summarise this article, please.", "Chain the methods: raw_prompt.strip().lower()"),
    ("word_count and hyphenated are correct", lambda ns: ns["word_count"] == 9 and ns["hyphenated"] == "The-model-was-fast-and-the-answers-were-accurate", 'len(review.split()) counts words; "-".join(review.split()) glues them.'),
    ("log_line is formatted exactly", lambda ns: ns["log_line"] == "Epoch 3/10 - loss: 0.123", 'Try: f"Epoch {epoch}/{total_epochs} - loss: {loss:.3f}"'),
    ("cost and cost_label are correct", lambda ns: round(ns["cost"], 6) == 0.0375 and ns["cost_label"] == "$0.0375 for 12,500 tokens", 'cost = tokens / 1_000_000 * price_per_million; then f"${cost:.4f} for {tokens:,} tokens"'),
]

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from checker import run

    run(globals(), CHECKS)
