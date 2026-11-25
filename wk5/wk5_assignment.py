from abc import ABC, abstractmethod


# Task 1: Abstract Base Class
class Vehicle(ABC):

    def __init__(self, vehicle_id, model, daily_rate):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__daily_rate = daily_rate

        if daily_rate <= 0:
            raise ValueError("Daily rental rate must be greater than 0.")

    # Task 2: Getter method
    def get_daily_rate(self):
        return self.__daily_rate

    # Task 2: Setter method
    def set_daily_rate(self, daily_rate):
        if daily_rate <= 0:
            raise ValueError("Daily rental rate must be greater than 0.")

        self.__daily_rate = daily_rate

    # Abstract method
    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    # Operator overloading: compare vehicles by daily rate
    def __lt__(self, other):
        return self.get_daily_rate() < other.get_daily_rate()


# Task 3: PassengerCar child class
class PassengerCar(Vehicle):

    def __init__(self, vehicle_id, model, daily_rate, num_seats):
        super().__init__(vehicle_id, model, daily_rate)
        self.num_seats = num_seats

    # Method overriding
    def calculate_rental_cost(self, days):
        return (self.get_daily_rate() * days) + (15.0 * self.num_seats)

    # String operator overloading
    def __str__(self):
        return (
            f"Passenger Car | ID: {self.vehicle_id} | "
            f"Model: {self.model} | Seats: {self.num_seats} | "
            f"Daily Rate: ${self.get_daily_rate():.2f}"
        )


# Task 3: CargoTruck child class
class CargoTruck(Vehicle):

    def __init__(self, vehicle_id, model, daily_rate, cargo_capacity_tons):
        super().__init__(vehicle_id, model, daily_rate)
        self.cargo_capacity_tons = cargo_capacity_tons

    # Method overriding
    def calculate_rental_cost(self, days):
        return (self.get_daily_rate() * days) + (50.0 * self.cargo_capacity_tons)

    # String operator overloading
    def __str__(self):
        return (
            f"Cargo Truck | ID: {self.vehicle_id} | "
            f"Model: {self.model} | Capacity: {self.cargo_capacity_tons} tons | "
            f"Daily Rate: ${self.get_daily_rate():.2f}"
        )


# Task 4: Polymorphic processing
def generate_fleet_manifest(fleet_list, days):

    print("\n========== FLEET RENTAL MANIFEST ==========")

    for vehicle in fleet_list:
        print(vehicle)
        print(f"Rental Duration: {days} days")
        print(f"Total Rental Cost: ${vehicle.calculate_rental_cost(days):.2f}")
        print("-------------------------------------------")


# Creating vehicle objects
car1 = PassengerCar("CAR101", "Toyota Corolla", 50.0, 5)
car2 = PassengerCar("CAR102", "Honda Civic", 60.0, 4)

truck1 = CargoTruck("TRK201", "Volvo FH", 120.0, 10.5)
truck2 = CargoTruck("TRK202", "Tata Prima", 100.0, 8.0)


# Creating a mixed fleet
fleet = [car1, truck1, car2, truck2]


# Display fleet manifest for 3 days
generate_fleet_manifest(fleet, 3)


# Sorting vehicles by daily rental rate
print("\n========== VEHICLES SORTED BY DAILY RATE ==========")

sorted_fleet = sorted(fleet)

for vehicle in sorted_fleet:
    print(vehicle)


# Demonstrating getter and setter
print("\n========== RATE UPDATE ==========")

print("Old daily rate:", car1.get_daily_rate())

car1.set_daily_rate(55.0)

print("Updated daily rate:", car1.get_daily_rate())


# Demonstrating invalid rate validation
print("\n========== INVALID RATE TEST ==========")

try:
    car1.set_daily_rate(-10)
except ValueError as error:
    print("Error:", error)
