
# проверка на високосность)
# year = int(input('Введите год: '))
# if year % 4 != 0:
#     print('Год не високосный.')
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print('Год високосный.')
#     else:
#         print('Год не високосный.')
# else:
#     print('Год високосный')


def vis_years(years):
    list_years = []
    for year in years:
        if year % 4 != 0:
            continue
        elif year % 100 == 0:
            if year % 400 == 0:
                list_years.append(year)
        else:
            list_years.append(year)
    return list_years

print(vis_years([1996, 1901, 1971, 2020, 2024]))