import os


def replace_checker_content(root_dir, new_content):
    for root, dirs, files in os.walk(root_dir):
        if 'checker.py' in files:
            file_path = os.path.join(root, 'checker.py')
            with open(file_path, 'w') as f:
                f.write(new_content)
            print(f"Обновлен файл: {file_path}")


if __name__ == '__main__':
    with open('checker.py', 'r') as file:
        updated_checker = file.read()

    replace_checker_content('.', updated_checker)
