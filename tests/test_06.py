import pprint

from checker import SberChecker

sber_checker = SberChecker(
    filename="../tasks/06.py",
    tests=[
        {
            "input": [2, 3],
            "output": [5],
        },
        {
            "input": [4, 6],
            "output": [10],
        },
    ],
    call="add",
)

result = sber_checker.run()
pprint.pprint(result)

