import pprint

from checker import SberChecker

sber_checker = SberChecker(
    filename="../tasks/step_2.py",
    tests=[
        {
            "args": [],
            "return": 'Function without arguments'
        },
    ],
    call="func_without_arguments",
)

pprint.pprint(sber_checker.run())
