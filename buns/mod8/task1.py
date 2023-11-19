class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed >= 0:
            self._speed = speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if year >= 0:
            self._year = year

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    def __str__(self):
        return f"Координаты: {self.coordinates}, Скорость: {self.speed}, Марка: {self.brand}, Год выпуска: {self.year}, Номер: {self.number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return pos_x <= self.coordinates[0] <= pos_x + length and pos_y <= self.coordinates[1] <= pos_y + width


class Passenger():
    def __init__(self, passengers_capacity, number_of_passengers):
        self.__passengers_capacity = passengers_capacity
        self.__number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if passengers_capacity >= 0:
            self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if number_of_passengers >= 0:
            self.__number_of_passengers = number_of_passengers

class Cargo():
    def __init__(self, carrying):
        self.__carrying = carrying
    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if carrying >= 0:
            self.__carrying = carrying

class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height >= 0:
            self._height = height

    def __str__(self):
        return f"Координаты: {self.coordinates}, Скорость: {self.speed}, Марка: {self.brand}, Год выпуска: {self.year}, Номер: {self.number}, Высота полёта: {self.height} м"


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)

class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    def __str__(self):
        return f"Координаты: {self.coordinates}, Скорость: {self.speed}, Марка: {self.brand}, Год выпуска: {self.year}, Номер: {self.number}, Название порта: {self.port}"

class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)

class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

    def __str__(self):
        return f"Координаты: {self.coordinates}, Скорость: {self.speed}, Марка: {self.brand}, Год выпуска: {self.year}, Номер: {self.number}, Вместимость: {self.passengers_capacity} пассажиров, Количество пассажиров: {self.number_of_passengers}"
class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)

    def __str__(self):
        return f"Координаты: {self.coordinates}, Скорость: {self.speed}, Марка: {self.brand}, Год выпуска: {self.year}, Номер: {self.number}, Ограничение по перевозке: {self.carrying} кг"

class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)

class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

    def __str__(self):
        return f"Координаты: {self.coordinates}, Скорость: {self.speed}, Марка: {self.brand}, Год выпуска: {self.year}, Номер: {self.number}, Название порта: {self.port}, Вместимость: {self.passengers_capacity} пассажиров, Количество пассажиров: {self.number_of_passengers}"

class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)

    def __str__(self):
        return f"Координаты: {self.coordinates}, Скорость: {self.speed}, Марка: {self.brand}, Год выпуска: {self.year}, Номер: {self.number}, Название порта: {self.port}, Ограничение по перевозке: {self.carrying} кг"

class Airplane(Plane):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number, height)

class PassengerPlane(Plane, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

    def __str__(self):
        return f"Координаты: {self.coordinates}, Скорость: {self.speed}, Марка: {self.brand}, Год выпуска: {self.year}, Номер: {self.number}, Высота полёта: {self.height} м, Вместимость: {self.passengers_capacity} пассажиров, Количество пассажиров: {self.number_of_passengers}"


class CargoPlane(Plane, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, height, carrying):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Cargo.__init__(self, carrying)

    def __str__(self):
        return f"Координаты: {self.coordinates}, Скорость: {self.speed}, Марка: {self.brand}, Год выпуска: {self.year}, Номер: {self.number}, Высота полёта: {self.height} м, Ограничение по перевозке: {self.carrying} кг"

"""
Этот класс не работает так, как надо из-за проблемы "ромбовидного" или же "алмазного" наследования
К сожалению, я не разобралась как решить эту задачу используя классы Plane и Ship одновременно

class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port):
        super().__init__(coordinates, speed, brand, year, number, height)
        self.port = port

    def __str__(self):
        return f"Координаты: {self.coordinates}, Скорость: {self.speed}, Марка: {self.brand}, Год выпуска: {self.year}, Номер: {self.number}, Высота полёта: {self.height} м, Название порта: {self.port}"        
"""
class Seaplane(Plane): #этот класс будет работать, однако он не совсем подходит под требования, данные в задаче
    def __init__(self, coordinates, speed, brand, year, number, height, port):
        super().__init__(coordinates, speed, brand, year, number, height)
        self.port = port

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    def __str__(self):
        return f"Координаты: {self.coordinates}, Скорость: {self.speed}, Марка: {self.brand}, Год выпуска: {self.year}, Номер: {self.number}, Высота полёта: {self.height} м, Название порта: {self.port}"

transport = Transport([0, 0], 100, "Toyota", 2010, "ABC123")

passenger = Passenger(50, 30)

cargo = Cargo(5000)

plane = Plane([1000, 1000], 500, "Boeing", 2015, "XYZ789", 10000)

auto = Auto([500, 500], 80, "BMW", 2012, "DEF456")

ship = Ship([2000, 2000], 200, "Titanic", 1912, "GHI789", "Southampton")

car = Car([100, 100], 60, "Ford", 2008, "JKL012")

bus = Bus([300, 300], 70, "Mercedes", 2013, "MNO345", 40, 25)

cargoAuto = CargoAuto([800, 800], 90, "Volvo", 2016, "PQR678", 3000)

boat = Boat([30, 40], 30, "River", 2005, "BOAT01", "River Port")

passenger_ship = PassengerShip([60, 60], 50, "Sea Ship", 2010, "PAS01", "Sea Port", 200, 150)

cargo_ship = CargoShip([0, 0], 40, "CargoShip1", 2000, "EE7890", "London", 5000)

airplane = Airplane([0, 10], 700, "Boeing", 2018, "FF2345", 12000)

passenger_plane = PassengerPlane([30, 30], 300, "PassengerPlaneBrand", 2010, "JKL012", 10000, 200, 150)

cargo_plane = CargoPlane([40, 40], 400, "CargoPlaneBrand", 2005, "MNO345", 15000, 5000)

seaplane = Seaplane([50, 50], 200, "SeaplaneBrand", 2015, "PQR678", 5000, "Port")

print(transport)
print(passenger)
print(cargo)
print(plane)
print(auto)
print(ship)
print(car)
print(bus)
print(cargoAuto)
print(boat)
print(passenger_ship)
print(cargo_ship)
print(airplane)
print(passenger_plane)
print(cargo_plane)
print(seaplane)

