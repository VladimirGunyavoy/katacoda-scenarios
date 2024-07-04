import pprint
from pathlib import Path

from checker import SberChecker

sber_checker = SberChecker(
    filename=Path(__file__).parent.parent / 'tasks' / "05.py",
    tests=[
        {
            "args": ["Варежка"],
            "return": 1,
        },
        {
            "args": ["Ротор"],
            "return": 2,
        },
    ],
    call="count_r",
)

result = sber_checker.run()
pprint.pprint(result)
