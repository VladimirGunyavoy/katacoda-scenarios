import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': [],
        'output': ["стоимость кофе: 1.99", 
                   "стоимость пончика: 2.49", 
                   "общая стоимость: 4.48",
                   "общая стоимость со скидкой: 3.61"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'cost -= discount' in code,
    should_include_message='не обнаружено корректного изменения переменной cost. необходимый формат: переменная -= переменная'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
