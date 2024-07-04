# SberChecker

SberChecker - это инструмент для автоматизированного тестирования Python-кода. 
Он поддерживает различные сценарии тестирования, включая проверку ввода/вывода, 
тестирование функций, использование последующего кода, а также сравнение с эталонным решением.

## Основные компоненты

- **tests**: Список тестов для проверки кода (каждый тест в виде словаря либо с input/output либо с args/return)
  - для скриптов без функций:
    - **input**: Данные, подаваемые на вход (список)
    - **output**: Ожидаемый вывод (список)
  - для скриптов с функциями
    - **args**: Аргументы, передаваемые в функцию (список)
    - **return**: Ожидаемый результат выполнения функции (любой тип данных)

- **solution**: Эталонная функция для сравнения результатов
- **should_include**: Функция для проверки наличия определенных конструкций в коде
- **call**: Название функции в задании ученика, которая должна быть вызвана для проверки
- **pre_code**: Код, выполняемый перед основным кодом [пока не реализовано]
- **post_code**: Код, выполняемый после основного кода

## Примеры использования

### 1. Задача на ввод и вывод

```python
# script.py
a = input()
b = input()

print(a)
print(b)

# test.py
checker = SberChecker(
    filename="script.py",
    tests=[
        {
            "input": [2, 4],
            "output": ["2", "4"]
        },
    ]
)
results = checker.run()
```

### 2. Задача на вызов функции с аргументами

```python
# script.py
def square(x):
    return x ** 2

# test.py
checker = SberChecker(
    filename="script.py",
    tests=[
        {"args": [5], "return": 25},
        {"args": [10], "return": 100}
    ],
    call="square"
)
results = checker.run()
```

### 3. Задача c посткодом

```python
# script.py
a=1
b=2

# test.py
postcode = """
try:
    a
    print("а задан")
except:
    print("а не задан")
try:
    b
    print("b задан")
except:
    print("b не задан")
"""

checker = SberChecker(
    filename="script.py",
    tests=[
        {
            "input": [],
            "output": ["а задан", "b задан"]
        },
    ],
    postcode=postcode,
)

results = checker.run()
```

### 4. Задача на проверку c solution

```python
# script.py
def count_r(line):
    return line.lower().count("р")

# test.py
def solution(line):
    return line.lower().count("р")


checker = SberChecker(
    filename="../tasks/07.py",
    tests=[
        {
            "input": ["Варежка"],
            "output": [],
        },
    ],
    call="count_r",
    solution=solution
)

results = checker.run()
```

### 5. Задача с should_include

```python
# script.py
items = input().split()

for item in items:
    print(item)

# test.py
def should_include(code):
    return "for" in code


checker = SberChecker(
    filename="../tasks/04.py",
    tests=[
        {
            "input": ["1 2 3"],
            "output": ["1", "2", "3"],
        },
    ],
    should_include=should_include,
)

result = checker.run()
```