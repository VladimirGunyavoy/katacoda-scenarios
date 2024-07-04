import pprint
from datetime import datetime
from pathlib import Path

from checker import SberChecker

year = datetime.now().year

sber_checker = SberChecker(
    filename=Path(__file__).parent.parent / 'tasks' / "lesson_1_part_1_problem_1.py",
    tests=[
        {
            "input": [],
            "output": [f"year: {year}"]
        },
    ]
)

pprint.pprint(sber_checker.run())
