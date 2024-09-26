import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

output = [f'число приседаний {s}' for s in range(24)]

my_tests = [
    {
        'input': [],
        'output': output
    },
]
def should_include(code):
    text = '''
for count in range(50):
    print('число приседаний', count)
    '''

    return text in code

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=should_include,
    should_include_message='что-то сломалось в задании цикла'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
