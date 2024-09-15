import csv

file = open('marketing_campaigns.csv', mode='r', encoding='utf-8')

reader = csv.DictReader(file)

# ваш код
...


# Закрываем файл
file.close()
