def summa(list_):
    res = 0
    if len(list_) < 1:
        return 0
    else:
        res = list_[0] + summa(list_[1:])
        return res
print(summa([1, 2, 3, 4]))

