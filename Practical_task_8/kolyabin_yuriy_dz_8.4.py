from functools import wraps


def val_checker(callback):
    def _checker(func):
        @wraps(func)
        def wrapper(*args):
            for x in args:
                if not callback(x):
                    raise ValueError(f'wrong value: {x}')
            return func(*args)

        return wrapper

    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
a = calc_cube(-5)
print(a)
