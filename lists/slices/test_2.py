import pprint

from checker import SberChecker


tests = [{
    "input": [],
    "output": [
        "['AlphaTech Innovations', 'BetaBuild Solutions', "
        "'GammaWave Industries', 'Delta Dynamics', 'Epsilon Enterprises']"
    ]
}]

checker = SberChecker(
    filename="task_2.py",
    tests=tests
)

results = checker.run()

pprint.pprint(results)
