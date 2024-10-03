import string
import keyword


def is_valid_variable_name(name):
    if name in keyword.kwlist:
        return False

    if not (name[0].isalpha() or name[0] == "_"):
        return False

    if name.count("_") > 1:
        return False

    for char in name:
        if char.isupper() or char in string.punctuation.replace("_", "") or char.isspace():
            return False
    return True


# Приклад використання
variable_name = input("Введіть ім'я змінної: ")
print(is_valid_variable_name(variable_name))
