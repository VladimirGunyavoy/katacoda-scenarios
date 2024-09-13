import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

elements = [
    {"id": 1, "value": "red"},
    {"id": 2, "value": "green"},
    {"id": 3, "value": "blue"},
]

my_tests = [
    {
        "args": [elements, 2],
        "return": {
            "id": 2,
            "value": "green"
        }
    },
    {
        "args": [elements, 3],
        "return": {
            "id": 3,
            "value": "blue"
        }
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="get_by_id",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
