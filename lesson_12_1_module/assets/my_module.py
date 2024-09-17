def my_mean(my_lst):
    # буфер под сумму
    my_sum = 0

    # длина списка
    my_n = len(my_lst)

    # для каждого числа в списке
    for number in my_lst:
        # складываем в буфер число
        my_sum += number

    # делим сумму на длину списка
    mean = my_sum / my_n

    return mean


def my_max(my_list):
    # помещаем первый элемент как рекорд
    record = my_list[0]

    # для каждого элемента кроме первого
    for element in my_list[1:]:
        # если элемент больше рекорда,
        if element > record:
            # то он новый рекорд
            record = element

    return record


def my_min(my_list):
    # помещаем первый элемент как рекорд
    record = my_list[0]

    # для каждого элемента кроме первого
    for element in my_list[1:]:
        # если элемент меньше рекорда,
        if element < record:
            # то он новый рекорд
            record = element

    return record
