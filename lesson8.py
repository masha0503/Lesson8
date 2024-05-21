import logging

logging.basicConfig(filename='logs.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Calculation:
    def __call__(self, operation, a, b):
        try:
            a = self._convert_to_number(a)
            b = self._convert_to_number(b)
            result = self._execute_operation(operation, a, b)
            logging.info(f'{a} {operation} {b} = {result}')
            return result
        except (ValueError, ZeroDivisionError) as e:
            logging.error(e)
            return str(e)

    def _convert_to_number(self, value):
        try:
            number = float(value)
            return number
        except ValueError:
            error_message = f"Помилка: Неможливо конвертувати значення '{value}' в число."
            logging.error(error_message)
            raise ValueError(error_message)

    def _execute_operation(self, operation, a, b):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                raise ZeroDivisionError("Помилка: Поділ на нуль неможливий.")
            return a / b
        else:
            raise ValueError(f"Помилка: Непідтримувана операція '{operation}'.")

calculator = Calculation()

print("Результат:", calculator('*', '5', '3'))