import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

precode = """\n
...
with open("teambuilding_offers.csv", 'r', encoding='utf-8') as f:
    saved_data = f.read()
    
"""

postcode = """
...
with open("teambuilding_offers.csv", 'w', encoding='utf-8') as f:
    f.write(saved_data)
"""
my_tests = [
    {
        "input": [],
        "output": [
            "EventCo",
            "Dynamic Events",
            "Unlimited Adventures",
            "Synergy Getaways",
            "Peak Performance",
        ]
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    precode=precode,
    postcode=postcode
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
