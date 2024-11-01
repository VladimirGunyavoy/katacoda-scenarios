import os

# os.chdir('python1')
x = os.listdir()
# print(os.getcwd())
# only_files = [i if os.path.isfile(i) and i[-5:] == 'ipynb' else pass for i in x]

nbs = []
for i in x:
    if os.path.isfile(i) and i[-5:] == 'ipynb':
        nbs.append(i)


print()
print(nbs)
print()
