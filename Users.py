import hashlib
import random

from BRTA import BRTA
from Vehicale import Car, Bike, Cng
from RideManager import uber

license_authority = BRTA()


class Users:
    def __init__(self, name, email, password):
        self.name = name,
        self.email = email,
        self.password = password
        password_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open("user.txt", "w") as file:
            file.write(f'{email} {password_encrypted}')
            file.close()
            print(self.name, f'email -> {email} password-> {password_encrypted}')

    @staticmethod
    def log_in(email, password):
        stored_pass = "",
        with open("user.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    print("email have ", line)
                    stored_pass = line.split(" ")[1]
                else:
                    print("email did not match")

        file.close()
        user_pass = hashlib.md5(password.encode()).hexdigest()

        if user_pass == stored_pass:
            print("Valid user")
            return True
        else:
            print("Vul info")
            return False


class Rider(Users):
    def __init__(self, name, email, password, location, balance):
        self.location = location,
        self.balance = balance,
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        self.location = destination

    def start_a_trip(self, fare):
        self.balance -= fare


class Driver(Users):
    def __init__(self, name, email, password, locations, licence):
        super().__init__(name, email, password)
        self.location = locations
        self.licence = licence
        self.valid_driver = license_authority.validate_license(email, licence)
        self.earning = 0

    def attend_driving_test(self):
        result = license_authority.get_licence(self.email)
        if result != False:
            self.licence = result
            self.valid_driver = True
        else:
            print("Your Lisense is Failed")

    def register_a_vehicle(self, vehicle_type, number_plate, rate):
        if self.valid_driver is True:
            if vehicle_type in ['car', 'bike', 'cng']:
                new_vehicle = Car(vehicle_type, number_plate, rate, self.email)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                print("You chose the wrong Vehicle type")
        else:
            print("You are not valid, Take a Driving Test Again")

    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination


# customer1 = Users("Ibrahim", "ibrahim75@gmail.com", "*123Ab#")
# Users.log_in("ibrahim75@gmail.com", "*123Ab#")
#
# kobir = Driver("Kobir Mia", "kobir@gmail.com", "12345", "Mohammadpur", 456344)
# kobir_check = license_authority.validate_license(kobir.email, kobir.licence)
# print(kobir_check)
# kobir.attend_driving_test()
# kobir_check = license_authority.validate_license(kobir.email, kobir.licence)
# print(kobir_check)

rider1 = Rider("Ibrahim", "ibrahim@gmail.com", "1234", random.randint(0, 100), 2000)
rider2 = Rider("biplob", "biplob@gmail.com", "12345", random.randint(0, 100), 2400)
rider3 = Rider("Jakir", "Jakir@gmail.com", "123", random.randint(0, 100), 2700)

driver1 = Driver("Driver1", "driver1@gmail.com", "123", random.randint(0, 100), 138456)
driver1.attend_driving_test()
driver1.register_a_vehicle("bike", 1384, 10)
# driver2 = Driver("Driver2", "driver2@gmail.com", "456", random.randint(0, 100), 138457)
# driver3 = Driver("Driver3", "driver3@gmail.com", "789", random.randint(0, 100), 138458)
