class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = sum({'wage': wage, 'bonus': bonus}.values())


class Position(Worker):
    def get_full_name(self):
        return f'Имя и Фамилия: {self.name} {self.surname}.'

    def get_total_income(self):
        return f'Зарплата в рублях: {self._income}.'


worker_1 = Position('Иван', 'Иванов', 'Бухгалтер', 70000, 30000)
print(f'Должность: {worker_1.position}.')
print(worker_1.get_full_name())
print(worker_1.get_total_income())
