import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ["текст из 20 символов"],
        'output': ["длина строки: 20"]
    },
    {
        'input': ["парасолька"],
        'output': ["длина строки: 7"]
    },
    {
        'input': ["двадцатичетырехбуквенное"],
        'output': ["длина строки: 24"]
    },
    {
        'input': [""],
        'output': ["длина строки: 0"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'len(' in code,
    should_include_message='не обнаружено использования функции len'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
