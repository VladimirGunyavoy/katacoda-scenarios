import json

from checker import SberChecker


filename = 'step_3.py'

my_tests = [
    {
        'input': [],
        'output':["coin 1", "", "Барт берет Женю", "Локи берет молчаливого Вову"]
    },
    {
        'input': [],
        'output':["coin 0", "", "Барт берет молчаливого Вову", "Локи берет Женю"]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)



