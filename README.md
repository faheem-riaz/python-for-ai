# Python for AI — from zero

My daily path from Python basics to building AI applications: one lesson a day for 40 days, following [CURRICULUM.md](CURRICULUM.md).

Lessons and exercises are prepared with [Claude](https://claude.com) as my tutor; I work through the exercises myself.

## How each day works

Every day has its own folder in [`days/`](days) with:

| File | What it's for |
| --- | --- |
| `lesson.md` | The lesson: read this first (about 30–40 minutes). |
| `exercises.py` | Replace each `...` with your answer. |
| `solutions.py` | Reference answers: compare *after* trying. |
| `feedback.md` | Notes on my attempt, added the following day (when I've tried the exercises). |

Check your answers from the day's folder:

```bash
cd days/day-01-hello-python
python3 exercises.py              # checks my answers
python3 exercises.py --solutions  # checks the reference solutions
```

Days 1–11 need nothing but Python 3. From Phase 2 onwards, install the libraries in a virtual environment (set up on Day 12):

```bash
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

## Progress

| Phase | Days | Status |
| --- | --- | --- |
| 1. Python foundations | 1–11 | 🟡 in progress |
| 2. Tools of the trade | 12–14 | ⬜ |
| 3. Data with NumPy and pandas | 15–20 | ⬜ |
| 4. Visualisation and the maths behind ML | 21–24 | ⬜ |
| 5. Machine learning with scikit-learn | 25–31 | ⬜ |
| 6. Deep learning with PyTorch | 32–35 | ⬜ |
| 7. LLMs and AI applications | 36–40 | ⬜ |

## Lessons

| Day | Lesson |
| --- | --- |
| 1 | [Hello, Python](days/day-01-hello-python/lesson.md) |
| 2 | [Numbers and Strings](days/day-02-numbers-and-strings/lesson.md) |
