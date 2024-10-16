import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        "input": [],
        "output": [""]
    },

]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    should_include=lambda code: "for i, year in" in code and "plt.subplot(1, 3" in code,
    should_include_message="Не обнаружено использования цикла 'for i, year in' и/или plt.subplot(1, 3, i+1) вашем коде",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
