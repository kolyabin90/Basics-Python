import time


class TrafficLight:
    __color = 'off'

    def running(self):
        counter = 1
        while counter <= 3:
            self.__color = 'RED'
            print(f'Stop! {self.__color}!')
            time.sleep(7)
            self.__color = 'YELLOW'
            print(f'Get ready! {self.__color}!')
            time.sleep(2)
            self.__color = 'GREEN'
            print(f'Go! {self.__color}!')
            time.sleep(2)
            self.__color = 'YELLOW'
            print(f'Get ready! {self.__color}!')
            time.sleep(1)
            counter += 1


result = TrafficLight()
result.running()
