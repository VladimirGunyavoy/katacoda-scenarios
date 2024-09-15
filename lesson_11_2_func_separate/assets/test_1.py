import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "args": [[500, 700, 900], [300, 200, 100]],
        "return": 1500
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="calculate_and_record_budget",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

with open('result.txt', mode='w', encoding='utf-8') as file:
    file.write('')

print(json_res)
