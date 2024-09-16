employees = [
    {
        "full_name": "Горюнова Василиса",
        "resource": 6
    },
    {
        "full_name": "Крылов Даниил",
        "resource": 12
    },
    {
        "full_name": "Миронов Кирилл",
        "resource": 8
    },
    {
        "full_name": "Борисова Полина",
        "resource": 2
    },
    {
        "full_name": "Кузнецова Эллада",
        "resource": 0
    }
]


def evaluate_task(employee, hours):
    if hours == 0:
        return None
    return employee["resorce"] / hours


def evaluate_task_by_all_employees(employees, hours):
    ...
    return ...

