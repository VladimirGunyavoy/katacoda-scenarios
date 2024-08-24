import os
import json
import re
from datetime import datetime

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

day_now = datetime.now().day
month_now = datetime.now().month
year_now = datetime.now().year

my_tests = [
    {
        'input': [],
        'output': [f"day: {day_now}", f"month: {month_now}", f"year: {year_now}"],
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
