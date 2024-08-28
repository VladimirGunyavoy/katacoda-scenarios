import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": [],
        "output": ["[{'name': 'Кросс-продажи с кино', 'ROI': 200.0}, {'name': 'Реклама на проездных', 'ROI': 150.0}, {'name': 'Сырки с промокодом', 'ROI': 1071.4}, {'name': 'Реклама на полу в метро', 'ROI': 166.7}]"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
