import pprint

from checker import SberChecker

sber_checker = SberChecker(
    filename="../tasks/step_0.py",
    tests=[
        {"args": [4], "return": 16},
        {"args": [2], "return": 4},
        {"args": [0], "return": 0}
    ],
    call="square",
)

pprint.pprint(sber_checker.run())
