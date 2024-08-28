import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": [],
        "output": ["[{'name': 'Task 1', 'is_priority': False}, {'name': 'Task 2', 'is_priority': True}, {'name': 'Task 3', 'is_priority': False}, {'name': 'Task 4', 'is_priority': True}, {'name': 'Task 5', 'is_priority': False}]"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
