import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

# ТЕСТЫ НЕ РАБОТАЮТ ДЛЯ ДАННОЙ ЗАДАЧИ
my_tests = [
    {
        "args": [],
        "return": [
            'average_rating: 3.38',
            'five_star_percent: 25.0',
            "positive_comments: ['Отличное обслуживание!','Все нормально.','Все супер!','Удовлетворительно.']",
            "negative_comments: ['Могло бы быть и лучше.',Совсем не понравилось.','Требуется улучшение.','Не очень.']"
        ]
    }
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
