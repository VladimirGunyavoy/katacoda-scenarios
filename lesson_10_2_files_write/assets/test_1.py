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
            "Прежде чем Вы примете решение об участии в этом исследовании, мы бы хотели предоставить Вам информацию об этом исследовании и возможных рисках."
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    postcode="research_introduction()"
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
