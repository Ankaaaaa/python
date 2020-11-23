class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.color, self.name, 'машина поехала прямо')

    def stop(self):
        print(self.color, self.name, 'машина остановилась')

    def turn(self, turn):
        print('машина повернула', turn)

    def show_speed(self):
        print('скорость автомобиля', self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('превышение скорости на ', self.speed - 60)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def sport(self):
        print('запуск метода из класса SportCar')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('превышение скорости на ', self.speed - 40)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        print('запуск метода из класса PoliceCar')
print('class Car')
b = Car (100, 'red', 'BMW', True)
b.show_speed()
print(30*'---')
print('class TownCar')
a = TownCar(90, 'black', 'BMW', False)
a.show_speed()
a.stop()
print(30*'---')
print('class WorkCar')
c = WorkCar(50, 'grean', 'BMW', False)
c.show_speed()
c.turn('налево')
print(30*'---')
print('class PoliceCar')
d = PoliceCar(50, 'grean', 'BMW', False)
d.police()
d.show_speed()
d.turn('направо')
