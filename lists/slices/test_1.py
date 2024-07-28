import pprint

from checker import SberChecker


tests = [{
    "input": [],
    "output": [
        "['09:50 Мельникова Анна', '09:55 Семенова Ирина', '09:57 Змеева Марина']"
    ]
}]

checker = SberChecker(
    filename="task_1.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
