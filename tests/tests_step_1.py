import pprint

from checker import SberChecker

sber_checker = SberChecker(
    filename="../tasks/step_1.py",
    tests=[
        {"input": [[1, 2, 3]], "output": [3]},
        {"input": [[-3, -2, -1]], "output": [-1]},
        {"input": [[0]], "output": [0]}
    ],
    call="get_last"
)

pprint.pprint(sber_checker.run())
