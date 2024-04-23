    error := testObj[testName]
    msg := sprintf("%s %s завершился с ошибкой: %s", [suite, testName, error])
}

deny[msg] {
	testObj := input[suite].error[_]
    testObj[testName]
    error := testObj[testName]
    msg := sprintf("%s %s завершился с ошибкой: %s", [suite, testName, error])
}

error[msg] {
	msg := input.error
}