import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

precode = """\n
...
with open('purchases.csv', mode='r', encoding='utf-8') as file:
    saved_purchases = file.read()
    
"""

postcode = """
import csv

with open('average.csv', mode='r', encoding='utf-8') as file:
    print(file.read())
    
with open('average.csv', mode='w', encoding='utf-8') as file:
    file.write('')  

with open('purchases.csv', mode='w', encoding='utf-8') as file:
    file.write(saved_purchases)
"""

my_tests = [
    {
        "input": [],
        "output": [
            "month,average",
            "june,3520",
            "august,4020",
            "october,4020",
            "september,4360",
            "july,4860"
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    precode=precode,
    postcode=postcode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
