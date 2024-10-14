import os
import re

pattern = re.compile(r'^outro.md$')


def replace_content(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if pattern.match(file):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                if 'просвящаться' in content:
                    print(f"Файл: {file_path}")
                    content = content.replace('просвящаться', 'просвещаться')
                    with open(file_path, 'w') as f:
                        f.write(content)
                    print(f"Обновлен файл: {file_path}")


if __name__ == '__main__':
    replace_content('.')
