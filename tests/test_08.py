import pprint

from checker import SberChecker

sber_checker = SberChecker(
    filename="../tasks/08.py",
    tests=[
        {
            "input": [],
            "output": ["Function without args"],
        }
    ],
    call="",
)

result = sber_checker.run()
pprint.pprint(result)

