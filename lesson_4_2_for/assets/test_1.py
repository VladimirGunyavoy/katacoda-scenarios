import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': [],
        'output': [
            "Минут прошло 0",
            "Минут прошло 1",
            "Минут прошло 2",
            "Минут прошло 3",
            "Минут прошло 4",
            "Минут прошло 5",
            "Пора выключать"
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
