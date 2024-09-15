В этой задаче у вас есть функция, которая считает расходы и доходы, выполняет сведение бюджета и записывает результаты в файл.

```python
def calculate_and_record_budget(incomes, expenses):
    
    incomes_total = 0
    expenses_total = 0
    
    for record in incomes:
       incomes_total += record["value"]
 
    for record in expenses:
       expenses_total += record["value"]   
       
    balance = incomes_total - expenses_total   
    
    file = open("result.txt", "w")
    file.write(str(balance))
    
    file.close()

calculate_and_record_budget([500, 700, 900], [300, 200, 100])
```

Пример записи в файл `result.txt` после выполнения:
```
1500
```

Вынесите подсчет расходов и доходов в отдельные функции:
```python
def calculate_total(records):
    pass


def record_to_file(result):
    pass


def calculate_and_record_budget(incomes, expanses):
    pass

```
