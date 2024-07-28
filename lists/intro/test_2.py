import pprint

from checker import SberChecker

postcode = """
print(', '.join(day_1))
print(', '.join(day_2))
"""

tests = [{
    "input": [],
    "output": [
        "Блиц-аналитика, Продуктовые исследования, Как транслировать стратегию компании",
        "Гибридные методологии управления, OKR в управлении, Применение AI"
    ]
}]

checker = SberChecker(
    filename="task_2.py",
    tests=tests,
    postcode=postcode
)

results = checker.run()

pprint.pprint(results)
