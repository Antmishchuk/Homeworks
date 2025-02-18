# Задача1

# x = float(input('Введите число: '))
# print("Первая цифра после точки равна: ", int(x * 10) % 10)

# Задача2
# х = int(input('Введите число минут: '))
# h = (х // 60) % 24
# m = х % 60
# print(h, m)


# Задача3

# n = int(input('Введите число 6-значное число: '))
# a = (n // 100000)
# b = (n // 10000 % 10)
# c = (n // 1000 % 10)
# d = (n // 100 % 10)
# e = (n // 10 % 10)
# f = (n % 10)
# print("Сумма цифр в числе:", (a + b + c + d + e + f))

# Задача4

# n = int(input('Введите число: '))
# print(((n // 2) * 2) + 2)

# Задача5

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# c = int(input('Введите число c: '))
# d = b**2 - 4 * a * c
# if d < 0:
#     pass
# elif d == 0:
#     print(-b / (2 * a))
# else:
#     k1 = int((-b + d ** 0.5) / (2 * a))
#     k2 = int((-b - d ** 0.5) / (2 * a))
#     if k1 < k2:
#         print(k1, k2)
#     else:
#         print(k2, k1)

# Задача6

# h = int(input('Введите час: '))
# m = int(input('Введите минуту: '))
# s = int(input('Введите секунду: '))
# x = 360/12
# a = x * h + x/60 * m + x/3600 * s
# print(a)

# Задача7

# s = input('Введите строку: ')
# print('Количество слов в строке: ', s.count(' ') + 1)

# Задача8

# s = input('Введите строку: ')
# s = s.replace(' ', '')
# if s.lower() == s[::-1].lower():
#     print('yes')
# else:
#     print('no')

# Задача9

# s = input('Введите строку: ')
# l = len(s)
# part_1 = (s[:(l + (l % 2)) // 2])
# part_2 = (s[(l + (l % 2)) // 2:])
# print(part_2 + part_1)

# Задача10

# alph = []
# for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     alph.append(i)
# text = input('Введите строку: ')
# key = int(input('Введите ключ: '))
# text = text.upper()
# s = ''
# for i in text:
#     k = alph.index(i)
#     s = s + alph[k-key]
#
# print(s)


# Задача11

# N, M, x, y = int(input()), int(input()), int(input()), int(input())
#
# if M > 1:
#     if y == 1:
#         print(x, y + 1)
#     elif y == M:
#         print(x, y - 1)
#     else:
#         print(x, y - 1)
#         print(x, y + 1)
# if N > 1:
#     if x == 1:
#         print(x + 1, y)
#     elif x == N:
#         print(x - 1, y)
#     else:
#         print(x - 1, y)
#         print(x + 1, y)

# Задача12

# n = int(input())
# m = int(input())
# k = int(input())
# if k <= n*m:
#     if k % n == 0 or k % m == 0:
#         print('YES')
#     else:
#         print('NO')


# Задача13 Римские цифры

# Задача14 IP адрес

# Задача15

sum = 0
element = int(input())
while element != 0:
    sum += element
    element = int(input())
print(sum)
