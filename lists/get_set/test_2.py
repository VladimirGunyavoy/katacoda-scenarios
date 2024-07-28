import pprint

from checker import SberChecker


def should_include(code):
    return "NPS: 36" in code and "results[0]" in code


tests = [{
    "input": [],
    "output": ["NPS: 42", "LTV: 25000"]
}]

checker = SberChecker(
    filename="task_2.py",
    tests=tests,
    should_include=should_include
)

results = checker.run()

pprint.pprint(results)
