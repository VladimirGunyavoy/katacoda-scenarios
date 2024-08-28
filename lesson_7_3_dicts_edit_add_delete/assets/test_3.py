import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": [],
        "output": ["26000000"]
    },
]

postcode = """
print(financial_plan.get('апрель'))
"""


sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    postcode=postcode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
