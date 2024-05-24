**Условные операторы**

В это сценарии мы выполним несколько заданий на работу с условными операторами в Python.

### Оператор if

Условные операторы нужны для проверки условий и, в зависимости от результата, чтобы вести логику выполнения программы в нужном направлении.

Условный оператор **if** ("если") является основным оператором проверки выполнения условия. Для того, чтобы выполнить простую вложенную инструкцию, необходимо проверить условие на соответствие, использовав оператор **if** и прописав после него соответствующее условие:

```
# объявляем переменную
var = 5
# выполняем проверку условия
if var < 10:
# если условие выполняется, то выполняется вложенная инструкция
    print("var less than 10")
```

В данном случае мы объявляем переменную **var** и присваиваем ей значение равное **5**, далее выполняем проверку условия - если переменная меньше **10**, то вывести соответсвующее сообщение.

Оператор **if** производит проверку истинности выражения, т.е. является ли результат выражения логической истиной (**True**) или же ложью (**False**). Далее выполняется вложенная инструкция, если результат выражения является **True**. Если результат выражения является **False**, тогда вложенная инструкция игнорируется. В предыдущем разделе приводились примеры того, что выводит Python в качестве результата выражения с оператором сравнения.