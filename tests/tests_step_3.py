import pprint

from checker import SberChecker

sber_checker = SberChecker(
    filename="../tasks/step_3.py",
    tests=[
        {
            "args": ['arg1', 'arg2'],
            "return": 'arg1 arg2'
        },
        {
            "args": ['one', 'two', 'three', 'four'],
            "return": 'one two three four'
        }
    ],
    call="concat"
)

pprint.pprint(sber_checker.run())
