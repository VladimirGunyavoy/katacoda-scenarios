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
            "Высокий приоритет",
            "Реализовать форму входа",
            "",
            "Средний приоритет:",
            "Создать панель пользователя",
            "Добавить интеграцию платежного шлюза",
            "Оптимизировать процесс оплаты",
            "",
            "Низкий приоритет:",
            "Исправить проблемы с CSS на странице профиля",
            "Обновить интерфейс настроек пользователя",
            "Улучшить функционал восстановления пароля",
            "Улучшить дизайн истории транзакций",
            "Добавить поддержку нескольких языков",
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
