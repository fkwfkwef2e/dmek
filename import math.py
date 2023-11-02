import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Ошибка! Деление на ноль невозможно.")

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        print("Ошибка! Квадратный корень из отрицательного числа не определен.")

def factorial(x):
    if x >= 0:
        return math.factorial(x)
    else:
        print("Ошибка! Факториал отрицательного числа не определен.")

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

# Проверка ввода чисел
def get_number_input(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Ошибка! Введите число.")

# Проверка ввода операции
def get_operation_input(message):
    operations = ['+', '-', '*', '/', '^', 'sqrt', '!', 'sin', 'cos', 'tan']
    while True:
        operation = input(message)
        if operation in operations:
            return operation
        else:
            print("Ошибка! Введите правильную операцию.")

# Главная функция калькулятора
def calculator():
    while True:
        operation = get_operation_input("Введите операцию (+, -, *, /, ^, sqrt, !, sin, cos, tan): ")

        if operation == '+':
            num1 = get_number_input("Введите первое число: ")
            num2 = get_number_input("Введите второе число: ")
            print("Результат:", add(num1, num2))

        elif operation == '-':
            num1 = get_number_input("Введите первое число: ")
            num2 = get_number_input("Введите второе число: ")
            print("Результат:", subtract(num1, num2))

        elif operation == '*':
            num1 = get_number_input("Введите первое число: ")
            num2 = get_number_input("Введите второе число: ")
            print("Результат:", multiply(num1, num2))

        elif operation == '/':
            num1 = get_number_input("Введите первое число: ")
            num2 = get_number_input("Введите второе число: ")
            print("Результат:", divide(num1, num2))

        elif operation == '^':
            num1 = get_number_input("Введите число: ")
            num2 = get_number_input("Введите степень: ")
            print("Результат:", power(num1, num2))

        elif operation == 'sqrt':
            num = get_number_input("Введите число: ")
            print("Результат:", square_root(num))

        elif operation == '!':
            num = get_number_input("Введите число: ")
            print("Результат:", factorial(num))

        elif operation == 'sin':
            num = get_number_input("Введите угол в радианах: ")
            print("Результат:", sin(num))

        elif operation == 'cos':
            num = get_number_input("Введите угол в радианах: ")
            print("Результат:", cos(num))

        elif operation == 'tan':
            num = get_number_input("Введите угол в радианах: ")
            print("Результат:", tan(num))

        choice = input("Хотите продолжить? (да/нет): ")
        if choice.lower() != 'да':
            break

calculator()