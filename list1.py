
def move_last_to_first(lst):
    if len(lst) <= 1:
        return lst
    else:
        last_element = lst.pop()
        lst.insert(0, last_element)
        return lst
my_list = [1, 2, 3, 4, 5]
new_list = move_last_to_first(my_list)
print(new_list)
