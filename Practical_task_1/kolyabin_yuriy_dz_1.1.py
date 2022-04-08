print("Старт")
try:
    duration = int(input('Введите число: '))
    if duration < 0:
        print('Введите число больше или равное нулю.')
    elif duration in range(0, 60):
        print(duration, 'сек.')
    elif duration in range(60, 3600):
        minutes = duration // 60
        seconds = duration % 60
        print(minutes, 'мин', seconds, 'сек')
    elif duration in range(3600, 86400):
        hours = duration // 3600
        minutes = duration % 3600
        seconds = minutes % 60
        minutes = minutes // 60
        print(hours, 'час', minutes, 'мин', seconds, 'сек')
    elif duration > 86400:
        days = duration // 86400
        hours = duration % 86400
        minutes = duration % 3600
        seconds = minutes % 60
        hours = hours // 3600
        minutes = minutes // 60
        print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
except ValueError:
    print('Вы ввели текст или ничего не ввели.')
print('Задание выполнено.')
