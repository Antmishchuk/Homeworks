def sum_elem(list_):
    res = 0
    for element in list_:
        if type(element) == type([]):
            res = res + sum_elem(element)
        else:
            res = res + element
    return res

    # for element in list_:
    #     if element == list:
    #         res += element
    #     else:
    #         res += sum_elem(element)
    # return res

    if not isinstance(list_,list):
        return list_
    for element in list_:
        res += sum_elem(element)
    return res

list_ = [1, [2, 3], [4, 5, 6]]
print(sum_elem(list_))
