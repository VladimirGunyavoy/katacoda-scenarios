import pprint

from checker import SberChecker

tests = [
    {
        "input": ['11:00'],
        "output": ['Иван'],
    },
    {
        "input": ['13:00'],
        "output": ['Петр'],
    },
    {
        "input": ['wrong time'],
        "output": [''],
    }
]

checker = SberChecker(
    filename="task_1.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
