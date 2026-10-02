"""Day 4 exercises: Loops.

Replace each `...` with your answer, then run:

    python3 exercises.py

Lines that start with # are instructions; you don't need to change them.
Most answers are a loop of several lines: write it where the `...` is.
"""

# 1. Write a `while` loop that keeps halving `learning_rate` for as long as it is 0.001 or more.
#    Add 1 to `halvings` each time you halve it.
learning_rate = 0.1
halvings = 0
while learning_rate >= 0.001:
    learning_rate = learning_rate / 2
    halvings += 1

# 2. Use a `for` loop with `range` to add up the squares of the numbers 1 to 10
#    (1*1 + 2*2 + ... + 10*10) in `squares_total`.
squares_total = 0
for number in range(1, 11):
    squares_total += number * number

# 3. Loop over the characters of `prompt` and count the vowels (a, e, i, o, u) in `vowels`.
#    Upper-case vowels count too.
prompt = "Explain attention in transformers"
vowels = 0
for letter in prompt:
    if letter.lower() in "aeiou":
        vowels += 1

# 4. Use `range` with a negative step to build `countdown` so that it ends up as exactly:
#    5 4 3 2 1 liftoff
countdown = ""
for i in range(5, 0, -1):
    countdown += str(i) + " "

countdown += "liftoff"  
    

# 5. Use `zip` to compare each prediction with its answer. Count the matches in `correct`,
#    then set `accuracy` to the fraction that were correct (a float between 0 and 1).
predictions = "cat dog cat bird dog".split()
answers = "cat dog dog bird cat".split()
correct = 0
for pred, ans in zip(predictions, answers):
    if pred == ans:
        correct += 1

accuracy = correct / len(predictions)

# 6. `losses` holds the loss after each epoch, as strings (epoch 1 comes first).
#    Use `enumerate` with start=1 to find the lowest loss. Store it as a float in `best_loss`
#    and the epoch it happened in as `best_epoch`.
losses = "0.9 0.7 0.4 0.35 0.5".split()
best_epoch = 0
best_loss = 100.0
for i, data in enumerate(losses, start = 1):
    fl = float(data)
    if fl < best_loss:
        best_loss = fl
        best_epoch = i

    

# 7. Loop over `stream`:
#    - when you reach "STOP", leave the loop with `break` (nothing after it is read);
#    - if an item isn't all digits, add 1 to `skipped` and move on with `continue`;
#    - otherwise add the item, as an int, to `token_total`.
stream = "12 7 skip 30 x 5 STOP 99".split()
token_total = 0
skipped = 0
for st in stream:
    if st == "STOP":
        break
    if not st.isdigit():
        skipped += 1
        continue
    else:
        token_total += int(st)

# 8. Early stopping. Loop over epochs 1 to `max_epochs`. In every epoch:
#    - multiply `final_loss` by 0.8 and round it to 4 decimal places;
#    - set `epochs_run` to the current epoch;
#    - if `final_loss` is now below `target_loss`, stop the loop.
#    After the loop, set `training_report` with an f-string, in this format:
#    stopped after 3 epochs at loss 0.512
max_epochs = 50
target_loss = 0.1
final_loss = 1.0
epochs_run = 0
for i in range(1, max_epochs+1):
    final_loss =  round(final_loss * 0.8, 4)
    epochs_run = i
    if final_loss < target_loss:
        break
training_report = f"stopped after {epochs_run} epochs at loss {final_loss}"


# ---------------------------------------------------------------------------
# Checks: don't edit below this line.
CHECKS = [
    ("learning_rate was halved 7 times and is below 0.001", lambda ns: ns["halvings"] == 7 and 0.0005 < ns["learning_rate"] < 0.001, "while learning_rate >= 0.001: then, indented, learning_rate = learning_rate / 2 and halvings += 1."),
    ("squares_total is 385", lambda ns: ns["squares_total"] == 385, "for number in range(1, 11): squares_total += number * number  (range stops before 11)."),
    ("vowels is 11", lambda ns: ns["vowels"] == 11, 'for character in prompt.lower(): if character in "aeiou": vowels += 1'),
    ("countdown is '5 4 3 2 1 liftoff'", lambda ns: ns["countdown"] == "5 4 3 2 1 liftoff", 'for number in range(5, 0, -1): countdown += f"{number} "   then, after the loop, countdown += "liftoff".'),
    ("correct is 3 and accuracy is 0.6", lambda ns: ns["correct"] == 3 and type(ns["accuracy"]) is float and ns["accuracy"] == 0.6, "for predicted, actual in zip(predictions, answers): if predicted == actual: correct += 1. Then accuracy = correct / len(answers)."),
    ("best_loss is 0.35 at best_epoch 4", lambda ns: type(ns["best_loss"]) is float and ns["best_loss"] == 0.35 and ns["best_epoch"] == 4, "for epoch, raw_loss in enumerate(losses, start=1): convert with float(raw_loss); if it is lower than best_loss, update both best_loss and best_epoch."),
    ("token_total is 54 and skipped is 2", lambda ns: ns["token_total"] == 54 and ns["skipped"] == 2, 'Check for "STOP" first (break), then `if not item.isdigit():` (skipped += 1, continue), then token_total += int(item).'),
    ("early stopping: epochs_run, final_loss and training_report are correct", lambda ns: ns["epochs_run"] == 11 and ns["final_loss"] == 0.0859 and ns["training_report"] == "stopped after 11 epochs at loss 0.0859", 'for epoch in range(1, max_epochs + 1): final_loss = round(final_loss * 0.8, 4); epochs_run = epoch; if final_loss < target_loss: break. Then f"stopped after {epochs_run} epochs at loss {final_loss}".'),
]

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from checker import run

    run(globals(), CHECKS)
