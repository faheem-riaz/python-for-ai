"""Day 3 reference solutions. Try the exercises first, then compare."""

raw_epochs = "12"
raw_learning_rate = "0.001"
epochs = int(raw_epochs)                  # "12" -> 12
learning_rate = float(raw_learning_rate)  # "0.001" -> 0.001

summary = "Trained for " + str(epochs) + " epochs"  # + only joins str to str

loss = 0.42
target_loss = 0.5
confidence = 0.87
model_a = "Claude"
model_b = "claude"
reached_target = loss <= target_loss
valid_confidence = 0 <= confidence <= 1             # chained comparison
same_model = model_a.lower() == model_b.lower()     # normalise case, then compare

has_api_key = True
tokens_used = 950
token_limit = 1000
is_flagged = False
score = 0.35
has_internet = True
can_call_api = has_api_key and tokens_used < token_limit
needs_review = is_flagged or score < 0.5
is_offline = not has_internet

sentiment = 0.31
if sentiment >= 0.5:
    label = "positive"
else:
    label = "negative"
# One-line alternative: label = "positive" if sentiment >= 0.5 else "negative"

accuracy = 0.84
if accuracy >= 0.9:       # highest threshold first, so each branch only catches its own range
    grade = "excellent"
elif accuracy >= 0.75:
    grade = "good"
elif accuracy >= 0.5:
    grade = "fair"
else:
    grade = "poor"

user_age_text = " 29 "
cleaned_age = user_age_text.strip()
if cleaned_age.isdigit():
    age = int(cleaned_age)
else:
    age = 0
can_sign_up = age >= 18

raw_temperature = " 1.7 "
cleaned_temperature = raw_temperature.strip()
if cleaned_temperature:   # an empty string is falsy
    temperature = float(cleaned_temperature)
else:
    temperature = 1.0

if 0 <= temperature <= 0.3:
    status = "focused"
elif 0 <= temperature <= 1.0:   # the 0 <= keeps negative values out of this branch
    status = "balanced"
elif 0 <= temperature <= 2.0:
    status = "creative"
else:
    status = "invalid"

status_message = f"temperature {temperature} is {status}"
