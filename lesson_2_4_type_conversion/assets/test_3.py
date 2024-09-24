import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': [],
        'output': ['3.0']
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include='burger_price_float_int_float = int(burger_price_float_int)',
    should_include_message='не обнаружено корректного создания переменной burger_price_float_int_float'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
