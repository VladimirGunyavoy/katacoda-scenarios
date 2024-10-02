import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ['1001 + 2001 + 3001 + 4001'],
        'output': ['10004']
    },
    {
        'input': ['0 + 3000'],
        'output': ['3000']
    },
    {
        'input': ['1500 + 2500 + 3500'],
        'output': ['7500']
    },
    {
        'input': ['500 + 1500 + 2500'],
        'output': ['4500']
    },
    {
        'input': ['100 + 200 + 300 + 400'],
        'output': ['1000']
    }

]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
