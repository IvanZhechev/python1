import string


def letter_range(input_str):
    letters = string.ascii_letters

    start, end = input_str.split('-')

    start_index = letters.index(start)
    end_index = letters.index(end)

    return letters[start_index:end_index + 1]


user_input = input("Введіть діапазон букв через дефіс (наприклад, 'a-c'): ")
result = letter_range(user_input)
print(result)
