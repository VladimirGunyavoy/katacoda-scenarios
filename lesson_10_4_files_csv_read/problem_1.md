В CSV-файле содержится информация о предложениях по проведению тимбилдинга (организатор, количество участников, бюджет). 

Напишите скрипт на Python с помощью DictReader, который выводит названия тимбилдингов с количеством участников больше 20 и бюджетом меньше 500 долларов.

Содержимое csv-файла:
```
организатор,количество участников,бюджет
"EventCo",25,450
"TeamBuilders Inc.",15,300
"Corporate Retreats Ltd.",30,600
"Dynamic Events",22,480
"FunTime Events",18,200
"Unlimited Adventures",50,499
"Team Energizers",10,100
"Synergy Getaways",35,450
"AdventureWorks",12,150
"Peak Performance",45,490
```

Формат вывода:
```
"EventCo"
"Dynamic Events"
...
```