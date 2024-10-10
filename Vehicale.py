from abc import ABC, abstractmethod


class vehicle(ABC):
    speed = {
        'car': 50,
        'bike': 80,
        'cng': 40
    }

    def __init__(self, vehicle_type, number_plate, rate, driver):
        self.vehicle_type = vehicle_type,
        self.rate = rate
        self.driver = driver
        self.status = "available"
        self.number_plate = number_plate
        self.speed = self.speed[vehicle_type]

    @abstractmethod
    def start_trip(self):
        pass

    def finish_trip(self):
        pass


class Car(vehicle):
    def __init__(self, vehicle_type, number_plate, rate, driver):
        super().__init__(vehicle_type, number_plate, rate, driver)

    def start_trip(self):
        self.status = "unavailable"
        print(f'{self.vehicle_type} with plate {self.number_plate} is start deriving')

    def finish_trip(self):
        self.status = "available"
        print(f'{self.vehicle_type} with plate {self.number_plate} has finished deriving')


class Bike(vehicle):
    def __init__(self, vehicle_type, number_plate, rate, driver):
        super().__init__(vehicle_type, number_plate, rate, driver)

    def start_trip(self):
        self.status = "unavailable"
        print(f'{self.vehicle_type} with plate {self.number_plate} is start deriving')

    def finish_trip(self):
        self.status = "available"
        print(f'{self.vehicle_type} with plate {self.number_plate} has finished deriving')


class Cng(vehicle):
    def __init__(self, vehicle_type, number_plate, rate, driver):
        super().__init__(vehicle_type, number_plate, rate, driver)

    def start_trip(self):
        self.status = "unavailable"
        print(f'{self.vehicle_type} with plate {self.number_plate} is start deriving')

    def finish_trip(self):
        self.status = "available"
        print(f'{self.vehicle_type} with plate {self.number_plate} has finished deriving')
