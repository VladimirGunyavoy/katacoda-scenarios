# Список измерений дневной температуры за сутки
temp_measurements = [23, 27, 25, 22, 17, 15, 16, 12]

# Сортируем список температур
sorted_temp = sorted(temp_measurements)

# Получаем минимальную и максимальную температуры
min_temp = temp_measurements[0]
max_temp = temp_measurements[-1]

# Вычисляем разницу между максимальной и минимальной температурами
temp_difference = max_temp - min_temp

# Выводим результат
print(f'{temp_difference} градусов')