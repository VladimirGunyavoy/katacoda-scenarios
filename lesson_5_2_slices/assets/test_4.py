import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': [],
        'output': ["хочется кушать!"]
    },
]


def should_include(code):

    pattern = r'my_string\[(?P<x>-?\d*):(?P<y>-?\d*):(?P<z>-?\d*)\]'
    matches = re.finditer(pattern, code)
    return any(matches)
    
sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=should_include,
    should_include_message='не обнаружено корректной экстракции с помощью срезов'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
