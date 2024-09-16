Почти в любой почтовой программе или сервисе есть функция сортировки писем по категориям, тегам или папкам. Давайте напишем небольшую функцию `organize_emails(all_emails)`. Она будет принимать список контактов (например, `["sasha@microminds.ru", "eva@retarded.ru", "veronica@dolt.io", "ivan@retarded.ru"]`  и возвращать контакты, отсортированные по организации, например: 

```python
{
  "retarded": ["eva@retarded.ru", "ivan@retarded.ru"],
  "microminds": ["sasha@microminds.ru",
  ...  
}
```

Cперва напишите функцию `extract_domain(email)`, которая возвращает домен почты.

```python
extract_domain("roman-hr@sber.ru") >>>  sber
extract_domain("guido@python.org") >>>  python
```

Затем напишите функцию `organize_emails(all_emails)`, которая принимает список и организует почты в словарь.

| Подсказка |
- Для извлечения названия организации сперва разделите строку по @ и возьмите последний сегмент, а затем разделите по точке и возьмите первый.