import pprint

from checker import SberChecker

sber_checker = SberChecker(
    filename="../tasks/step_with_inputs.py",
    tests=[
        {
            "input": ['Jason', 'Michael', 'John'],
            "output": ['Jason, Michael, John']
        },
    ]
)

pprint.pprint(sber_checker.run())