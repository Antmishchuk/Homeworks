my_input = int(input('Введите число: '))
# int(my_input)
#print(my_input)
pare = []
for i in range(1, 11):
    for j in range(1, 11):
        a = i + j
        if my_input % a == 0 and i <= my_input and j <= my_input:
            pare.append(f'{i}{j}')
            result = set(pare)
            print(pare)




