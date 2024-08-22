import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ["0", "0", "0", "0", "0"],
        'output': ["Вы: Первичный бульон"]
    },
    {
        'input': ["0", "0", "0", "0", "1"],
        'output': ["Вы: Громоздкое четвероногое"]
    },
    {
        'input': ["0", "0", "0", "1", "0"],
        'output': ["Вы: Человек каменного века"]
    },
    {
        'input': ["0", "0", "1", "0", "0"],
        'output': ["Вы: Человек бронзового века"]
    },
    {
        'input': ["0", "1", "0", "0", "0"],
        'output': ["Вы: Человек индустриального века"]
    },
    {
        'input': ["1", "0", "0", "0", "0"],
        'output': ["Вы: Человек компьютерного века"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
