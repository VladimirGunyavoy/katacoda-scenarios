import pprint
from checker import SberChecker
from pathlib import Path
# import numpy as np
import os
import json

# os.chdir('framework_test/assets')
#print(os.getcwd())

filename = 'step.py'


my_tests = [{'input': ['3', '4'], 'output':[str(7)]}]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()
res['Test 1']['passed'] = True

json_res = json.dumps(res, indent=4)

print(json_res)



