import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'filename.py'

my_tests = [
    {
        "input": [],
        "output": [
            "2021",
            "new clients per month",
            "[49, 56, 53, 36, 65, 59, 52, 45, 59, 41, 55, 62]",
            "mean:  52.7",
            "min:   36",
            "max:   65",
            "",
            "2022",
            "new clients per month",
            "[40, 28, 29, 30, 58, 67, 38, 33, 23, 12, 24, -11]",
            "mean:  30.9",
            "min:   -11",
            "max:   67",
            "",
            "2023",
            "new clients per month",
            "[56, 63, 66, 51, 58, 66, 59, 59, 62, 49, 58, 68]",
            "mean:  59.6",
            "min:   49",
            "max:   68"
        ]
    },
]

postcode = """\n
...
with open('report.txt', 'r') as file:
    print(file.read())
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    postcode=postcode,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
