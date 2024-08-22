import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ["True", "True"],
        'output': ["Priority: 1"]
    },
    {
        'input': ["False", "True"],
        'output': ["Priority: 2"]
    },
    {
        'input': ["True", "False"],
        'output': ["Priority: 3"]
    },
    {
        'input': ["False", "False"],
        'output': ["Priority: 4"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
