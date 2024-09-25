import json

from checker import SberChecker

filename = 'step_1.py'

my_tests = [
    {
        'input': [],
        'output': ["glasses"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'sunny = True' in code,
    should_include_message='не обнаружено корректного создания переменной sunny'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
