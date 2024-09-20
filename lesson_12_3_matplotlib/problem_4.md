Так как на горизонтальной оси находятся месяцы, то было бы хорошо указать текстовые подписи, а не номер месяца.

После команды `year_2021 = ...` создайте список `month` с сокращенными названиями месяцев, как в примере из теории.

В конце программы допишите команду

```python
plt.xticks(ticks=range(len(months)))
```

и посмотрите на результат.

Затем замените ее на команду

```python
plt.xticks(ticks=range(len(months)), labels=months)
```

Подстановка происходит в два этапа. Передавая в аргумент `ticks=range(len(months))`, мы сообщаем, что ярлыки по оси Х должны быть числами от 0 до 11. Передавая `labels=months`, мы заменяем каждое число на элемент массива `months` согласно индексам.