def len_(list_):
    counter = 0
    if not list_:
        return 0
    else:
        counter = 1 + len_(list_[1:])
        return counter
print('Длина списка ', len_([1, 2, 3, 4]))