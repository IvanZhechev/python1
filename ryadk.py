def move_zeros_to_end(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(0)
    return lst


lst = [0, 1, 0, 3, 12]
result = move_zeros_to_end(lst)
print(result)
