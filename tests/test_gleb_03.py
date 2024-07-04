import pprint

from checker import SberChecker


def solution(incomes, expenses):
    return sum(incomes + expenses)

sber_checker = SberChecker(
    filename="../tasks/gleb_03.py",
    tests=[
        {
            "args": [[5,5,5], [3,3,3]],
            "return": []
        },
    ],
    call="calculate_budget",
    solution=solution
)

result = sber_checker.run()
pprint.pprint(result)
