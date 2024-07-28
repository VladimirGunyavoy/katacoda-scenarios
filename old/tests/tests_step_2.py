import pprint
from pathlib import Path

from checker import SberChecker

sber_checker = SberChecker(
    filename=Path(__file__).parent.parent / 'tasks' / "step_2.py",
    tests=[
        {
            "args": [],
            "return": 'Function without arguments'
        },
    ],
    call="func_without_arguments",
)

pprint.pprint(sber_checker.run())
