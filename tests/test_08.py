import pprint
from pathlib import Path

from checker import SberChecker

sber_checker = SberChecker(
    filename=Path(__file__).parent.parent / 'tasks' / "08.py",
    tests=[
        {
            "args": [],
            "return": "Function without args",
        }
    ],
    call="without_args",
)

result = sber_checker.run()
pprint.pprint(result)

