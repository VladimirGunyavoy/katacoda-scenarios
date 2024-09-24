import json

from checker import SberChecker


filename = 'step_3.py'

my_tests = [
    {
        'input': [],
        'output':["Теплая одежда: 2", "Такси: 1"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'taxi' in code and 'warm_clothes' in code,
    should_include_message='не обнаружено переменных taxi и warm_clothes'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)



