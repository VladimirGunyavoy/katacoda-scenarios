import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ['2 + 3'],
        'output': ['pass']
    },
    {
        'input': ['sum(2, 3)'],
        'output': ['+ not included']
    },
    {
        'input': ['asdg + sgdh'],
        'output': ['pass']
    },
    {
        'input': ['просто какое-то текст'],
        'output': ['+ not included']
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
