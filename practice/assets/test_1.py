import os
import json
import re

from checker import SberChecker


filename = 'practice.py'

my_tests = [
    {
        'input': [],
        'output': ["Hello, world!"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()
res['Test 1']['passed'] = False

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
