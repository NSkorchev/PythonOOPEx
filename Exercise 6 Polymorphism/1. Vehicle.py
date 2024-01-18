from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: int):
        consumed_fuel = (self.fuel_consumption + 0.9) * distance
        if consumed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= consumed_fuel

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: int):
        consumed_fuel = (self.fuel_consumption + 1.6) * distance
        if consumed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= consumed_fuel

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * 0.95
