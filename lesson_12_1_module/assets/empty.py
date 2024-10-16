import os
os.chdir('/root')
import my_module as mm
inp = input()
print(mm.my_mean(inp))