import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": ["step_2_data1.txt"],
        "output": [
            "Иванов Иван Разработчик",
            "Сидоров Сергей Администратор",
            "Смирнова Анна Аналитик",
            "270 мин"
        ]
    },
    {
        "input": ["step_2_data2.txt"],
        "output": [
            "Петров Петр Тестировщик",
            "Кузнецов Алексей Менеджер проекта",
            "Васильева Мария Дизайнер",
            "Медведев Арсений Разработчик",
            "258 мин"
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
