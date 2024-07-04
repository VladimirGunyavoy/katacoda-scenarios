import pprint

from checker import SberChecker

sber_checker = SberChecker(
    filename="../tasks/05.py",
    tests=[
        {
            "input": ["Варежка"],
            "output": [1],
        },
        {
            "input": ["Ротор"],
            "output": [2],
        },
    ],
    call="count_r",
)

result = sber_checker.run()
pprint.pprint(result)
