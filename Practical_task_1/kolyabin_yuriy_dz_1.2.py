print('Старт')
lst_nums = []
for i in range(1, 1000):
    if i % 2 != 0:
        num = i ** 3
        lst_nums.append(num)
sum_digits = 0
sum_nums = 0
for i in lst_nums:
    number = i
    while number > 0:
        digit = number % 10
        sum_digits += digit
        number = number // 10
    if sum_digits % 7 == 0:
        sum_nums += i
        sum_digits = 0
    else:
        sum_digits = 0
        continue
print('Сумма чисел из данного списка, сумма цифр которых делится на 7: ', sum_nums)
sum_nums = 0
for i in lst_nums:
    number = i + 17
    while number > 0:
        digit = number % 10
        sum_digits += digit
        number = number // 10
    if sum_digits % 7 == 0:
        sum_nums += i + 17
        sum_digits = 0
    else:
        sum_digits = 0
        continue
print('К каждому элементу списка добавили 17 и нашлась сумма тех чисел из списка, сумма цифр которых делится на 7: ',
      sum_nums)
print('Задание выполнено.')
