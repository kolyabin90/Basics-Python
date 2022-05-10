class IsNotDigit(ValueError):
    pass


nums = list()
while True:
    try:
        enter = input('Введите число. Если захотите остановиться, введите "stop": ')
        if enter == 'stop':
            break
        if enter.isdigit() or enter.replace('.', '').isdigit():
            nums.append(float(enter))
        else:
            raise IsNotDigit(enter)
    except IsNotDigit as x:
        print(f'"{x}" не является числом!')
print(nums)
