print('Старт')
for i in range(1, 101):
    if i % 10 == 1:
        if i == 11:
            print(i, 'процентов')
            continue
        print(i, 'процент')
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        if i == 12 or i == 13 or i == 14:
            print(i, 'процентов')
            continue
        print(i, 'процента')
    elif i % 10 == 5:
        print(i, 'процентов')
    elif i % 10 == 6:
        print(i, 'процентов')
    elif i % 10 == 7:
        print(i, 'процентов')
    elif i % 10 == 8:
        print(i, 'процентов')
    elif i % 10 == 9:
        print(i, 'процентов')
    elif i % 10 == 0:
        print(i, 'процентов')
print('Задание выполнено.')
