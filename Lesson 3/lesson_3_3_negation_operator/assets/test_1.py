import json

from checker import SberChecker


filename = 'step_1.py'

my_tests = [
    {
        'input': ["2"],
        'output':["coin 0", "True"]
    },
    {
        'input': ["11"],
        'output':["coin 1", "False"]
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



