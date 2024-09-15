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
            "отдел,бонус",
            "Продажи,14500",
            "Маркетинг,9700",
            "IT,20200",
            "Операции,4500"
        ]
    },
]

precode = """\n
...
with open('employee_bonuses.csv', 'r', encoding='utf-8') as f:
    saved_employee_bonuses = f.read()
    
"""
postcode = """\n
...
with open('department_bonuses.csv', 'r', encoding='utf-8') as f:
    print(f.read())

with open('department_bonuses.csv', 'w', encoding='utf-8') as f:
    f.write('')

with open('employee_bonuses.csv', 'w', encoding='utf-8') as f:
    f.write(saved_employee_bonuses)
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    precode=precode,
    postcode=postcode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
