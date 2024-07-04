import pprint
from datetime import datetime

from checker import SberChecker

year = datetime.now().year

sber_checker = SberChecker(
    filename="../tasks/lesson_1_part_1_problem_1.py",
    tests=[
        {"output": [f"year: {year}"]},
    ]
)

pprint.pprint(sber_checker.run())
