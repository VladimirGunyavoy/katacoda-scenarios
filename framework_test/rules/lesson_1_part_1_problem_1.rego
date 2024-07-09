package sbercode

allow[msg] {
	test := input[key]
    test.passed
    msg := sprintf("*%s* выполнены условия теста\n ожидаемый результат: %s, \nфактический результат %s", [key, test.result[0], test.expected[0]])
}

deny[msg] {
	test := input[key]
    not(test.passed)
    msg := sprintf("*%s* не выполнен\nВвод: Ожидания: %s\nреальность %s", [key,  test.input, test.expected[0], test.result[0]])
}

error[msg] {
	test := input[key]
    test.error != null
    msg := sprintf("*%s* непредвиденная ошибка: %s", [key, test.error])
}