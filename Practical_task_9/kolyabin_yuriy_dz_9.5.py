class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}. Запуск отсортировки.')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}. Запуск отсортировки Pen.')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}. Запуск отсортировки Pencil.')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}. Запуск отсортировки Handle.')


pen = Pen('тетрадь')
pen.draw()
pencil = Pencil('блокнот')
pencil.draw()
handle = Handle('доска')
handle.draw()
stat = Stationery('магазин')
stat.draw()
