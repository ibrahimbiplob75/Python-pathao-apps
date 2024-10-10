import random


class BRTA:
    def __init__(self):
        self.__license = {}

    def get_licence(self, email):
        score = random.randint(0, 100)
        if score > 33:
            print("You passed on driving Test .your Score is", score)
            license_number = random.randint(500000, 999999)
            self.__license[email] = license_number
            return license_number
        else:
            print("You are failed on driving Test .your Score is",score)
            return False

    def validate_license(self, email, licence):
        for key, value in self.__license.items():
            print(key,value)
            if key == email and value == licence:
                return True
        return False
