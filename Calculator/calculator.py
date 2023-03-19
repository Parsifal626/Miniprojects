# Запросите у пользователя два числа
while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка! Введите числа.")

# Попросите у пользователя операцию, которую нужно выполнить
while True:
    operation = input("Выберите операцию (+, -, *, /): ")
    if operation in ['+', '-', '*', '/']:
        break
    else:
        print("Ошибка! Выберите допустимую операцию.")

# Выполните выбранную операцию
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Ошибка! Деление на ноль.")
    else:
        result = num1 / num2

# Выведите результат
if operation != "/":
    print("Результат: ", result)
