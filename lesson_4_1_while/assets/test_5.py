import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': [8],
        'output': [
            "размер очереди 10",
            "metal index 30",
            "thank you, goodbye",
            "",
            "размер очереди 9",
            "metal index 48",
            "thank you, goodbye",
            "",
            "размер очереди 8",
            "metal index 49",
            "thank you, goodbye",
            "",
            "размер очереди 7",
            "metal index 17",
            "thank you, goodbye",
            "",
            "размер очереди 6",
            "metal index 25",
            "thank you, goodbye",
            "",
            "размер очереди 5",
            "metal index 91",
            "",
            "размер очереди 5",
            "metal index 6",
            "thank you, goodbye",
            "",
            "размер очереди 4",
            "metal index 11",
            "thank you, goodbye",
            "",
            "размер очереди 3",
            "metal index 18",
            "thank you, goodbye",
            "",
            "размер очереди 2",
            "metal index 32",
            "thank you, goodbye",
            "",
            "размер очереди 1",
            "metal index 65",
            "",
            "размер очереди 1",
            "metal index 27",
            "thank you, goodbye"
        ]
    },
]

precode = """
import random
random.seed(int(input()))
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    precode=precode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
