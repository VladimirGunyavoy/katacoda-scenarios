import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

reviews = [
    {
        "name": "Анна",
        "grade": 8,
        "comment": "Хороший сервис, но хотелось бы больше удобных опций."
    },
    {
        "name": "Олег",
        "grade": 9,
        "comment": "Очень доволен, практически все устроило!"
    },
    {
        "name": "Ирина",
        "grade": 7,
        "comment": "Неплохо, но могли бы улучшить поддержку клиентов."
    },
    {
        "name": "Максим",
        "grade": 10,
        "comment": "Отлично! Воспользуюсь еще раз."
    },
    {
        "name": "Светлана",
        "grade": 6,
        "comment": "Средний опыт, есть куда расти."
    },
    {
        "name": "Дмитрий",
        "grade": 4,
        "comment": "Не совсем доволен, сталкивался с трудностями."
    }
]

my_tests = [
    {
        "args": [reviews],
        "return": [
            "Отлично! Воспользуюсь еще раз.",
            "Очень доволен, практически все устроило!",
            "Хороший сервис, но хотелось бы больше удобных опций."
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="sort_by_grade"
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
