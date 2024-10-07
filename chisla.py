def multiply_digits_until_single(num):
    while num > 9:
        product = 1
        while num > 0:
            product *= num % 10
            num //= 10
        num = product
    return num

user_input = int(input("Введіть ціле число: "))
result = multiply_digits_until_single(user_input)
print(f"Результат: {result}")
