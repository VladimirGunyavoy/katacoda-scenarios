import pprint

from checker import SberChecker

postcode = """
print(', '.join(values))
"""

tests = [{
    "input": [],
    "output": ['Инновации, Дружелюбие, Идеальный сервис']
}]

checker = SberChecker(
    filename="task_1.py",
    tests=tests,
    postcode=postcode
)

results = checker.run()

pprint.pprint(results)
