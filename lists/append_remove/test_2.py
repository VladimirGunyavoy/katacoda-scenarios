import pprint

from checker import SberChecker


def should_include(code):
    return "remove" in code and "append" in code


tests = [{
    "input": ["Даниил", "Роксана"],
    "output": [
        "['Алексей', 'Алёна', 'Лариса', 'Тимошка', 'Роксана']"
    ]
}]

checker = SberChecker(
    filename="task_2.py",
    tests=tests,
    should_include=should_include
)

results = checker.run()

pprint.pprint(results)
