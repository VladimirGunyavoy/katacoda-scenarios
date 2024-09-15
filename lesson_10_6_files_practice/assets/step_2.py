import csv


file = open('financial_budget.csv', mode='r', encoding='utf-8')
reader = csv.DictReader(file)

# ваш код
...


# Закрываем файл
file.close()
