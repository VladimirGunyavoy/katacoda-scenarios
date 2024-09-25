import json

from checker import SberChecker


filename = 'step_3.py'

my_tests = [
    {
        'input': ["11"],
        'output':["coin 1", "", "Барт берет Женю", "Локи берет молчаливого Вову"]
    },
    {
        'input': ["2"],
        'output':["coin 0", "", "Барт берет молчаливого Вову", "Локи берет Женю"]
    },
]

precode = """
import random
random.seed(int(input()))
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    precode=precode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)



