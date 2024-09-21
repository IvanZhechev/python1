
number = int(input("Введіть 4-значне число: "))

thousands, remainder = divmod(number, 1000)
print(thousands)

hundreds, remainder = divmod(remainder, 100)
print(hundreds)

tens, units = divmod(remainder, 10)
print(tens)

print(units)
