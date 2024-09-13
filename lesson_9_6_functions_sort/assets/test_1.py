import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

employees = [
    {"name": "Алиса", "months": 24},
    {"name": "Борис", "months": 12},
    {"name": "Василиса", "months": 36},
    {"name": "Даниил", "months": 6},
]

my_tests = [
    {
        "args": [employees],
        "return": ["Даниил", "Борис", "Алиса", "Василиса"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="return_names_by_months"
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
