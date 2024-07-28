import pprint
from checker import SberChecker
from pathlib import Path
import numpy as np

filename = Path(__file__).parent.parent / 'tasks' / 'sum_a_b.py'

N = 2
my_inputs = np.random.randint(0, 10, size=(N, 2))

my_tests = []
for i in range(len(my_inputs)):
    input_list = my_inputs[i].tolist()
    my_tests.append({'input': input_list, 'output': [str(sum(input_list))]})

print(my_tests)

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)

pprint.pprint(sber_checker.run())