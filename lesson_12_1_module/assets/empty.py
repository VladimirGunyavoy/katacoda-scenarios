import sys

sys.path.insert(0, '/root')


import my_module as mm
inp = input()
print(mm.my_mean(inp))