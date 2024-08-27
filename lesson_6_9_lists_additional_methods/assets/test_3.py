import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": ["75"],
        "output": ["Новикова Ольга 120%", "Васильев Константин 104%", "Морозова Алина 102%"]
    },
    {
        "input": ["82"],
        "output": [
            "Новикова Ольга 120%",
            "Васильев Константин 104%",
            "Морозова Алина 102%",
            "Федоров Михаил 102%",
            "Петрова Мария 99%",
        ]
    },
    {
        "input": ["100"],
        "output": [
            "Новикова Ольга 120%",
            "Васильев Константин 104%",
            "Морозова Алина 102%",
            "Федоров Михаил 102%",
            "Петрова Мария 99%",
            "Волков Роман 98%",
            "Мельникова Анна 98%",
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
