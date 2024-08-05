import pprint
from checker import SberChecker
from pathlib import Path
import numpy as np
import json

filename = 'step0.py'

N = 10
my_inputs = np.random.randint(0, 10, size=(N, 2))

print(my_inputs)

my_tests = []
for i in range(len(my_inputs)):
    print({'input': my_inputs[i], 'output':[str(sum(my_inputs[i]))]})
    my_tests.append({'input': (my_inputs[i]).astype(str).tolist(), 'output':[str(sum(my_inputs[i]))]})

# print(my_tests)

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()
# pprint.pprint(res)

json_res = json.dumps(res, indent=4)

print(json_res)


