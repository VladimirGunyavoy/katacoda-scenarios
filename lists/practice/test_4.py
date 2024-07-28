import pprint

from checker import SberChecker

tests = [
    {
        "input": ['8'],
        "output": ["Осталось 3 ч", "Осталось 2 ч", "Осталось 1 ч", "Осталось 0 ч", "Осталось 1 ч"],
    },
    {
        "input": ['6'],
        "output": ["Осталось 1 ч", "Осталось 0 ч", "Осталось 0 ч", "Осталось 0 ч", "Осталось 0 ч"],
    },
]

checker = SberChecker(
    filename="task_4.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
