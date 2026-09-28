"""Shared checker for the daily exercises.

Each day's exercises.py defines a list called CHECKS and ends with:

    if __name__ == "__main__":
        run(globals(), CHECKS)

Run `python3 exercises.py` to check your answers, or `python3 exercises.py --solutions`
to check the reference solutions in solutions.py instead.
"""

import importlib.util
import sys
from pathlib import Path


def _load_solutions(exercise_globals):
    path = Path(exercise_globals["__file__"]).with_name("solutions.py")
    spec = importlib.util.spec_from_file_location("solutions", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return vars(module)


def run(exercise_globals, checks):
    namespace = _load_solutions(exercise_globals) if "--solutions" in sys.argv else exercise_globals
    passed = 0
    for number, (description, test, hint) in enumerate(checks, start=1):
        try:
            ok = bool(test(namespace))
            error = None
        except Exception as exc:  # A wrong answer can raise; report it like a failure.
            ok = False
            error = f"{type(exc).__name__}: {exc}"
        passed += ok
        print(f"{'✔' if ok else '✘'} {number}. {description}")
        if not ok:
            print(f"     hint: {hint}")
            if error:
                print(f"     error: {error}")
    print(f"\n{passed}/{len(checks)} passed" + ("  🎉 all done!" if passed == len(checks) else ""))
    return passed == len(checks)
