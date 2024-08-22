import numpy as np

N = 10
my_inputs = np.random.randint(0, 10, size=(N, 2))

# print(my_inputs)

my_tests = []


# f = open('tests_1.txt', 'w')

for i in range(len(my_inputs)):
    # print({'input': my_inputs[i], 'output':[str(sum(my_inputs[i]))]})
    my_tests.append({'input': (my_inputs[i]).astype(str).tolist(), 'output':[str(sum(my_inputs[i]))]})
    # f.write('input: ')
    # f.write(str((my_inputs[i]).astype(str).tolist()))
    # f.write(', ')
    # f.write('output: ')
    # f.write(str([str(sum(my_inputs[i]))]))
    # f.write('\n')
# print(my_tests)

f = open('tests_1.txt', 'w')
f.write(str(my_tests))