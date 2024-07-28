import pprint

from checker import SberChecker

tests = [
    {
        "input": [250000],
        "output": ["осталось 45000.00"],
    },
    {
        "input": [20000],
        "output": ["лимит превышен"],
    }
]

checker = SberChecker(
    filename="task_2.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
