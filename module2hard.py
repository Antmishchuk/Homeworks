my_input = int(input('Введите число: '))
pare = []
for i in range(1, my_input):
    for j in range(i+1, my_input):
        a = i + j
        if  my_input % a == 0:
            pare.append(f'{i}{j}')
            result = (''.join(pare))
print(f'{my_input} - {result}')




