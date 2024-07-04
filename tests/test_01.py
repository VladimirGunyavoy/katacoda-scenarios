import pprint
from pathlib import Path

from checker import SberChecker

postcode = """
try:
    a
    print("а задан")
except:
    print("а не задан")
try:
    b
    print("b задан")
except:
    print("b не задан")
"""

sber_checker = SberChecker(
    filename=Path(__file__).parent.parent / 'tasks' / '01.py',
    tests=[
        {
            "input": [],
            "output": ["а задан", "b задан"]
        },
    ],
    postcode=postcode,
)

result = sber_checker.run()
pprint.pprint(result)
