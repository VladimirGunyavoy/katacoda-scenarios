import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': [3],
        'output': [
            "count 2",
            "count 7",
            "count 12",
            "count 14",
            "count 17",
            "count 22",
            "count 26",
            "count 32",
            "count 37",
            "идеально"
        ]
    },
    {
        'input': [111],
        'output': [
            "count 2",
            "count 5",
            "count 9",
            "count 11",
            "count 15",
            "count 19",
            "count 24",
            "count 26",
            "count 32",
            "count 34",
            "count 40",
            "превышение 3"
        ]
    },
]

precode = """
import random
random.seed(int(input()))
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    precode=precode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
