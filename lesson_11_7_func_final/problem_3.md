Планы продаж для каждого сотрудника различаются в зависимости от отдела и хранятся в файле `teams.csv` в формате:

```
team,lead,plan
team_red,Морошкина,850000
team_green,Алексеев,960000
team_blue,Ушастая,930000
```

У вас есть:

- файл `employees.csv`

```
employee,team
Ласточкина,team_red
Серебрянников,team_green
Кукушкин,team_blue
```

- функция `read_data(path)`, которая загружает файл в формате `.csv`;
- функция `get_plan_by_team(name)`, которая вернет план по названию команды;
- функция `get_employee_by_surname(surname)`, которая вернет информацию о сотруднике по его фамилии.

Напишите функцию `get_employee_plan(name)`, которая получит имя сотрудника и вернет его план продаж, используя две функции выше.