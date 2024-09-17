import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'filename.py'

my_tests = [
    {
        "input": [],
        "output": ["36", "2"]
    },

]

postcode = """\n
from my_module import my_min

print(my_min([2, 4, 6, 8]))
"""

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    postcode=postcode,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
