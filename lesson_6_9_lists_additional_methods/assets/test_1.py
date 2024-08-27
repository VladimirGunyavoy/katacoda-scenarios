import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": ["15:00"],
        "output": ["Алексей"]
    },
    {
        "input": ["11:00"],
        "output": ["Иван"]
    },
    {
        "input": ["23:00"],
        "output": [""]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
