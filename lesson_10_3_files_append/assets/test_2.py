import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": [
            "Дмитрий",
            "Екатерина",
            "Не выключает свет в переговорной после использования"
        ],
        "output": [
            "sender, employee, reason",
            "Оксана, Василий, Ворует у меня конфеты из ящика стола",
            "Дмитрий, Екатерина, Не выключает свет в переговорной после использования"
        ]
    },
]

precode = """\n
...
with open('complaints.txt', 'r', encoding='utf-8') as f:
    saved_complaints = f.read()

"""

postcode = """\n
...
with open('complaints.txt', 'r', encoding='utf-8') as f:
    print(f.read())

with open('complaints.txt', 'w', encoding='utf-8') as f:
    f.write(saved_complaints)
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    precode=precode,
    postcode=postcode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
