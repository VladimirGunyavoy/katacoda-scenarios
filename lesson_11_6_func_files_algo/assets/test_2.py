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
            "Средняя оценка: 3.38",
            "Процент оценок 5: 25.00%",
            "",
            "Позитивные комментарии:",
            "Отличное обслуживание!",
            "Все нормально.",
            "Все супер!",
            "Удовлетворительно.",
            "",
            "Негативные комментарии:",
            "Могло бы быть и лучше.",
            "Совсем не понравилось.",
            "Требуется улучшение.",
            "Не очень."
        ]
    }
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
