import pprint
from checker import SberChecker
from pathlib import Path
# import numpy as np
import json

filename = 'step0.py'

f = open('tests_1.txt')
my_tests = eval(f.read())

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()
# pprint.pprint(res)

json_res = json.dumps(res, indent=4)

print(json_res)


