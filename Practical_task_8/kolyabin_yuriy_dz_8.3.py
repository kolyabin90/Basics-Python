from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args):
        for x in args:
            print(f'{x}: {type(x)}', end=', ')
            if x == args[-1]:
                print('')
        for x in args:
            if x != args[-1]:
                print(callback(x))
        return callback(args[-1])

    return wrapper


@type_logger
def calc_logger(x):
    return x ** 3


print(calc_logger(2, 3.5, -6))
a = calc_logger(5)
print(a)
