def three_args(a=None, b=None, c=None):
    list = []
    for i in (a, b, c):
        if i is not None:
            list.append(i)
    return list
print(three_args(1))
