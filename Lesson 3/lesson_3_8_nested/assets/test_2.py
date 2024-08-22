import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ["1", "0", "1"],
        'output': [
            "Зарплата выше 500 000?",
            "1 — да, 0 — нет",
            "Добираться больше одного часа?",
            "1 — да, 0 — нет",
            "Есть бесплатный кофе?",
            "1 — да, 0 — нет",
            "Принять оффер"
        ]
    },
    {
        'input': ["0", "0", "0"],
        'output': [
            "Зарплата выше 500 000?",
            "1 — да, 0 — нет",
            "Добираться больше одного часа?",
            "1 — да, 0 — нет",
            "Есть бесплатный кофе?",
            "1 — да, 0 — нет",
            "Отклонить оффер"
        ]
    },
    {
        'input': ["1", "1", "1"],
        'output': [
            "Зарплата выше 500 000?",
            "1 — да, 0 — нет",
            "Добираться больше одного часа?",
            "1 — да, 0 — нет",
            "Есть бесплатный кофе?",
            "1 — да, 0 — нет",
            "Отклонить оффер"
        ]
    },
    {
        'input': ["1", "0", "0"],
        'output': [
            "Зарплата выше 500 000?",
            "1 — да, 0 — нет",
            "Добираться больше одного часа?",
            "1 — да, 0 — нет",
            "Есть бесплатный кофе?",
            "1 — да, 0 — нет",
            "Отклонить оффер"
        ]
    },
]

def should_include(code):
    return "elif " not in code

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=should_include,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
