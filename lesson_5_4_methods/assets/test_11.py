import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'

my_tests = [
    {
        'input': ['file_1.txt'],
        'output': ['C:\\Users\\Ivan\\Desktop\\Secrets\\file_1.txt']
    },

    {
        "input": ["file_2.txt"],
        "output": ["C:\\Users\\Ivan\\Desktop\\Secrets\\file_2.txt"]
    },

    {
        "input": ["document.pdf"],
        "output": ["C:\\Users\\Ivan\\Desktop\\Secrets\\document.pdf"]
    },


    {
        "input": ["image.png"],
        "output": ["C:\\Users\\Ivan\\Desktop\\Secrets\\image.png"]
    },

    {
        "input": ["notes.docx"],
        "output": ["C:\\Users\\Ivan\\Desktop\\Secrets\\notes.docx"]
    },

]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
