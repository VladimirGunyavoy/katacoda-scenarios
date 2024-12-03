import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

elements = [
    {"id": 1, "value": "red"},
    {"id": 2, "value": "green"},
    {"id": 3, "value": "blue"},
]

my_tests = [
    {
        "args": [elements, 2],
        "return": {
            "id": 2,
            "value": "green"
        }
    },
    {
        "args": [elements, 3],
        "return": {
            "id": 3,
            "value": "blue"
        }
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="get_by_id",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

dct = json.loads(json_res)

for test in dct:
    print(test)
    print(dct[test])
    print()
    for res in dct[test]:
        if res == 'input':
            
            # print(res)
            dct[test][res][0] = str(dct[test][res][0])
            
        # print(res)
        if res == 'expected':
            # print(res)
            # dct[test][res] = str(dct[test][res])
            # print(dct[test][res])
            
            dct[test][res][0] = str(dct[test][res][0])
            print(dct[test][res])
            # print(dct[test][res])
        
            # print(dct[test][res])
        
        
        # for el in dct[test][res]:
        #     print(el)
# print(json_res)

print(dct)

json_res = json.dumps(dct, indent=4, ensure_ascii=False)

print(json_res)