"""
На работу в офис нужно приходить к 9:00.
У вас есть список сотрудников, отсортированный по времени прихода на работу.
Выведите трех человек, которые пришли последними:

Исходный код:

check_in_time = {
    "09:20 Новикова Ольга",
    "09:25 Васильев Константин",
    "09:30 Морозова Алина",
    "09:35 Федоров Михаил",
    "09:40 Петрова Мария",
    "09:45 Волков Роман",
    "09:50 Мельникова Анна",
    "09:55 Семенова Ирина",
    "09:57 Змеева Марина"
}
"""

""" Выполненное задание """

check_in_time = [
    "09:20 Новикова Ольга",
    "09:25 Васильев Константин",
    "09:30 Морозова Алина",
    "09:35 Федоров Михаил",
    "09:40 Петрова Мария",
    "09:45 Волков Роман",
    "09:50 Мельникова Анна",
    "09:55 Семенова Ирина",
    "09:57 Змеева Марина"
]

print(check_in_time[-3:])