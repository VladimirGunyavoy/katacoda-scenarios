import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ["0"],  # 4 4
        'output': ["dice 1: 4", "dice 2: 4", "", "fail"]
    },
    {
        'input': ["1"],  # 2 5
        'output': ["dice 1: 2", "dice 2: 5", "", "win"]
    },
    {
        'input': ["5"],  # 5 3
        'output': ["dice 1: 5", "dice 2: 3", "", "win"]
    },
    {
        'input': ["18"],  # 2 1
        'output': ["dice 1: 2", "dice 2: 1", "", "win"]
    },
    {
        'input': ["13"],  # 3 3
        'output': ["dice 1: 3", "dice 2: 3", "", "fail"]
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
