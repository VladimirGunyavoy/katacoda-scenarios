import os
import json
import re
from datetime import datetime

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

day_now = datetime.now().day

my_tests = [
    {
        'input': [],
        'output': [f'day: {day_now}'],
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'day = ' in code or 'day=' in code,
    should_include_message='Не обнаружено использования переменной day'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
