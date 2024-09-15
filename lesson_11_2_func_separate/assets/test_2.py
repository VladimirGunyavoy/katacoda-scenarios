import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "args": [["Дамир Павлов", "Костя Шмелев", "Елена Шакирова", "Айрат Хасанов"]],
        "return": [
            "Павлов",
            "Шмелев",
            "Хасанов"
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call='filter_by_last_name',
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
