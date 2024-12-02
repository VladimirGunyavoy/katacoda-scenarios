print('Зарплата выше 500 000?')
print('1 — да, 0 — нет')
big_salary = int(input())

print('Добираться больше одного часа?')
print('1 — да, 0 — нет')
long_road = int(input())

print('Есть бесплатный кофе?')
print('1 — да, 0 — нет')
free_coffee = int(input())

# Ваш код


if not big_salary:
    print('Отклонить оффер')
else:
    if long_road:
        print('Отклонить оффер')
    else:
        if not free_coffee: 
            print('Отклонить оффер')
        else:
            print('Принять оффер')
    