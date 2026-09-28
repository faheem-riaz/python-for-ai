"""Day 1 exercises: Hello, Python.

Replace each `...` with your answer, then run:

    python3 exercises.py

Lines that start with # are instructions; you don't need to change them.
"""

# 1. Create a variable called `greeting` holding exactly the text: Hello, AI!
greeting = ...

# 2. There are 60 seconds in a minute, 60 minutes in an hour and 24 hours in a day.
#    Use multiplication (not a number you worked out yourself) to set `seconds_per_day`.
seconds_per_day = ...

# 3. Set `my_name` to your first name, as a string.
my_name = ...

# 4. Join strings with + so that `intro` is "My name is " followed by your name.
#    Use the `my_name` variable rather than typing your name again.
intro = ...

# 5. A rough rule of thumb for English text is that one LLM token is about 4 characters.
#    Using len(), estimate how many tokens `sentence` is: its length divided by 4.
sentence = "Python is the language of AI."
tokens_estimate = ...

# 6. A model trains for `epochs` rounds. Add 1 to `epochs` using the variable itself
#    (the `x = x + 1` pattern from the lesson), so it ends up as 6.
epochs = 5
epochs = ...


# ---------------------------------------------------------------------------
# Checks: don't edit below this line.
CHECKS = [
    ("greeting says Hello, AI!", lambda ns: ns["greeting"] == "Hello, AI!", 'Text needs quotes: "Hello, AI!" (capitals, comma and ! included).'),
    ("seconds_per_day is correct", lambda ns: ns["seconds_per_day"] == 86400, "Multiply 60 * 60 * 24."),
    ("my_name is a non-empty string", lambda ns: isinstance(ns["my_name"], str) and ns["my_name"].strip() != "", 'Put your name in quotes, e.g. "Faheem".'),
    ("intro is built from my_name", lambda ns: ns["intro"] == "My name is " + ns["my_name"], 'Try: "My name is " + my_name (mind the space before the closing quote).'),
    ("tokens_estimate uses len(sentence) / 4", lambda ns: ns["tokens_estimate"] == len(ns["sentence"]) / 4, "len(sentence) gives the number of characters; divide it by 4."),
    ("epochs ends up as 6", lambda ns: ns["epochs"] == 6, "Write: epochs = epochs + 1"),
]

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from checker import run

    run(globals(), CHECKS)
