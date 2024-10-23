def some_gen(begin, end, func):
    """
    Генераторна функція, яка повертає n елементів числової послідовності.

    :param begin: перший елемент послідовності
    :param end: кількість елементів у послідовності
    :param func: функція, яка формує значення для послідовності
    """
    value = begin
    for _ in range(end):
        yield value
        value = func(value)


def pow(x):
    return x ** 2

gen = some_gen(2, 4, pow)

from inspect import isgenerator
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
