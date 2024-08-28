import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": [],
        "output": ["[{'full_name': 'Сергей Петров', 'experience': 4, 'salary': 95000}, {'full_name': 'Мария Сидорова', 'experience': 3, 'salary': 85000}]"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
