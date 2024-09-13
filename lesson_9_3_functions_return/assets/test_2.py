import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "args": [250, 5],
        "return": 2.0
    },
    {
        "args": [1000, 21],
        "return": 2.1
    },
    {
        "args": [1234, 22],
        "return": 1.78
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="get_sales_conversion",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
