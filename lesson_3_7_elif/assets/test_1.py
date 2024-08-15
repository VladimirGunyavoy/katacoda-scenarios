import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ["300"],
        'output': ["квартал 4"]
    },
    {
        'input': ["37"],
        'output': ["квартал 1"]
    },
    {
        'input': ["165"],
        'output': ["квартал 2"]
    },
    {
        'input': ["220"],
        'output': ["квартал 3"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
