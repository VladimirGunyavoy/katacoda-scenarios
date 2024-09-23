import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_1.py'

my_tests = [
    {
        'input': [],
        'output': []
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'number of trees = 10' in code,
    should_include_message='не обнаружено создания переменной trees_number. \nКомментарий: формат должен быть ИМЯ_ПЕРЕМЕННОЙ = ЗНАЧЕНИЕ.'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
