
def split_list(lst):
    if not lst:
        return [[], []]
    split_index = (len(lst) + 1) // 2
    first_part = lst[:split_index]
    second_part = lst[split_index:]
    return [first_part, second_part]
my_list = [1, 2, 3, 4, 5]
result = split_list(my_list)
print(result)
