import os
os.chdir('/root')
print(os.getcwd())
import my_module as mm
inp = input()
print(mm.my_mean(inp))