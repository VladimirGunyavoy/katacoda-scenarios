import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ["2024", "3", "10"],
        'output': [
            "Введите начальный взнос: 2024", "Введите количество лет: 3", "Введите процентную ставку: 10",
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'input(' in code,
    should_include_message='не обнаружено использования функции input'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
