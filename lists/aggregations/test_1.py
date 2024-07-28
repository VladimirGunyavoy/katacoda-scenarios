import pprint

from checker import SberChecker


tests = [{
    "input": [],
    "output": ["15%"],
}]

checker = SberChecker(
    filename="task_1.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
