import random


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # Methods
    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn(self):
        return f'{self.name} is turned {random.choice(["left", "right"])}'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed} km/h'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Attention! {self.name}! Exceeding the speed limit!\n{super().show_speed()}'
        else:
            return super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Attention! {self.name}! Exceeding the speed limit!\n{super().show_speed()}'
        return super().show_speed()


class PoliceCar(Car):
    pass


town_car = TownCar(60, 'White', 'MINI COOPER COUNTRYMAN')
sport_car = SportCar(250, 'Yellow', 'Lamborghini Huracan')
work_car = WorkCar(80, 'Rouge Arden', 'Citroen Berlingo')
polce_car = PoliceCar(180, 'Black', 'Chevrolet Tahoe SSV', True)

print(town_car.go())
print(town_car.show_speed())
print(f'{sport_car.name} is {sport_car.color}')
print(sport_car.turn())
print(f'{polce_car.name} is {polce_car.is_police} police car')
print(work_car.show_speed())
print(work_car.stop())
