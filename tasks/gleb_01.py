"""
Напишите функцию print_approved_requests(all_requests) для отображения текущего списка покупок в виде словаря,
выведите названия всех товаров для офиса которые нужно передать в ближайшую закупку.
 Функция получает на вход список словарей формата:
"""

def print_approved_requests(arg):
    for i in arg:
        if i['approved']:
            print(i['name'])
