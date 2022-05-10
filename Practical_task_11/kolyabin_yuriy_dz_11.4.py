import json


class Stock:
    def __init__(self):
        self.stock = {}
        self.other_stock = {}
        self.count_printers = 0
        self.count_scanners = 0
        self.count_copiers = 0

    def count_equip(self, param):

        """Функция считает экземпляры оргтехники поступивших на склад"""

        if param.type_equip() == 'Printer':
            self.count_printers += 1
            return self.count_printers
        if param.type_equip() == 'Scanner':
            self.count_scanners += 1
            return self.count_scanners
        if param.type_equip() == 'Xerox':
            self.count_copiers += 1
            return self.count_copiers

    def add_to_stock(self, param):

        """Функция добавляет на склад экземпляр оргтехники сортируя по категириям"""

        self.count_equip(param)
        if param.type_equip() not in self.stock:
            self.stock.setdefault(param.type_equip(), [])
        return self.stock[param.type_equip()].append(param.add_stock())

    def trasfer(self, name_equip, name):

        """Функция перемещает экземпляр оргтехники на другой склад"""

        if name_equip not in self.other_stock:
            self.other_stock.setdefault(name_equip, [])
        for eq in self.stock[name_equip]:
            if eq['name'] == name:
                self.other_stock[name_equip].append(eq)
                return self.stock[name_equip].remove(eq)


class OfficeEquipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.type_eq = f'{self.__class__.__name__}'

    def type_equip(self):
        return f'{self.type_eq}'


class Printer(OfficeEquipment):
    def __init__(self, name, price, type_printer):
        super().__init__(name, price)
        self.type_printer = type_printer

    def add_stock(self):
        add_printer = {'name': self.name, 'price': self.price, 'type': self.type_printer}
        return add_printer


class Scanner(OfficeEquipment):
    def __init__(self, name, price, type_scan):
        super().__init__(name, price)
        self.type_scan = type_scan

    def add_stock(self):
        add_scanner = {'name': self.name, 'price': self.price, 'type': self.type_scan}
        return add_scanner


class Xerox(OfficeEquipment):
    def __init__(self, name, price, speed_copy):
        super().__init__(name, price)
        self.speed_copy = speed_copy

    def add_stock(self):
        add_xerox = {'name': self.name, 'price': self.price, 'type': self.speed_copy}
        return add_xerox


stock_new = Stock()
printer_1 = Printer('Canon Pixma TS304', 9055, 'струйный')
stock_new.add_to_stock(printer_1)
printer_2 = Printer('Xerox B400DN', 99635, 'лазерный')
stock_new.add_to_stock(printer_2)
printer_3 = Printer('KYOCERA 1102VB3RU0', 54350, 'лазерный')
stock_new.add_to_stock(printer_3)
scanner_1 = Scanner('Epson WorkForce DS-30', 17041, 'протяжный')
stock_new.add_to_stock(scanner_1)
scanner_2 = Scanner('Canon Formula DR-C225W II', 89919, 'протяжный')
stock_new.add_to_stock(scanner_2)
scanner_3 = Scanner('HP Scanlet Pro 4500 fn1', 131892, 'планшетный')
stock_new.add_to_stock(scanner_3)
xerox_1 = Xerox('Xerox B205', 44444, '40 стр/мин')
stock_new.add_to_stock(xerox_1)
xerox_2 = Xerox('Xerox WC3345DNI', 33333, '30 стр/мин')
stock_new.add_to_stock(xerox_2)
xerox_3 = Xerox('Xerox 3025v', 22222, '20 стр/мин')
stock_new.add_to_stock(xerox_3)
print(json.dumps(stock_new.stock, ensure_ascii=False, indent=2))
print(f'Количество принтеров доставленых на склад: {stock_new.count_printers}')
stock_new.trasfer("Printer", 'Xerox B400DN')
print(json.dumps(stock_new.other_stock, ensure_ascii=False, indent=2))
print(json.dumps(stock_new.stock, ensure_ascii=False, indent=2))
