import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "args": ["Хуан", "Лебедев", "Иванович"],
        "return": "Лебедев Хуан Иванович",
    },
    {
        "args": ["Иван", "Иванов"],
        "return": "Иванов Иван",
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="get_full_name",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
