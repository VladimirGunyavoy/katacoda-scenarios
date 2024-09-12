import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

graphic = {"пн": True, "вт": False, "ср": False, "чт": True, "пт": True}

my_tests = [
    {
        "args": [graphic, "вт"],
        "return": "свободен"
    },
    {
        "args": [graphic, "чт"],
        "return": "занят"
    },
    {
        "args": [graphic, "пт"],
        "return": "занят"
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="is_free",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
