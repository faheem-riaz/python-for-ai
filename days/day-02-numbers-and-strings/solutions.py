"""Day 2 reference solutions. Try the exercises first, then compare."""

total_examples = 1000
batch_size = 32
full_batches = total_examples // batch_size  # 31 full batches of 32 = 992
leftover = total_examples % batch_size       # 8 examples left over

correct = 874
total = 1000
accuracy = correct / total                   # / always gives a float: 0.874
accuracy_pct = round(accuracy * 100, 1)      # 87.4

run_seconds = 7384
hours = run_seconds // 3600                  # 2
minutes = (run_seconds % 3600) // 60         # what's left after the hours, in minutes: 3
seconds = run_seconds % 60                   # 4

filename = "training_data_2026.csv"
extension = filename[-3:]                    # works for any name ending in a 3-letter extension
year = filename[-8:-4]                       # the 4 characters just before ".csv"
stem = filename[:-4]                         # drop the last 4 characters (".csv")

raw_prompt = "   Summarise THIS Article, Please.   "
clean_prompt = raw_prompt.strip().lower()    # each method returns a new string

review = "The model was fast and the answers were accurate"
word_count = len(review.split())             # split() gives a list of 9 words
hyphenated = "-".join(review.split())        # join is called on the separator

epoch = 3
total_epochs = 10
loss = 0.123456
log_line = f"Epoch {epoch}/{total_epochs} - loss: {loss:.3f}"

tokens = 12_500
price_per_million = 3.0
cost = tokens / 1_000_000 * price_per_million  # about 0.0375 (floats are close, not exact)
cost_label = f"${cost:.4f} for {tokens:,} tokens"
