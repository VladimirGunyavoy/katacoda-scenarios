import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

employees_1 = [
    {"id": 1, "name": "Александр", "salary": 150_000},
    {"id": 2, "name": "Дарья", "salary": 130_000},
    {"id": 3, "name": "Лариса", "salary": 140_000},
]

employees_2 = []

my_tests = [
    {
        "args": [employees_1],
        "return": 140000
    },
    {
        "args": [employees_2],
        "return": 0
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="get_average_salary",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
