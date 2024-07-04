import pprint

from checker import SberChecker


sber_checker = SberChecker(
    filename="../tasks/03_1.py",
    tests=[
        {
            "input": [2, 4],
            "output": ["2", "4"]
        },
    ]
)

result = sber_checker.run()
pprint.pprint(result)
