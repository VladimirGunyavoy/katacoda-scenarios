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
            "['Блиц-аналитика', 'Продуктовые исследования', 'Impact гипотез: как строить прогноз доходности?', 'Как транслировать стратегию компании']",
            "['MVP-тестирование. На что обратить внимание', 'Гибридные методологии управления', 'Аналитика и метрики в управлении продуктом', 'Применение AI в Product Management']"
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    postcode="\nprint(day_1)\nprint(day_2)"
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
