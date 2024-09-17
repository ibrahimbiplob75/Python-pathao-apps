import hashlib


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
        self.earning = 0

    def start_a_trip(self, destination, fare):
        self.earning += destination
        self.location=destination


customer1 = Users("Ibrahim", "ibrahim75@gmail.com", "*123Ab#")
Users.log_in("ibrahim75@gmail.com", "*123Ab#")
