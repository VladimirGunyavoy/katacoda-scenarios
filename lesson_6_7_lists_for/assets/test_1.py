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
            "Сделать KPI на второй квартал",
            "Встреча с аналитиками",
            "Презентация по работе в Q1",
            "Проверить отчеты команды",
            "Отправить задачу на оценку разработчикам"
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
