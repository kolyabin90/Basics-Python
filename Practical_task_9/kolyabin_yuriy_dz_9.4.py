class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.name}, go!')
        self.show_speed()

    def stop(self):
        print(f'{self.name}, stop.')
        self.speed = 0
        self.show_speed()

    def turn(self, direction):
        if direction.lower() == 'left' or direction.lower() == 'right':
            print(f'{self.name} turned {direction}.')
        else:
            print(f"You made a spelling mistake '{direction}'. {self.name} didn't turn around.")
        self.show_speed()

    def show_speed(self):
        if self.speed == 0:
            print(f'The {self.name} stopped. Speed {self.speed} km/h.')
        else:
            print(f'The {self.name} is moving at a speed of {self.speed} km/h.')


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        super().show_speed()
        if self.speed > self.speed_limit:
            print(f'Bringing the speed to {self.speed - self.speed_limit}!!!')


class SportCar(Car):
    pass


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        super().show_speed()
        if self.speed > self.speed_limit:
            print(f'Bringing the speed to {self.speed - self.speed_limit}!!!')


class PoliceCar(Car):
    is_police = True


auto_1 = TownCar(65, 'yellow', 'Volkswagen')
auto_1.go()
auto_1.turn('Righht')
auto_1.stop()
auto_2 = SportCar(170, 'red', 'Ferrari')
auto_2.go()
auto_2.turn('Right')
auto_2.stop()
auto_3 = WorkCar(42, 'white', 'Renault')
auto_3.go()
auto_3.turn('left')
auto_3.stop()
auto_4 = PoliceCar(80, 'blue', 'Lada')
auto_4.go()
auto_4.turn('LEFT')
auto_4.stop()
