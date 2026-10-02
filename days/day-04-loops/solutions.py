"""Day 4 reference solutions. Try the exercises first, then compare."""

learning_rate = 0.1
halvings = 0
while learning_rate >= 0.001:   # keep going until it drops below 0.001
    learning_rate = learning_rate / 2
    halvings += 1

squares_total = 0
for number in range(1, 11):     # 1 to 10: the stop value is not included
    squares_total += number * number

prompt = "Explain attention in transformers"
vowels = 0
for character in prompt.lower():   # lower() so "E" counts too
    if character in "aeiou":
        vowels += 1

countdown = ""
for number in range(5, 0, -1):     # 5, 4, 3, 2, 1
    countdown += f"{number} "
countdown += "liftoff"

predictions = "cat dog cat bird dog".split()
answers = "cat dog dog bird cat".split()
correct = 0
for predicted, actual in zip(predictions, answers):
    if predicted == actual:
        correct += 1
accuracy = correct / len(answers)

losses = "0.9 0.7 0.4 0.35 0.5".split()
best_epoch = 0
best_loss = 100.0                  # start higher than any real loss
for epoch, raw_loss in enumerate(losses, start=1):
    loss = float(raw_loss)         # split() gives strings
    if loss < best_loss:
        best_loss = loss
        best_epoch = epoch

stream = "12 7 skip 30 x 5 STOP 99".split()
token_total = 0
skipped = 0
for item in stream:
    if item == "STOP":             # nothing after STOP is read
        break
    if not item.isdigit():
        skipped += 1
        continue
    token_total += int(item)

max_epochs = 50
target_loss = 0.1
final_loss = 1.0
epochs_run = 0
for epoch in range(1, max_epochs + 1):
    final_loss = round(final_loss * 0.8, 4)
    epochs_run = epoch
    if final_loss < target_loss:   # early stopping
        break
training_report = f"stopped after {epochs_run} epochs at loss {final_loss}"
