import pprint

from checker import SberChecker

sber_checker = SberChecker(
    filename="../tasks/step_0.py",
    tests=[
        {"input": [4], "output": [16]},
        {"input": [2], "output": [4]},
        {"input": [0], "output": [0]}
    ],
    call="square",
)

pprint.pprint(sber_checker.run())
