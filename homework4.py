immutable_var = (2, 5, [1, 2], True, 'text')
print(immutable_var)
# immutable_var[4] = 'string' #Элементы кортежа, если только это не список внутри кортежа, являются неизменяемыми
mutable_list = [2, 5, [1, 2], True, 'text']
print(mutable_list)
mutable_list[4] = 'string'
print(mutable_list)