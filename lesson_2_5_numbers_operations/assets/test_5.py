import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ["100", "10", "0.1"],
        'output': [
            "Начальный взнос: 100",
            "Количество лет: 10",
            "Процентная ставка: 0.1",
            "Итоговый баланс: 259.37"
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'float(' in code,
    should_include_message='не обнаружено использования функции float'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
