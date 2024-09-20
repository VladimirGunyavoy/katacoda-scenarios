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
    should_include=lambda code: ".mean()" in code and ".min()" in code and ".max()" in code,
    should_include_message="Вы не использовали mean/min/max в вашем коде",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
