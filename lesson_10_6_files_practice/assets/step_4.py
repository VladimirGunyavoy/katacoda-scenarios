import csv

csv_purchases_path = input()

file = open(csv_purchases_path, mode='r', encoding='utf-8')
reader = csv.DictReader(file)
file.close()

# ваш код
...