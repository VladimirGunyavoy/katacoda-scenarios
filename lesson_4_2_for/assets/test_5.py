import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

output = [f'номер этажа {s}' for s in range(1, 13)] + [f'номер этажа {s}' for s in range(14, 31)]

my_tests = [
    {
        'input': [],
        'output': output
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'for i in range(1, 31):' in code,
    should_include_message='что-то сломалось в задании цикла'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
