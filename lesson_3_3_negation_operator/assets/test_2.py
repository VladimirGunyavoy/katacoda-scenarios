import json

from checker import SberChecker

filename = 'step_2.py'

my_tests = [
    {
        'input': ["11"],
        'output': ["coin 0", "", "designer:", "arial", "", "you", "times new roman"]
    },
    {
        'input': ["2"],
        'output': ["coin 1", "", "designer:", "times new roman", "", "you", "arial"]
    },
]

precode = """
import random
random.seed(int(input()))
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
