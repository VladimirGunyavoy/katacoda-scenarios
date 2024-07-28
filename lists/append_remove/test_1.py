import pprint

from checker import SberChecker


tests = [{
    "input": ["Сходить в магазин", "Помыть посуду"],
    "output": [
        "['Планерка квартала', 'Курс по лидерству', 'Обед с коллегой', 'Сходить в магазин', 'Помыть посуду']"
    ]
}]

checker = SberChecker(
    filename="task_1.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
