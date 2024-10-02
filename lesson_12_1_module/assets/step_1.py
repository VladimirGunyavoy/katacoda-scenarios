import csv

print('hoi')

with open('data1.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        s = sum(map(int, lines)) / len(lines)

print(s)