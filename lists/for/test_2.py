import pprint

from checker import SberChecker

tests = [{
    "input": [],
    "output": [
        "Алексей (frontend): 40",
        "Иван (frontend): 45",
        "Петр (frontend): 41",
    ],
}]

checker = SberChecker(
    filename="task_2.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
