# employees = []

employees = [
    {"id": 1, "name": "Александр", "salary": 150_000},
    {"id": 2, "name": "Дарья", "salary": 130_000},
    {"id": 3, "name": "Лариса", "salary": 140_000},
]


def get_average_salary(employees):
    total = 0
    for one_employee in employees:
        total += one_employee["salary"]
    return round(total / len(employees))
