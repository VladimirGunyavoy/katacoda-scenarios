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
            "{'title': 'Как мыть руки', 'content': 'Руки нужно мыть тщательно...'}",
            "КАК ВЗЯТЬ ОТПУСК",
            "Каждому сотруднику полагается 35 дней отпуска в год. Чтобы уйти в отпуск, его нужно согласовать с руководителем..."
        ]
    },

]

postcode = """\n
print(get_article(all_articles, "как мыть руки"))
show_article(get_article(all_articles, 'Как взять отпуск'))
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    postcode=postcode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
