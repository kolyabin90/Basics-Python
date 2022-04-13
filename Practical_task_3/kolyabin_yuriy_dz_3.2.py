DIGITS = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
          'four': 'четыре', 'five': 'пять', 'six': 'шесть',
          'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(x):
    if x.istitle():
        return DIGITS.get(x.lower()).title()
    return DIGITS.get(x)


print(num_translate_adv('ten'))
print(num_translate_adv('One'))
print(num_translate_adv('twenty'))
