import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

expenses = [
    {"category": "Зарплата", "value": 987000},
    {"category": "Аренда", "value": 160000},
    {"category": "Продвижение", "value": 350000},
]

my_tests = [
    {
        "args": [expenses],
        "return": [
            {'category': 'Зарплата', 'value': 0.66},
            {'category': 'Аренда', 'value': 0.11},
            {'category': 'Продвижение', 'value': 0.23}
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="get_expenses_stats",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
