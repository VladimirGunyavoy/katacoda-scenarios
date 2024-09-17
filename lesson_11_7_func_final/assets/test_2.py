import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "args": [],
        "return": [
            "Как работать 4 часа в неделю",
            "Как управлять своей жизнью",
            "Контент",
            "Маркетинг на 100%",
            "Метод пяти почему",
            "Психология влияния",
            "Сила воли"
        ]
    },

]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)


print(json_res)
