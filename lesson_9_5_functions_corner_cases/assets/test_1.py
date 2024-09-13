import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "args": [100_000, 100],
        "return": 140000
    },
    {
        "args": [20_000, 0],
        "return": 20000
    },
    {
        "args": [200_000, 150],
        "return": 320000
    },
    {
        "args": [120_000, 80],
        "return": 144000
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="get_bonus",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
