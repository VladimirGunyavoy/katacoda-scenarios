import pprint

from checker import SberChecker


def solution(line):
    return line.lower().count("р")


sber_checker = SberChecker(
    filename="../tasks/07.py",
    tests=[
        {
            "input": ["Варежка"],
            "output": [],
        },
    ],
    call="count_r",
    solution=solution
)

result = sber_checker.run()
pprint.pprint(result)
