# Текст шаблона
"""
Отправляю расчет премии за квартал.

У тебя {SALES} сделок на сумму {SUM} при плане в {PLAN}, твой план выполнен на {PERCENT}%. Твоя зарплата в этом квартале - {SALARY} в месяц, твоя премия - {BONUS}.
"""

employee_data = {
    "sales": 20,
    "sum": 1680000,
    "plan": 1500000,
    "percent": 110,
    "salary": 90000,
    "bonus": 120000
}


# Ваш код
def build_letter(employee_data):
    return ...
