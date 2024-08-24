import random

queue = 10

while queue > 0:
    print()
    print('размер очереди', queue)

    # задаем индекс металла случайно
    metal_index = random.randint(1, 100)
    print('metal index', metal_index)

    ### ваш код
    ...

    ### конец вашего кода

    # прощаемся и уменьшаем очередь
    print('thank you, goodbye')
    queue -= 1