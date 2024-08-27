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
            "Всего на этой неделе: 43.6",
            "Среднее на этой неделе: 7.3",
            "",
            "Всего на прошлой неделе: 38.3",
            "Среднее на прошлой неделе: 6.4",
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
