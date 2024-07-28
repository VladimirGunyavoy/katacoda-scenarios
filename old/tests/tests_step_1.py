import pprint
from pathlib import Path

from checker import SberChecker

sber_checker = SberChecker(
    filename=Path(__file__).parent.parent / 'tasks' / "step_1.py",
    tests=[
        {"args": [[1, 2, 3]], "return": 3},
        {"args": [[-3, -2, -1]], "return": -1},
        {"args": [[0]], "return": 0}
    ],
    call="get_last"
)

pprint.pprint(sber_checker.run())
