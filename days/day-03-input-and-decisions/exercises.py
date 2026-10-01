"""Day 3 exercises: Input and Decisions.

Replace each `...` with your answer, then run:

    python3 exercises.py

Lines that start with # are instructions; you don't need to change them.
The checker can't type for you, so variables like `raw_epochs` stand in for text a user
typed into input(). Remember: input() always gives you a string.
"""

# 1. A user typed these into input(). Convert them so you can do maths with them:
#    `epochs` must be an int and `learning_rate` must be a float.
raw_epochs = "12"
raw_learning_rate = "0.001"
epochs = ...
learning_rate = ...

# 2. Using + (not an f-string) and the `epochs` variable from exercise 1,
#    set `summary` to exactly:  Trained for 12 epochs
summary = ...

# 3. Set each variable to a comparison (so it becomes True or False):
#    - `reached_target`: is `loss` less than or equal to `target_loss`?
#    - `valid_confidence`: is `confidence` between 0 and 1 (inclusive)? Use one chained comparison.
#    - `same_model`: is `model_a` the same as `model_b`, ignoring upper/lower case?
loss = 0.42
target_loss = 0.5
confidence = 0.87
model_a = "Claude"
model_b = "claude"
reached_target = ...
valid_confidence = ...
same_model = ...

# 4. Use `and`, `or` and `not` to set:
#    - `can_call_api`: True when there is an API key AND tokens_used is below token_limit.
#    - `needs_review`: True when the answer is flagged OR its score is below 0.5.
#    - `is_offline`: the opposite of `has_internet`.
has_api_key = True
tokens_used = 950
token_limit = 1000
is_flagged = False
score = 0.35
has_internet = True
can_call_api = ...
needs_review = ...
is_offline = ...

# 5. Write an if / else that sets `label` to "positive" when `sentiment` is 0.5 or more,
#    and "negative" otherwise.
sentiment = 0.31
label = ...

# 6. Write an if / elif / else that sets `grade` from `accuracy`:
#    0.9 or more -> "excellent", 0.75 or more -> "good", 0.5 or more -> "fair", below 0.5 -> "poor".
#    Think about the order of your checks!
accuracy = 0.84
grade = ...

# 7. A user typed their age, with stray spaces. If the stripped text is all digits,
#    set `age` to it as an int. Otherwise set `age` to 0.
#    Then set `can_sign_up` to True when age is 18 or more.
user_age_text = " 29 "
age = ...
can_sign_up = ...

# 8. Check an LLM temperature setting that a user typed:
#    - If `raw_temperature` is empty (or only spaces), use 1.0. Otherwise convert it to a float.
#      Store the result in `temperature`.
#    - Then set `status`: "focused" if 0 <= temperature <= 0.3, "balanced" if it's at most 1.0,
#      "creative" if it's at most 2.0, and "invalid" for anything else (including negatives).
#    - Finally set `status_message` with an f-string, e.g. "temperature 1.7 is creative".
raw_temperature = " 1.7 "
temperature = ...
status = ...
status_message = ...


# ---------------------------------------------------------------------------
# Checks: don't edit below this line.
CHECKS = [
    ("epochs is the int 12 and learning_rate the float 0.001", lambda ns: type(ns["epochs"]) is int and ns["epochs"] == 12 and type(ns["learning_rate"]) is float and ns["learning_rate"] == 0.001, "Wrap each string: int(raw_epochs) and float(raw_learning_rate)."),
    ("summary is built with str()", lambda ns: ns["summary"] == "Trained for 12 epochs", '"Trained for " + str(epochs) + " epochs" (mind the spaces).'),
    ("the three comparisons are correct", lambda ns: (ns["reached_target"], ns["valid_confidence"], ns["same_model"]) == (True, True, True) and all(type(ns[k]) is bool for k in ("reached_target", "valid_confidence", "same_model")), "loss <= target_loss; 0 <= confidence <= 1; model_a.lower() == model_b.lower()"),
    ("can_call_api, needs_review and is_offline are correct", lambda ns: (ns["can_call_api"], ns["needs_review"], ns["is_offline"]) == (True, True, False) and all(type(ns[k]) is bool for k in ("can_call_api", "needs_review", "is_offline")), "has_api_key and tokens_used < token_limit; is_flagged or score < 0.5; not has_internet"),
    ("label is negative for 0.31", lambda ns: ns["label"] == "negative", 'if sentiment >= 0.5: label = "positive", else: label = "negative" (indent each block).'),
    ("grade is good for 0.84", lambda ns: ns["grade"] == "good", "Check the highest threshold first: if accuracy >= 0.9 ... elif accuracy >= 0.75 ..."),
    ("age is 29 and can_sign_up is True", lambda ns: type(ns["age"]) is int and ns["age"] == 29 and ns["can_sign_up"] is True, "if user_age_text.strip().isdigit(): age = int(user_age_text.strip()); then can_sign_up = age >= 18"),
    ("temperature, status and status_message are correct", lambda ns: ns["temperature"] == 1.7 and ns["status"] == "creative" and ns["status_message"] == "temperature 1.7 is creative", 'Strip first; an empty string is falsy. Rule out invalid values first (temperature < 0 or temperature > 2.0), then check <= 0.3, <= 1.0, else creative. Finally f"temperature {temperature} is {status}".'),
]

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from checker import run

    run(globals(), CHECKS)
