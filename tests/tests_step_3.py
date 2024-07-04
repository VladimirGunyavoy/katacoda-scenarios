import pprint

from checker import SberChecker

sber_checker = SberChecker(
    filename="../tasks/step_3.py",
    tests=[
        {
            "input": ['arg1', 'arg2'],
            "output": ['arg1 arg2']
        },
        {
            "input": ['one', 'two', 'three', 'four'],
            "output": ['one two three four']
        }
    ],
    call="concat"
)

pprint.pprint(sber_checker.run())
