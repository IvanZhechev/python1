import string
import keyword

def is_valid_variable_name(name):
    if name in keyword.kwlist:
        return False
    if name[0].isdigit():
        return False
    if " " in name or name.count("_") > 1:
        return False
    for char in name:
        if char in string.punctuation and char != "_":
            return False
        if char.isupper():
            return False

    return True

examples = ["_", "__", "my_new_value", "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"]

results = {example: is_valid_variable_name(example) for example in examples}
results
