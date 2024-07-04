import pprint

from checker import SberChecker


sber_checker = SberChecker(
    filename="../tasks/03.py",
    tests=[
        {
            "input": [1],
            "output": ["1", "1"]
        },
    ]
)

result = sber_checker.run()
pprint.pprint(result)
