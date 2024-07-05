import sys
from io import StringIO
from typing import Callable
from unittest.mock import patch


class SberChecker:
    """ Class for checking code"""

    def __init__(self, filename, tests, call=None, solution=None, should_include=None, postcode=None):
        self.filename: str = filename
        self.tests: list = tests
        self.call: str = call
        self.solution: Callable = solution
        self.should_include: Callable = should_include
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
    def __execute_function(func: str | Callable, args, file_content):
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
            """ If output is empty, then we should try to execute solution function """
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
                exec(file_content)
                result = captured_output.getvalue().strip().split('\n')
                passed = expected_output == result
                return passed, result, None
        except Exception as e:
            return False, None, f"{type(e).__name__}: {str(e)}"
        finally:
            sys.stdout = sys.__stdout__

    def __check_post_code(self, test, file_content):
        _, expected_output = self.__check_inputs_outputs(test)

        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            file_content = file_content + f'\n{self.postcode}'
            exec(file_content)
            result = captured_output.getvalue().strip().split('\n')
            passed = expected_output == result
            return passed, result, None
        except Exception as e:
            return False, None, f"{type(e).__name__}: {str(e)}"
        finally:
            sys.stdout = sys.__stdout__

    def __check_include(self, file_content):
        return self.should_include(file_content)

    def run(self):
        file_content = self.__file_read(self.filename)
        if "error" in file_content:
            return file_content
        try:
            results = {}
            for index, test in enumerate(self.tests, start=1):
                if f'def {self.call}' in file_content:
                    passed, result, error = self.__check_with_function(test, file_content)
                elif self.postcode:
                    passed, result, error = self.__check_post_code(test, file_content)
                else:
                    passed, result, error = self.__check_without_function(test, file_content)

                inputs, output = self.__check_inputs_outputs(test)

                results[f'Test {index}'] = {
                    'input': inputs if inputs else "N/A",
                    'expected': output if output else "N/A",
                    'result': result if result is not None else "N/A",
                    'passed': passed,
                    'error': error,
                    'should_include': self.__check_include(file_content) if self.should_include else "N/A",
                }
            return results
        except Exception as e:
            return {"error": f"{type(e).__name__}: {str(e)}"}
