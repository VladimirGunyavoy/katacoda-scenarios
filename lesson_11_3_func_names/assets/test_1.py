import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": ["Михаил"],
        "output": ["М...л"]
    },
]


def should_include(code):
    if "hideName" in code:
        return False

    if "(s)" in code:
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

with open('result.txt', mode='w', encoding='utf-8') as file:
    file.write('')

print(json_res)
