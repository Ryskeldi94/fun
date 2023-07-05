def calculator():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b != 0:
            return a / b
        else:
            print("Ошибка: деление на ноль")
            return None

    def power(a, b):
        return a ** b

    def sqrt(a):
        if a >= 0:
            return a ** 0.5
        else:
            print("Ошибка: квадратный корень из отрицательного числа")
            return None

    def factorial(n):
        if n >= 0:
            result = 1
            for i in range(1, n+1):
                result *= i
            return result
        else:
            print("Ошибка: вычисление факториала для отрицательного числа")
            return None

    def average(numbers):
        if len(numbers) > 0:
            return sum(numbers) / len(numbers)
        else:
            print("Ошибка: невозможно вычислить среднее значение для пустого списка чисел")
            return None

    def maximum(numbers):
        if len(numbers) > 0:
            return max(numbers)
        else:
            print("Ошибка: невозможно найти максимальное значение в пустом списке чисел")
            return None

    def minimum(numbers):
        if len(numbers) > 0:
            return min(numbers)
        else:
            print("Ошибка: невозможно найти минимальное значение в пустом списке чисел")
            return None

    # вывод операции и значения 
    num1 = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))

    # вызов функция swich(operation)
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Ошибка: неподдерживаемая операция")
        result = None

    # Вывод результата
    if result is not None:
        print("Результат:", result)

# Вызов главной функции калькулятора
calculator()
