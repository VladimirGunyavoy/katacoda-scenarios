import os
import json
import re

from checker import SberChecker

index = re.search(r'\d+', os.path.basename(__file__)).group()

filename = f'step_{index}.py'


employee_data = {
    "sales": 10,
    "sum": 1200000,
    "plan": 1000000,
    "percent": 120,
    "salary": 100000,
    "bonus": 25000
}


my_tests = [
    {
        "args": [employee_data],
        "return": f"Отправляю расчет премии за квартал.\n\n"
                  f"У тебя {employee_data['sales']} сделок на сумму {employee_data['sum']} при плане в "
                  f"{employee_data['plan']}, твой план выполнен на {employee_data['percent']}%. "
                  f"Твоя зарплата в этом квартале - {employee_data['salary']} в месяц, "
                  f"твоя премия - {employee_data['bonus']}."
    },
]

sber_checker = SberChecker(
    filename=filename,
    tests=my_tests,
    call="build_letter",
)
res = sber_checker.run()

json_res = json.dumps(res, indent=4, ensure_ascii=False)

print(json_res)
