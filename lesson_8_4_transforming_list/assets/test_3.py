import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": [],
        "output": [
            "[{'name': 'Иван Иванов', 'total_salary': 60000}, {'name': 'Алексей Смирнов', 'total_salary': 100000}, {'name': 'Ольга Петрова', 'total_salary': 75000}, {'name': 'Мария Волкова', 'total_salary': 45000}, {'name': 'Дмитрий Сидоров', 'total_salary': 82000}]",
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
