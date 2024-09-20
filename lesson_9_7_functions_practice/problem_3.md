У вас есть список словарей формата
```python
[
   {"category": "Зарплата", "value": 987000},
   {"category": "Аренда", "value": 160000},
   {"category": "Продвижение", "value": 350000},   
]
```

Напишите функцию `get_expenses_stats(expenses)`, которая считает, какой процент занимает каждая из категорий, и верните результат в виде словаря. 

Пример возвращаемого значения:

```python
expenses = [
    {"category": "Зарплата", "value": 0.56},
    {"category": "Аренда", "value": 0.19},
    ...
]
```