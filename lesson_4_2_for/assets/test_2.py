import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

output = [f'Секунд прошло {s}' for s in range(301)] + ['Пора выключать']

my_tests = [
    {
        'input': [],
        'output': output
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'for' in code and 'while' not in code,
    should_include_message='необходимо использовать цикл for, а не while'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
