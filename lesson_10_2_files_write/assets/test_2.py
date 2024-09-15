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
            "Веретенников",
            "Златоручев",
            "Радостехин",
            "",
            "Листопадов",
            "Гроздокарпов",
            "Кристалвовский"
        ]
    },
]

postcode = """\n
...
with open('team_1.txt', 'r') as file:
    print(file.read())
    
with open('team_2.txt', 'r') as file:
    print(file.read())

with open('team_1.txt', 'w') as file:
    file.write("")

with open('team_2.txt', 'w') as file:
    file.write("")
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    postcode=postcode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
