Большая часть покупателей довольны вашими продуктами, но некоторые оформляют возврат. В CSV-файле `purchases_and_refunds.csv` указан месяц покупки, сумма покупки и статус:

- `payment` означает, что товар был оплачен;
- `refund` — за товар вернули деньги.

Со стандартного ввода подается название месяца. Расчет возвратов от месяца к месяцу позволяет планировать продажи и отслеживать уровень удовлетворенности вашим продуктом. Выведите процент возвратов в этом месяце в формате float, округленного до одного знака после запятой, со знаком процента. 

```python
# Пример ввода:
february

# Пример вывода:
9.0%
```

Содержимое файла `purchases_and_refunds.csv`:
```
month,product,amount,status 
june,Подписка на 3 месяца,3000,payment 
june,Подписка на 1 месяц,1300,payment 
june,Максимальная подписка на 12 месяцев,9000,payment 
june,Подписка на 1 месяц,1300,refund 
june,Подписка на 3 месяца,3000,payment
may,Подписка на 3 месяца,3000,payment
may,Подписка на 1 месяца,1300,payment
may,Подписка на 1 месяц,1300,refund 
```