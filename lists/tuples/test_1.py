import pprint

from checker import SberChecker

tests = [{
    "input": [],
    "output": [
        'Всего этой неделе: 43.60',
        'Среднее на этой неделе: 7.27',
        'Всего на прошлой неделе: 38.30',
        'Среднее на прошлой неделе: 6.38',
    ]
}]

checker = SberChecker(
    filename="task_1.py",
    tests=tests,
)

results = checker.run()

pprint.pprint(results)
