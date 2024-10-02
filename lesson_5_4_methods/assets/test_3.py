import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ['В следующем квартале планируется использование скрама'],
        'output': ["скрам обнаружен. беги"]
    },
    {
        'input': ['Наша команда предпочитает вотерфлоу'],
        'output': ["скрам не обнаружен"]
    },
    {
        'input': ['В нашей команде активно используется Скрам для управления проектами.'],
        'output': ["скрам обнаружен. беги"]
    },

    {
        'input': ['Мы изучаем принципы скрам на нашем курсе.'],
        'output': ["скрам обнаружен. беги"]
    },

    {
        'input': ['Скрам позволяет нам быстро адаптироваться к изменениям.'],
        'output': ["скрам обнаружен. беги"]
    },
    {
        'input': ['Наша команда работает над новым проектом.'],
        'output': ["скрам не обнаружен"]
    },

    {
        'input': ['Мы используем разные методологии для управления задачами.'],
        'output': ["скрам не обнаружен"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
