import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

vehicles = {
    'А123БВ77': 'Toyota Camry',
    'Е789КЛ79': 'Honda Civic',
    'М123ОР80': 'BMW 3 Series',
    'Н456ВР81': 'Mercedes-Benz C-Class',
    'Р789АК82': 'Audi A6',
}

my_tests = [
    {
        "input": [[vehicles]],
        "output": ["['А123БВ77', 'Е789КЛ79', 'М123ОР80', 'Н456ВР81', 'Р789АК82']"]
    },
]


def should_include(code):
    if "def names" in code:
        return False

    if "(avtomobili)" in code:
        return False

    return True


sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=should_include,
    should_include_message="Не изменено название функции либо аргумент!",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
