import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": [],
        "output": ["[{'name': 'Алексей', 'text': 'Игра неплохая, но много багов.', 'r': 3}, {'name': 'Иван', 'text': 'Неудобное управление. И вообще скучно.', 'r': 2}, {'name': 'Ольга', 'text': 'Много рекламы, не хватает контента.', 'r': 1}, {'name': 'Наталья', 'text': 'Средненькая игра, на один раз.', 'r': 3}, {'name': 'Дмитрий', 'text': 'Полностью разочарован, ждал большего', 'r': 2}, {'name': 'Светлана', 'text': 'Просто ужасно, игра не стоит денег.', 'r': 1}, {'name': 'Егор', 'text': 'Мне понравилось, хоть и не шедевр.', 'r': 3}]"],
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
