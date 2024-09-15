import csv

csv_employees_path = input()
csv_salary_path = input()

file = open(csv_employees_path, mode='r', encoding='utf-8')
reader_employees = csv.DictReader(file)
file.close()

file = open(csv_salary_path, mode='r', encoding='utf-8')
reader_salaries = csv.DictReader(file)
file.close()

# ваш код
...