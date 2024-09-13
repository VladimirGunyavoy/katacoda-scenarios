import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "args": [8000],
        "return": 1000
    },
    {
        "args": [14000, 6],
        "return": 2333
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="count_hour_rate",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
