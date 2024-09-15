import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": [f"step_3_feedback1.txt"],
        "output": [
            "Средняя: 3.0",
            "Доля 5: 25%"
        ]
    },
    {
        "input": [f"step_3_feedback2.txt"],
        "output": [
            "Средняя: 3.4",
            "Доля 5: 20%"
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
