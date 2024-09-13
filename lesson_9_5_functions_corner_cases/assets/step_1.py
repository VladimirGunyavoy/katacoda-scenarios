def get_bonus(salary, performance=100):
    if performance >= 75:
        return salary * 1.2
    elif performance >= 100:
        return salary * 1.4
    elif performance >= 150:
        return salary * 1.6
    else:
        return salary

