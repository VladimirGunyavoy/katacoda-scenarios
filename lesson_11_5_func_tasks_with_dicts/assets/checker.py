import sys
from io import StringIO
from typing import Callable, Union
from unittest.mock import patch


class SberChecker:
    """ Class for checking code"""

    def __init__(
        self,
        filename,
        tests,
        call=None,
        solution=None,
        should_include=None,
        should_include_message=None,
        precode=None,
        postcode=None
    ):
        self.filename: str = filename
        self.tests: list = tests
        self.call: str = call
        self.solution: Callable = solution
        self.should_include: Callable = should_include
        self.message: str = should_include_message
        self.precode: str = precode
        self.postcode: str = postcode

    @staticmethod
    def __file_read(filename):
        try:
            with open(filename, encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return {"error": f"File {filename} not found in current directory"}

    @staticmethod
    def __check_inputs_outputs(test):
        try:
            if 'input' in test:
                return test['input'], test['output']
            return test['args'], test['return']
        except KeyError:
            raise ValueError("'input(args)' and/or 'output(return)' are not defined")

    @staticmethod
    def __execute_function(func: Union[str, Callable], args, file_content):
        if isinstance(func, str):
            exec(file_content, globals())
            function = globals().get(func)
            if not function:
                raise ValueError(f"Function with name '{func}' is not defined")
        else:
            function = func

        if not args:
            result = function()
        else:
            result = function(*args)
        return result

    def __check_with_function(self, test, file_content):
        args, expected_return = self.__check_inputs_outputs(test)

        try:
            # If output is empty, then we should try to execute solution function
            if not expected_return and expected_return != 0:
                if self.solution:
                    user_result = self.__execute_function(self.call, args, file_content)
                    solution_result = self.__execute_function(self.solution, args, file_content)

                    passed = user_result == solution_result
                    return passed, user_result, None
                else:
                    raise ValueError("Solution function is not defined")

            user_result = self.__execute_function(self.call, args, file_content)

            passed = expected_return == user_result
            return passed, user_result, None
        except Exception as e:
            return False, None, f"{type(e).__name__}: {str(e)}"

    def __check_without_function(self, test, file_content):
        input_values, expected_output = self.__check_inputs_outputs(test)

        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            with patch('builtins.input', side_effect=input_values):
                exec(file_content, globals())
                result = captured_output.getvalue().strip().split('\n')
                passed = expected_output == result
                return passed, result, None
        except Exception as e:
            return False, None, f"{type(e).__name__}: {str(e)}"
        finally:
            sys.stdout = sys.__stdout__

    def __check_include(self, file_content):
        clean_code = file_content

        # Обрабатываем многострочные комментарии обоих типов
        for quotes in ('"""', "'''"):
            while quotes in clean_code:
                start = clean_code.find(quotes)
                end = clean_code.find(quotes, start + 3)
                if end == -1:  # Если нет закрывающих кавычек то отмена
                    break
                clean_code = clean_code[:start] + ' ' + clean_code[end + 3:]

        # Обрабатываем однострочные комментарии и пустые строки
        clean_lines = []
        for line in clean_code.split('\n'):
            # Убираем комментарии из строки
            if '#' in line:
                line = line[:line.find('#')]

            line = line.strip()
            if line:
                clean_lines.append(line)

        clean_code = ' '.join(clean_lines)

        return self.should_include(clean_code)

    def _convert_to_string(self, obj):
        if isinstance(obj, (int, float)):
            return str(obj)
        elif isinstance(obj, (str, bool)):
            return obj
        elif isinstance(obj, list):
            return [self._convert_to_string(item) for item in obj]
        elif isinstance(obj, dict):
            return str({self._convert_to_string(k): self._convert_to_string(v) for k, v in obj.items()})
        else:
            return str(obj)

    def run(self):
        """ Main function for checking code """

        def _crutch_for_output(obj):
            """ Crutch for output results """
            return obj if isinstance(obj, list) else [obj]

        file_content = self.__file_read(self.filename)
        if "error" in file_content:
            return file_content
        try:
            results = {}
            for index, test in enumerate(self.tests, start=1):
                if self.precode:
                    code = f'{self.precode}\n\n' + file_content
                else:
                    code = file_content

                if self.postcode:
                    code = code + f'\n\n{self.postcode}'

                if f'def {self.call}' in code:
                    passed, result, error = self.__check_with_function(test, code)
                else:
                    passed, result, error = self.__check_without_function(test, code)

                inputs, output = self.__check_inputs_outputs(test)

                if self.should_include:
                    if not self.message:
                        return {"error": f"You must specify 'should_include_message' parameter"}

                    should_include_result = self.__check_include(file_content)
                else:
                    should_include_result = ""

                results[f'Test {index}'] = {
                    'input': _crutch_for_output(self._convert_to_string(inputs)) if inputs else [],
                    'expected': _crutch_for_output(self._convert_to_string(output)) if output else [],
                    'result': _crutch_for_output(self._convert_to_string(result)) if result is not None else [],
                    'passed': passed,
                    'error': error,
                    'should_include': should_include_result,
                }
                if not should_include_result:
                    results[f'Test {index}']['message'] = self.message

            return results
        except Exception as e:
            return {"error": f"{type(e).__name__}: {str(e)}"}
