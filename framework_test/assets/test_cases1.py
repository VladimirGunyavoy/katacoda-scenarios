import pprint
from checker import SberChecker
from pathlib import Path
import numpy as np
import os
import json

os.chdir('framework_test/assets')
print(os.getcwd())

filename = 'step0.py'

N = 3
my_inputs = np.random.randint(0, 10, size=(N, 2)).tolist()

my_tests = []
for i in range(len(my_inputs)):
    my_tests.append({'input': list(map(str, my_inputs[i])), 'output':[str(sum(my_inputs[i]))]})

# print(my_tests)

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4)

print(json_res)


