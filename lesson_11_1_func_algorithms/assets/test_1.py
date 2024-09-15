import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": [],
        "output": [
            "[{'name': 'Алексеев', 'rate': 8}, {'name': 'Галиулин', 'rate': 8}]",
            "[{'name': 'Павлов', 'rate': 6}]",
            "[{'name': 'Шмелев', 'rate': 3}, {'name': 'Шакирова', 'rate': 4}, {'name': 'Хасанов', 'rate': 5}]"
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
