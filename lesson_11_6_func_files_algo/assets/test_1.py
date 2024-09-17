import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "args": ['customers_recent.txt', 'customers_old.txt'],
        "return": [
            "Baker",
            "Bishop",
            "Butler",
            "Ross"
        ]
    },

]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call='get_common_customers',
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

data = ['Ford', 'Cole', 'Baker', 'Bishop', 'Price', 'Ross', 'Butler']
with open('customers_old.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(data))

data = ['Ross', 'Henderson', 'Baker', 'Bishop', 'Butler']
with open('customers_recent.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(data))

print(json_res)
