import os
import json
import re
from datetime import datetime

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

month_now = datetime.now().month

my_tests = [
    {
        'input': [],
        'output': [f'month: {month_now}'],
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: 'month = ' in code or 'month=' in code,
    should_include_message='Не обнаружено использования переменной month'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
