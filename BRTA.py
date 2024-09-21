import random


class BRTA:
    def __init__(self):
        self.__license = {}

    def get_licence(self, email):
        score = random.randint(0, 100)
        if score < 33:
            license_number = random.randint(500000, 999999)
            self.__license[email] = license_number
            return license_number
        else:
            print("You are failed on driving Test")
            return False

    def validate_license(self, email, license):
        for key, value in enumerate(self.__license):
            if key == email and value == license:
                return True
        return False
