

number = int(input("Введіть 5-значне число: "))


reversed_number = 0


for _ in range(5):
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10


print(reversed_number)

