class MyError(ZeroDivisionError):
    pass


try:
    number = int(input("567 мы хотим поделить на: "))
    if number == 0:
        raise MyError(f'{MyError.__name__}')
    result = 567 / number
except MyError as err:
    print(f"{err} Ай-я-яй... На ноль делить нельзя!")
except ValueError as err:
    print(f"{err} Вы что-то не то ввели...")
except NameError as err:
    print(f"{err} Как мы на это делить будем? Так не пойдет!")
except KeyboardInterrupt as err:
    print(f"{err} Такое тоже может быть.")
except Exception as err:
    print(f"{err} Ну это уже на всякий случай.")
else:
    print(result)
