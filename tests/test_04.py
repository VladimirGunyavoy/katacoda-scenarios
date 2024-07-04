import pprint
from pathlib import Path

from checker import SberChecker


def should_include(code):
    return "for" in code


sber_checker = SberChecker(
    filename=Path(__file__).parent.parent / 'tasks' / "04.py",
    tests=[
        {
            "input": ["1 2 3"],
            "output": ["1", "2", "3"],
        },
    ],
    should_include=should_include,
)

result = sber_checker.run()
pprint.pprint(result)
