import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ["1"],  # 6 4
        'output': ["dice 1: 6", "dice 2: 4", "", "fail"]
    },
    {
        'input': ["2"],  # 1 6
        'output': ["dice 1: 1", "dice 2: 6", "", "win"]
    },
    {
        'input': ["12"],  # 4 4
        'output': ["dice 1: 4", "dice 2: 4", "", "fail"]
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
