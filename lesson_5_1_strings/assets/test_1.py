import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': [],
        'output': ["м", "я", "г", "к", "и", "й"]
    },
]

def should_include(code):
    return 'my_string[' in code

    return
sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=should_include,
    should_include_message='не обнаружено экстракции символов из данной строки вида my_string[x]'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)


