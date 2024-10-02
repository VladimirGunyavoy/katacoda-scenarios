import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ['Арсений, Аркадий, Александр.'],
        'output': ['Арсений', 'Аркадий', 'Александр']
    },
    {
        'input': ['Дмитрий, Денис, Даниил.'],
        'output': ['Дмитрий', 'Денис', 'Даниил']
    },
    {
        'input': ['Мария, Мила, Маргарита.'],
        'output': ['Мария', 'Мила', 'Маргарита']
    },
    {
        'input': ['Сергей, Станислав, Святослав.'],
        'output': ['Сергей', 'Станислав', 'Святослав']
    }
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
