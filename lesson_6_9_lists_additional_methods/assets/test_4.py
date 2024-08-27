import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": ["7"],
        "output": [
            "Осталось 0 ч",
            "Осталось 0 ч",
            "Осталось 0 ч",
            "Осталось 1 ч",
            "Осталось 0 ч",
        ]
    },
    {
        "input": ["5"],
        "output": [
            "Осталось 0 ч",
            "Осталось 1 ч",
            "Осталось 2 ч",
            "Осталось 3 ч",
            "Осталось 2 ч",
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
