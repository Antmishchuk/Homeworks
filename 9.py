def sum_list(list_):
    if list_ == []:
        return list_
    if isinstance(list_[0], list):
        return sum_list(list_[0]) + sum_list(list_[1:])
    return list_[:1] + sum_list(list_[1:])
list_ = [1, [2, 3], [4, 5, 6]]

print(sum_list(list_))

