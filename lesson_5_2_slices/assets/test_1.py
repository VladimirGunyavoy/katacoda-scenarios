import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': [],
        'output': ["француз"]
    },
]


def should_include(code):
    import re

    # Регулярное выражение для поиска my_string[число:число] или my_string[текст:текст]
    pattern = r'my_string\[(\d+|[a-zA-Z]+):(\d+|[a-zA-Z]+)\]'

    # Функция для проверки текста
    return bool(re.search(pattern, code))

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=should_include,
    should_include_message='не обнаружено экстракции символов с помощью срезов'
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)