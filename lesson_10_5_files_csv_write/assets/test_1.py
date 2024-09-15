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
            "дата,платформа,количество лайков,количество комментариев,количество репостов",
            "1 января 2024,телеграм,150,20,5",
            "3 января 2024,яндекс дзен,200,15,10",
            "5 января 2024,вконтакте,300,30,8",
            "7 января 2024,телеграм,180,25,6",
            "10 января 2024,яндекс дзен,220,18,12",
            "12 января 2024,вконтакте,350,40,15",
            "15 января 2024,телеграм,160,22,7",
            "18 января 2024,яндекс дзен,210,19,9",
            "20 января 2024,вконтакте,320,35,10",
            "23 января 2024,телеграм,170,23,8"
        ]
    },
]

postcode = """\n
...
with open('mediareport.csv', 'r', encoding='utf-8') as f:
    print(f.read())

with open('mediareport.csv', 'w', encoding='utf-8') as f:
    f.write('')
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    postcode=postcode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
