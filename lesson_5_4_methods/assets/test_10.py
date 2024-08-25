import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ['Дима', 'Маша', 'Иван', 'Евгения'],
        'output': [
            "На сегодняшней встрече со стороны подрядчика присутствуют следующие специалисты:",
            "Дима — менеджер проекта, основной канал коммуникации.",
            "Маша — лучший дизайнер компании.",
            "За разработку приложения отвечает старший разработчик Иван.",
            "Пиаром будет заниматься Евгения — специалист, обладающий весьма нестандартным и успешным подходом к решению проблем."
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
