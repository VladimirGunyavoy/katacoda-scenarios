import pprint
from pathlib import Path

from checker import SberChecker

tests = [
    {
        "args": [100, 10],
        "return": 10
    }

]
sber_checker = SberChecker(
    filename=Path(__file__).parent.parent / 'tasks' / "02.py",
    tests=tests,
    call="get_tax"
)

result = sber_checker.run()
pprint.pprint(result)
