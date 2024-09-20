Продолжим задачу из предыдущего урока.

Создайте скрипт для обработки CSV-файла, в котором содержатся отзывы пользователей об обслуживании в вашем офисе в
формате «оценка (1-5), комментарий».

Программа должна подсчитать среднюю оценку и процент оценки 5. Также нужно отдельно вывести все негативные комментарии (к оценкам 1, 2, 3) и все позитивные (к оценкам 4 и 5).

CSV-файл:

```
rating,comment
5,Отличное обслуживание!
3,Могло бы быть и лучше.
1,Совсем не понравилось.
4,Все нормально.
2,Требуется улучшение.
5,Все супер!
4,Удовлетворительно.
3,Не очень.
```

Формат вывода следующий:
```
Средняя оценка: 3.14
Процент оценок 5: 14.29%

Позитивные комментарии:
Все нормально.
Все супер!
Удовлетворительно.

Негативные комментарии:
Могло бы быть и лучше.
Совсем не понравилось.
Требуется улучшение.
Не очень.
```