import os
import json
import re
import random

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

nums_1 = random.sample(range(1, 50), 5)
res_1 = round(sum(nums_1), 2) / len(nums_1)

nums_2 = random.sample(range(1, 50), 5)
res_2 = round(sum(nums_2), 2) / len(nums_2)

nums_3 = random.sample(range(1, 50), 5)
res_3 = round(sum(nums_3), 2) / len(nums_3)

my_tests_1 = [
    {
        "input": ['data_1.csv'],
        "output": ['52.67']
    }
]

my_tests_2 = [
    {
        "input": [(nums_1)],
        "output": [str(res_1)]
    },
    {
        "input": [(nums_2)],
        "output": [str(res_2)]
    },
    {
        "input": [(nums_3)],
        "output": [str(res_3)]
    },
]

postcode = """\n
import my_module as mm
inp = input()
print(mm.my_mean(inp))
"""

sber_checker_1 = SberChecker(
    filename=filename,
    tests=my_tests_1,
)

sber_checker_2 = SberChecker(
    filename='/usr/local/lib/empty.py',
    tests=my_tests_2,
    postcode=postcode,
)


res_1 = sber_checker_1.run()
res_1['Test 0'] = res_1.pop('Test 1')

# os.chdir('/usr/local/lib')

res_2 = sber_checker_2.run()

res = res_1 | res_2

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)