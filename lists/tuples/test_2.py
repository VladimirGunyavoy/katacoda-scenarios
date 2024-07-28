import pprint

from checker import SberChecker

tests = [{
    "input": [],
    "output": ['61%']
}]

checker = SberChecker(
    filename="task_2.py",
    tests=tests,
)

results = checker.run()

pprint.pprint(results)
