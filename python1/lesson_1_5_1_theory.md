# Преобразование типов | Туда и обратно


У любой переменной можно спросить какого она типа с помощью функции ```type```. Чтобы узнать какого типа переменная ```a``` надо написать ```type(a)```.


```python
a = 1
print(a, type(a))

b = 1.5
print(b, type(b))

c = True
print(c, type(c))
```

    1 <class 'int'>
    1.5 <class 'float'>
    True <class 'bool'>
    

Более того в питоне, в отличии от некоторых других языков программирования царит типовая демократия и каждая переменная по сути гендер-флюид, то есть может изменить свой тип в любой момент времени. Правда в результате смены типа может терятся некоторая информация...


```python
print('int to float:', a, '->', float(a))
print('int to bool: ', a, '->', bool(a))
print()

print('float to int: ', b, '->', int(b))
print('float to bool:', b, '->', bool(b))
print()

print('bool to int:  ', c, '->', int(c))
print('bool to float:', c, '->', float(c))
```

    int to float: 1 -> 1.0
    int to bool:  1 -> True
    
    float to int:  1.5 -> 1
    float to bool: 1.5 -> True
    
    bool to int:   True -> 1
    bool to float: True -> 1.0
    

Любое число при преобразовании в bool, если оно не 0, превращается в True, а если 0, то превращается в False.

У добного числа при преобразовании в целое обрезается целая часть.

Булево True превращается в 1 или 1.0, а булево False превращается в 0 или 0.0.
Казалось бы 1 и 1.0 это одно и то же, но нет. Одно это целый тип, другое дробный и они занимают разное количество места в памяти, хотя значат одно и то же.