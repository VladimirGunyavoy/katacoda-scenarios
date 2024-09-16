import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "args": [["sasha@microminds.ru", "eva@retarded.ru", "veronica@dolt.io", "ivan@retarded.ru"]],
        "return": {
            'microminds': ['sasha@microminds.ru'],
            'retarded': ['eva@retarded.ru', 'ivan@retarded.ru'],
            'dolt': ['veronica@dolt.io']
        }
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call='organize_emails',
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
