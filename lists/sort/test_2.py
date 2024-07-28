import pprint

from checker import SberChecker


tests = [{
    "input": [],
    "output": ["['Андрей_Андреев.odt', 'Иван_Иванов.docx', 'Мария_Смирнова.pages']"],
}]

checker = SberChecker(
    filename="task_2.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
