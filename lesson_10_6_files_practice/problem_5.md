Возьмите данные из файлов `employees.csv`  и `salary.csv`, где содержится информация по должностям сотрудников и их заработным платам соответственно.

Содержимое `employees.csv`:
```
full_name,profession,grade
Марк Киселев,frontend,junior
Дарина Максимова,backend,middle
Аксель Игнатьев,backend,senior
Феликс Воронов,frontend,junior
Злата Бурова,qa,middle
Луиза Романовская,backend,middle
Ирина Альшевская,designer,middle
Полина Хрущева,product,junior
Радомир Зеленский,product,senior
Вильгельм Казанцев,frontend,middle
Лукреция Миронова,qa,junior
Герман Нестеров,designer,senior
```


Содержимое `salary.csv`:
```
full_name,salary
Ирина Альшевская,120000
Марк Киселев,90000
Дарина Максимова,135000
Аксель Игнатьев,110000
Феликс Воронов,95000
Злата Бурова,125000
Луиза Романовская,118000
Полина Хрущева,87000
Радомир Зеленский,140000
Вильгельм Казанцев,105000
Лукреция Миронова,95000
Герман Нестеров,130000
```

Объедините данные в таблицу и запишите в файл `empoyees_full.csv`
```
full_name,profession,grade,salary
Марк Киселев,frontend,junior,90000
Дарина Максимова,backend,middle,135000
Аксель Игнатьев,backend,senior,110000
...
```