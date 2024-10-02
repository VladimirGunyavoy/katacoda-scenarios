import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ['Геннадий', 'Александр', 'Борис'],
        'output': ['Геннадий, Александр, Борис.']
    },
    {
        "input": ["Екатерина", "Сергей", "Ольга"],
        "output": ["Екатерина, Сергей, Ольга."]
    },
    {
        "input": ["Дмитрий", "Анна", "Ирина"],
        "output": ["Дмитрий, Анна, Ирина."]
    },
    {
        "input": ["Максим", "Татьяна", "Виктор"],
        "output": ["Максим, Татьяна, Виктор."]
    },
    {
        "input": ["Наталья", "Павел", "Светлана"],
        "output": ["Наталья, Павел, Светлана."]
    }
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'f\'' in code,
    should_include_message='не обнаружено использования форматирования'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
