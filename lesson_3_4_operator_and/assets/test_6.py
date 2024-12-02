import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': [],
        'output': ["пора идти дальше"]
    },
]

def should_include(code):
    test_code = '''if not (a and b):
print('пора идти дальше')
else:
print('пока посидим тут')'''
    
    for line in test_code.split('\n'):
        if line not in code:
            return False
    return True
    

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=should_include,
    should_include_message='что-то случилось с первоначальным кодом, перезапустите задание'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)