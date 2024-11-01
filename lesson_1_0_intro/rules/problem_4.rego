package sbercode

# https://play.openpolicyagent.org/p/zmT8PbZlF0

fmt := concat("", [
	`## %s

<details>

### Входные данные

`,
	"```",
	`
%s
`,
	"```",
	`

### Ожидаемый результат

`,
	"```",
	`
%s
`,
	"```",
	`
### Фактический результат

`,
	"```",
	`
%s
`,
	"```",
])

errFmt := concat("", [
	`## %s

<details>

### Непредвиденая ошибка

`,
	"```",
	`
%s
`,
	"```",
])

allow[msg] {
	test := input[key]
	test.passed
	msg := sprintf(fmt, [key, concat("\n", test.input), concat("\n", test.expected), concat("\n", test.result)])
}

deny[msg] {
	test := input[key]
	not test.passed

	msg := sprintf(fmt, [key, concat("\n", test.input), concat("\n", test.expected), concat("\n", test.result)])
}

deny[msg] {
	test := input[key]
	not test.should_include

	msg := test.message
}

error[msg] {
	test := input[key]
	test.error != null
	msg := sprintf(errFmt, [key, test.error])
}
