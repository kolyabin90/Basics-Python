DIGITS = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
          'four': 'четыре', 'five': 'пять', 'six': 'шесть',
          'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(x):
    return DIGITS.get(x)


print(num_translate('six'))
print(num_translate('nine'))
print(num_translate('twelve'))
