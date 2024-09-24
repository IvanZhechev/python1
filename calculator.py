
num1 = float(input("Введіть перше число: "))
operation = input("Введіть дію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Помилка: ділення на нуль!"
else:
    result = "Невідома операція!"

print(f"Результат: {result}")
