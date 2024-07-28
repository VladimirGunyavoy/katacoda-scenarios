import pprint

from checker import SberChecker


tests = [{
    "input": [],
    "output": ["['1 Провести планирование с командой', '2 Провести интервью с кандидатом', "
              "'3 Пройти курс по лидерству']"],
}]

checker = SberChecker(
    filename="task_1.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
