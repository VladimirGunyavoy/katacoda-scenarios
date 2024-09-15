import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

precode = """\n
import csv

with open('employees.csv', mode='r', encoding='utf-8') as file:
    saved_employees = file.read()
    
with open('salary.csv', mode='r', encoding='utf-8') as file:
    saved_salary = file.read()

"""

postcode = """
...
with open('empoyees_full.csv', mode='r', encoding='utf-8') as file:
    data = file.read().splitlines()
    data.sort()
    print(data)

with open('empoyees_full.csv', mode='w', encoding='utf-8') as file:
    file.write('')

with open('employees.csv', mode='w', encoding='utf-8') as file:
    file.write(saved_employees)

with open('salary.csv', mode='w', encoding='utf-8') as file:
    file.write(saved_salary)
"""

my_tests = [
    {
        "input": [],
        "output": [
            "['full_name,profession,grade,salary', 'Аксель Игнатьев,backend,senior,110000', 'Вильгельм Казанцев,frontend,middle,105000', 'Герман Нестеров,designer,senior,130000', 'Дарина Максимова,backend,middle,135000', 'Злата Бурова,qa,middle,125000', 'Ирина Альшевская,designer,middle,120000', 'Луиза Романовская,backend,middle,118000', 'Лукреция Миронова,qa,junior,95000', 'Марк Киселев,frontend,junior,90000', 'Полина Хрущева,product,junior,87000', 'Радомир Зеленский,product,senior,140000', 'Феликс Воронов,frontend,junior,95000']"
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    precode=precode,
    postcode=postcode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
