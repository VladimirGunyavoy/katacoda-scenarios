import pprint
from pathlib import Path

from checker import SberChecker

postcode = """

requests = [
  {"name": "Офисное кресло" , "approved": True},
  {"name": "Бумага для принтера" , "approved": True},  
  {"name": "Надувной розовый крокодил" , "approved": False},  
]

print_approved_requests(requests)

"""


tests = [
    {
        "input": [],
        "output": ["Офисное кресло", "Бумага для принтера"]
    }

]
sber_checker = SberChecker(
    filename=Path(__file__).parent.parent / 'tasks' / "01.py",
    tests=tests,
    postcode=postcode
)

result = sber_checker.run()
pprint.pprint(result)
