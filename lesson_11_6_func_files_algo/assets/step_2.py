def load_comments():
    import csv
    ...

    return comments


def print_sorted_comments(all_comments):
    positive_comments = []
    negative_comments = []

    avg_rating = ...
    five_star_percent = ...

    # Код печати результатов, для формирования правильного вывода
    print(f"Средняя оценка: {avg_rating:.2f}")
    print(f"Процент оценок 5: {five_star_percent:.2f}%")
    print("\nПозитивные комментарии:")
    [print(comment) for comment in positive_comments]
    print("\nНегативные комментарии:")
    [print(comment) for comment in negative_comments]


# Код для проверки, не удаляйте его
comments = load_comments()
print_sorted_comments(comments)
