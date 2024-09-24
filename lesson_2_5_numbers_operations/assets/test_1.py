import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': [],
        'output': ["палочек на гостя: 2", "палочек осталось: 3"]
    },
]

def my_check(code):
    lst = ['//', '%']
    for word in lst:
        if word not in code:
            return False
    return True

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=my_check ,
    should_include_message='не обнаружено использования операций целочисленного деления и взятия остатка'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
