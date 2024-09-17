import csv


def load_data(file_path):
    ...
    return ...


def unique_books(all_books):
    ...

    return ...


# Код для проверки результата
file_path = "book_records.csv"
all_books = load_data(file_path)
unique_book_titles = unique_books(all_books)

for title in unique_book_titles:
    print(title)
