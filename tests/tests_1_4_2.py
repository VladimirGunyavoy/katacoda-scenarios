import pprint

from checker import SberChecker


sber_checker = SberChecker(
    filename="../tasks/lesson_1_part_4_problem_2.py",
    tests=[
        {
            "input": [],
            "output": ["Дует ли ветер: False"]
        },
    ]
)

result = sber_checker.run()
pprint.pprint(result)
