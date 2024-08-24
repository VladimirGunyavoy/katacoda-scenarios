import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ["1"],  # 1 1
        'output': ["coin 1: True", "coin 2: True", "", "берем"]
    },
    {
        'input': ["2"],  # 0 1
        'output': ["coin 1: False", "coin 2: True", "", "не берем"]
    },
    {
        'input': ["3"],  # 0 0
        'output': ["coin 1: False", "coin 2: False", "", "не берем"]
    },
]

precode = """
import numpy as np
np.random.seed(seed=int(input()))
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    precode=precode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)