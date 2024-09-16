import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

employees = [
    {
        "full_name": "Горюнова Василиса",
        "resource": 6
    },
    {
        "full_name": "Крылов Даниил",
        "resource": 12
    },
    {
        "full_name": "Миронов Кирилл",
        "resource": 8
    },
    {
        "full_name": "Борисова Полина",
        "resource": 2
    },
    {
        "full_name": "Кузнецова Эллада",
        "resource": 0
    }
]

my_tests = [
    {
        "args": [employees, 12],
        "return": [
            {
                "full_name": "Горюнова Василиса",
                "weeks": 2.0
            },
            {
                "full_name": "Крылов Даниил",
                "weeks": 1.0
            },
            {
                "full_name": "Миронов Кирилл",
                "weeks": 1.5
            },
            {
                "full_name": "Борисова Полина",
                "weeks": 6.0
            },
            {
                "full_name": "Кузнецова Эллада",
                "weeks": None
            }
        ]
    },
    {
        "args": [employees, 24],
        "return": [
            {
                "full_name": "Горюнова Василиса",
                "weeks": 4.0
            },
            {
                "full_name": "Крылов Даниил",
                "weeks": 2.0
            },
            {
                "full_name": "Миронов Кирилл",
                "weeks": 3.0
            },
            {
                "full_name": "Борисова Полина",
                "weeks": 12.0
            },
            {
                "full_name": "Кузнецова Эллада",
                "weeks": None
            }
        ]
    }
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call='evaluate_task_by_all_employees',
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
