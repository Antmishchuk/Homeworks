def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(a=2)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 2, 3]
values_dict = {'a': 3, 'b': 4, 'c': 5}
print_params(*values_list)
print_params(**values_dict)

values_list2 = ['Строка', True]
print_params(*values_list2, 42)