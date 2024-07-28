import pprint

from checker import SberChecker


tests = [{
    "input": [],
    "output": [
        "Сделать KPI на второй квартал",
        "Встреча с аналитиками",
        "Презентация по работе в Q1",
        "Проверить отчеты команды",
        "Отправить задачу на оценку разработчикам",
    ],
}]

checker = SberChecker(
    filename="task_1.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
