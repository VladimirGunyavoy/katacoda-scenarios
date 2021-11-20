## Подготовка окружения
Для  подготовки окружения запустим скрипт: 

`prepare.sh`{{execute}}

скрипт выполняет следуещее:
- создает необходимые неймспейсы в kubernetes
- создает файл переменных окружения ~/envs
- выполняет деплой системных компонент OpenFaaS, Gravitee apim, registry
- устанавливает консольную утилиту faas-cli для взаиимодействия с OpenFaaS из командной строки
- скачивает темплейт для создания функций на языке python в root/template
- устанавливает gravitee apim

Для установки переменных окружения используем созданный файл:

`source ~/envs`{{execute}}
## Проверка окружения
получим список запущенных подов в кластере и убедимся что у всех статус ready

`kubectl get po -A`{{execute}}

Проверим доступ из консольного клиента к OpenFaaS 

`faas-cli list -v`{{execute}}

т.к. ни одной функции мы еще не создали, вывод будет следующий:
```
Function                        Image                                           Invocations     Replicas        CreatedAt
```

Интерфейс gravitee доступен по ссылке [gravitee ](https://[[HOST_SUBDOMAIN]]-32500-[[KATACODA_HOST]].environments.katacoda.com/ui)
Портал доступен по ссылке [gravitee portal](https://[[HOST_SUBDOMAIN]]-32500-[[KATACODA_HOST]].environments.katacoda.com/portal)

На этом настройка окружения успешно завершена. Далее попробуем запустить свою первую serverless функцию.