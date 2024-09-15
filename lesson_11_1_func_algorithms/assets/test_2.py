import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

results = [
    {"employee": "Алексеев", "score": 82},
    {"employee": "Мельник", "score": 75},
    {"employee": "Соколова", "score": 91},
    {"employee": "Игнатьев", "score": 78},
    {"employee": "Петрова", "score": 85},
    {"employee": "Козлов", "score": 62}
]

my_tests = [
    {
        "args": [results],
        "return": [
            {
                "name": "Алексеев",
                "score": 82,
                "grade": 4
            },
            {
                "name": "Мельник",
                "score": 75,
                "grade": 3
            },
            {
                "name": "Соколова",
                "score": 91,
                "grade": 5
            },
            {
                "name": "Игнатьев",
                "score": 78,
                "grade": 3
            },
            {
                "name": "Петрова",
                "score": 85,
                "grade": 4
            },
            {
                "name": "Козлов",
                "score": 62,
                "grade": 2
            }
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call='detail_employee_results',
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
