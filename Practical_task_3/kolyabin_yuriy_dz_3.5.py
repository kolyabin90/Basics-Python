import random


def get_joker(n):
    """
    Функция выдает n количество шуток
    """

    nouns = ['лес', 'город', 'космос', 'океан', 'проспект']
    adverbs = ['сейчас', 'завтра', 'в среду', 'вчера', 'после обеда']
    adjectives = ['зеленый', 'шершавый', 'ароматный', 'квадратный', 'мягкий']
    random.shuffle(nouns)
    random.shuffle(adverbs)
    random.shuffle(adjectives)
    result = []
    for i, (nouns, adverbs, adjectives) in enumerate(zip(nouns, adverbs, adjectives)):
        result.append(f'{nouns} {adverbs} {adjectives}')
        if i == n:
            break
    return result


print(get_joker(4))
