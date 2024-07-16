def sum_(arg):
    res = 0
    if len(arg) < 1:
        return 0
    else:
        res += arg[0] + sum_(arg[1:])
        return res
print(sum_([1, 2, 3, 4]))
