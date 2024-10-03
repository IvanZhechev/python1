def calculator():
    while True:
        try:

            num1 = float(input("Введіть перше число: "))
            # Запитуємо операцію
            operation = input("Оберіть операцію (+, -, *, /): ")

            num2 = float(input("Введіть друге число: "))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Помилка: ділення на нуль неможливе.")
                    continue
                result = num1 / num2
            else:
                print("Невідома операція. Спробуйте ще раз.")
                continue


            print(f"Результат: {result}")

        except ValueError:
            print("Помилка: введено некоректні дані. Спробуйте ще раз.")
            continue


        choice = input("Хочете продовжити? (y/yes для продовження): ").strip().lower()
        if choice != "y" and choice != "yes":
            print("Роботу завершено.")
            break

calculator()
