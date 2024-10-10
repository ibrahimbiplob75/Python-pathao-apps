class RideManager:
    def __init__(self):
        print("Ride manager activated")
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cng = []

    def add_a_vehicle(self, vehicle_type, vehicle):
        print("Type",vehicle.number_plate)
        if vehicle_type == "car":
            self.__available_cars.append(vehicle)
        elif vehicle_type == "bike":
            self.__available_bikes.append(vehicle)

        elif vehicle_type == "cng":
            self.__available_cng.append(vehicle)

    def match_a_vehicle(self):
        pass


uber = RideManager()
