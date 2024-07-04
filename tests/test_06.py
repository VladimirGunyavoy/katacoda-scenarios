import pprint
from pathlib import Path

from checker import SberChecker

sber_checker = SberChecker(
    filename=Path(__file__).parent.parent / 'tasks' / "06.py",
    tests=[
        {
            "args": [2, 3],
            "return": 5,
        },
        {
            "args": [4, 6],
            "return": 10,
        },
    ],
    call="add",
)

result = sber_checker.run()
pprint.pprint(result)

