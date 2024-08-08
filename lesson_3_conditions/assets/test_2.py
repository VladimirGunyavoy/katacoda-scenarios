import json

from checker import SberChecker


filename = 'step_2.py'

my_tests = [
    {
        'input': [],
        'output':["до оператора if", "после оператора if"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4)

print(json_res)



