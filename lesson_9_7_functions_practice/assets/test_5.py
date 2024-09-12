import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'


my_tests = [
    {
        "args": [3000],
        "return": 390
    },
    {
        "args": [5_000_000],
        "return": 650000
    },
    {
        "args": [20_000_000],
        "return": 3000000
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="get_progressive_tax",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
