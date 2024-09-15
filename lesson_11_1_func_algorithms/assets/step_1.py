employees = [
    {"name": "Алексеев", "rate": 8},
    {"name": "Галиулин", "rate": 8},
    {"name": "Павлов", "rate": 6},
    {"name": "Шмелев", "rate": 3},
    {"name": "Шакирова", "rate": 4},
    {"name": "Хасанов", "rate": 5},
]


def get_loyalty(number):
    if 0 < number < 6:
        return "low"
    elif 6 <= number < 8:
        return "medium"
    elif 8 <= number <= 10:
        return "high"

    return "Неверная оценка"


high = []
medium = []
low = []

# Ваш код
...




# Код для проверки
print(high)
print(medium)
print(low)
