import os
import json
import re
import random

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests_1 = [
    {
        "input": ['data_1.csv'],
        "output": ["36"]
    },
]

my_tests_2 = []
N = 3

for i in range(N):
    nums = random.sample(range(1, 50), 5)
    res = min(nums)

    my_tests_2.append({'input': [nums], 'output':[str(res)]})

precode = '''\n
import sys

sys.path.insert(0, '/root')
'''


postcode = """\n
import my_module as mm
inp = input()
print(mm.my_min(inp))
"""

def should_include(code):
    lst = ['my_module', 'my_min', 'data_1.csv']
    prod = 1
    for name in lst:
        prod *= int(name in code)

    return bool(prod)

sber_checker_1 = SberChecker(
    filename=filename,
    precode=precode,
    tests=my_tests_1,
    should_include=should_include,
    should_include_message='Не обнаружены необходимый импорты'
)

sber_checker_2 = SberChecker(
    # filename='/usr/local/lib/empty.py',
    filename='empty.py',
    tests=my_tests_2,
    postcode=postcode,
)


res_1 = sber_checker_1.run()
res_1['Test 0'] = res_1.pop('Test 1')
res_2 = sber_checker_2.run()

res = {**res_1, **res_2}

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
