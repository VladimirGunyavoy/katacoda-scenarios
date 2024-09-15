import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

expenses_1 = [
    {"category": "Зарплата", "plan": 987000, "fact": 960000},
    {"category": "Аренда", "plan": 160000, "fact": 190000},
]

expenses_2 = [
    {"category": "Зарплата", "plan": 150000, "fact": 140000},
    {"category": "Аренда", "plan": 12000, "fact": 13000},
]


my_tests = [
    {
        "args": [expenses_1],
        "return": -3000
    },
    {
        "args": [expenses_2],
        "return": 9000
    },

]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="get_balance",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
