import csv

csv_path = input()

file = open(csv_path, mode='r', encoding='utf-8')
reader = csv.DictReader(file)
file.close()

# ваш код
...