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
            "product, amount, total",
            "Кресло офисное, 1, 15000",
            "Лампа офисная, 2, 4000",
            "Стол большой рабочий, 1, 25000"
        ]
    },
]

precode = """\n
...
with open('today_report.txt', 'r', encoding='utf-8') as f:
    saved_today_report = f.read()
    
with open('sales_report.txt', 'r', encoding='utf-8') as f:
    saved_sales_report = f.read()

"""

postcode = """\n
...
with open('sales_report.txt', 'r', encoding='utf-8') as f:
    print(f.read())

with open('today_report.txt', 'w', encoding='utf-8') as f:
    f.write(saved_today_report)
    
with open('sales_report.txt', 'w', encoding='utf-8') as f:
    f.write(saved_sales_report)
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
