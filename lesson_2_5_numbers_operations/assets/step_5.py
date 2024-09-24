start = ... # Ваш код
years = ... # Ваш код
percent = ... # Ваш код

finish = round(start * (1 + percent) ** years, 2)

# вывод для проверки
print('Начальный взнос:', start)
print('Количество лет:', years)
print('Процентная ставка:', percent)
print('Итоговый баланс:', finish)