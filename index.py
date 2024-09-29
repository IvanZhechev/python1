def sum_even_index_and_multiply(lst):
    if not lst:
        return 0
    return sum(lst[::2]) * lst[-1]

lst = [2, 3, 4, 5, 6]
result = sum_even_index_and_multiply(lst)
print(result)

