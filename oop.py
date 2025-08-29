# ------------------------------
# Assignment 1: Smartphone Class 
# ------------------------------

# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.model} is calling {number}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

# Subclass: GamingPhone inherits from Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, refresh_rate):
        super().__init__(brand, model, storage)
        self.refresh_rate = refresh_rate

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.model} at {self.refresh_rate}Hz refresh rate!")

# Creating smartphone objects
phone1 = Smartphone("Samsung", "Galaxy A52", 128)
phone2 = GamingPhone("ASUS", "ROG Phone 5", 256, 144)

# Using the methods
phone1.info()
phone1.call("234-456-7890")

phone2.info()
phone2.call("987-654-3210")
phone2.play_game("Asphalt 9")

# ------------------------------
# Activity 2: Polymorphism with Vehicles 🚗✈️🛳️
# ------------------------------

# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves.")

# Subclasses
class Car(Vehicle):
    def move(self):
        print("The car is driving. 🚗")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying. ✈️")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing. 🛳️")

# List of vehicles
vehicles = [Car(), Plane(), Boat()]

# Loop through each and call move()
print("\nVehicle Movements:")
for v in vehicles:
    v.move()
