import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': [178],
        'output': [
            "Restaurant rating: 15",
            "Restaurant rating: 72",
            "Restaurant rating: 60",
            "Restaurant rating: 83"
        ]
    },
    {
        'input': [2],
        'output': [
            "Restaurant rating: 8",
            "Restaurant rating: 12",
            "Restaurant rating: 11",
            "Restaurant rating: 47",
            "Restaurant rating: 22",
            "Restaurant rating: 95"
        ]
    },
    {
        'input': [8],
        'output': [
            "Restaurant rating: 30",
            "Restaurant rating: 48",
            "Restaurant rating: 49",
            "Restaurant rating: 17",
            "Restaurant rating: 25",
            "Restaurant rating: 91"
        ]
    },
    {
        'input': [9],
        'output': [
            "Restaurant rating: 60",
            "Restaurant rating: 79"
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
