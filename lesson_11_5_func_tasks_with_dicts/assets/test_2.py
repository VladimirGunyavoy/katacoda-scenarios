import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

employees = [
    {
        "full_name": "Горюнова Василиса",
        "salary": 60000,
        "performance": 80
    },
    {
        "full_name": "Крылов Даниил",
        "salary": 90000,
        "performance": 100
    },
    {
        "full_name": "Миронов Кирилл",
        "salary": 110000,
        "performance": 70
    },
    {
        "full_name": "Борисова Полина",
        "salary": 94000,
        "performance": 100
    },
    {
        "full_name": "Кузнецова Эллада",
        "salary": 80000,
        "performance": 50
    }
]

my_tests = [
    {
        "args": [employees],
        "return": [
            {
                "full_name": "Горюнова Василиса",
                "bonus": 48000
            },
            {
                "full_name": "Крылов Даниил",
                "bonus": 90000
            },
            {
                "full_name": "Миронов Кирилл",
                "bonus": 77000
            },
            {
                "full_name": "Борисова Полина",
                "bonus": 94000
            },
            {
                "full_name": "Кузнецова Эллада",
                "bonus": 40000
            }
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call='calculate_all_bonuses',
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
