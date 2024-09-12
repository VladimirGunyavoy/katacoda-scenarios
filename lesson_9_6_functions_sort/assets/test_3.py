import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

employees = [
    {"full_name": "Август Тарновский", "salary": 120000, "tax_rate": 0.2},
    {"full_name": "Божена Короленко", "salary": 150000, "tax_rate": 0.06},
    {"full_name": "Вилен Соколовский", "salary": 110000, "tax_rate": 0.06},
    {"full_name": "Глафира Коваль", "salary": 125000, "tax_rate": 0.17},
    {"full_name": "Дементий Яновский", "salary": 130000, "tax_rate": 0.2},
    {"full_name": "Евграф Вишневский", "salary": 140000, "tax_rate": 0.06},
    {"full_name": "Жанна Трофимова", "salary": 135000, "tax_rate": 0.17},
    {"full_name": "Злата Оводова", "salary": 145000, "tax_rate": 0.1},
    {"full_name": "Игнат Лазовский", "salary": 115000, "tax_rate": 0.13}
]


my_tests = [
    {
        "args": [employees],
        "return": [
            'Дементий Яновский',
            'Август Тарновский',
            'Жанна Трофимова',
            'Глафира Коваль',
            'Игнат Лазовский',
            'Злата Оводова',
            'Божена Короленко',
            'Евграф Вишневский',
            'Вилен Соколовский'
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="sort_by_tax"
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
