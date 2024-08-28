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
            "[{'name': 'Анна Кузнецова', 'activity': 'высокая'}, {'name': 'Борис Михайлов', 'activity': 'средняя'}, {'name': 'Виктория Соколова', 'activity': 'низкая'}, {'name': 'Георгий Иванов', 'activity': 'высокая'}, {'name': 'Елена Тихонова', 'activity': 'средняя'}, {'name': 'Дмитрий Никифоров', 'activity': 'низкая'}]"
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
