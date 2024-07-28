import pprint

from checker import SberChecker


tests = [{
    "input": [],
    "output": ["095% Мария", "094% Алексей", "093% Светлана"],
}]

checker = SberChecker(
    filename="task_3.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
