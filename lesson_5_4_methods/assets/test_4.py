import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ['получилось плохо'],
        'output': ['получилось не так хорошо, как бывало']
    },
    {
        'input': ['что вышло то вышло'],
        'output': ['что вышло то вышло']
    },
    {
        'input': ['У меня сегодня так плохо с настроением, что даже мой будильник решил не звонить!'],
        'output': ['У меня сегодня так получилось не так хорошо, как бывало с настроением, что даже мой будильник решил не звонить!']
    },
    {
        'input': ['Я так хорошо поел, что теперь могу выступать в роли живого дивана!'],
        'output': ['Я так хорошо поел, что теперь могу выступать в роли живого дивана!']
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
