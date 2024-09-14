import os
import re

pattern = re.compile(r'^problem_\d+\.rego$')


def replace_rego_files(root_dir, new_content):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if pattern.match(file):
                file_path = os.path.join(root, file)
                with open(file_path, 'w') as rego_file:
                    rego_file.write(new_content)
                print(f"Обновлен файл: {file_path}")


if __name__ == '__main__':
    with open('step (1).rego', 'r') as f:
        new_rego_content = f.read()

    replace_rego_files('.', new_rego_content)
