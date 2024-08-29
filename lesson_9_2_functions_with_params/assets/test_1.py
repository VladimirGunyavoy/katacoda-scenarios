import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": [],
        "output": [
            "Уважаемый Михаил, спасибо за ваш интерес к позиции Электрик. К сожалению, на данный момент мы выбрали другого кандидата. Мы очень ценим ваше время и усилия и будем рады связаться с вами в будущем, если появятся новые возможности."
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    postcode="generate_rejection('Михаил', 'Электрик')"
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
