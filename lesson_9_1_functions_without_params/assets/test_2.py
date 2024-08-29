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
            "Вы попытались отправить сообщение, но по нашим данным вы находитесь в отпуске, и мы не разрешаем вам работать. Отдохните хорошенько и возвращайтесь к нам не раньше конца вашего отпуска."
        ],
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    postcode="holiday_block()"
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
