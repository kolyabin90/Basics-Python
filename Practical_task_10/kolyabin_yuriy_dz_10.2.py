from abc import ABC, abstractmethod


class Clothes(ABC):
    expense = 0

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size
        Coat.expense += self.consumption

    def __str__(self):
        return f'Для польто ткани необходимо: {self.consumption:.3f} см^2. Израсходовано {self.expense}см^2.'

    @property
    def consumption(self):
        cons = self.size / 6.5 + 0.5
        return float(f'{cons:.3f}')


class Suit(Clothes):
    def __init__(self, growth):
        super().__init__()
        self.growth = growth
        Suit.expense += self.consumption

    def __str__(self):
        return f'Для костюма ткани необходимо: {self.consumption:.3f} см^2. Израсходовано {self.expense}см^2.'

    @property
    def consumption(self):
        cons = 2 * self.growth + 0.3
        return float(f'{cons:.3f}')


coat = Coat(60)
print(coat)
suit = Suit(180)
print(suit)
coat_2 = Coat(58)
print(coat_2)
suit_2 = Suit(167)
print(suit_2)
