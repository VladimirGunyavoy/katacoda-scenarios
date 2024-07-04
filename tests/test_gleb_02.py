import pprint

from checker import SberChecker

tests = [
    {
        "args": [100, 10],
        "return": 10
    }

]
sber_checker = SberChecker(
    filename="../tasks/gleb_02.py",
    tests=tests,
    call="get_tax"
)

result = sber_checker.run()
pprint.pprint(result)
