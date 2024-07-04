import pprint
from pathlib import Path

from checker import SberChecker


sber_checker = SberChecker(
    filename=Path(__file__).parent.parent / 'tasks' / "02.py",
    tests=[
        {
            "input": ["Варежка"],
            "output": ["Количество р", "1"]
        },
    ]
)

result = sber_checker.run()
pprint.pprint(result)
