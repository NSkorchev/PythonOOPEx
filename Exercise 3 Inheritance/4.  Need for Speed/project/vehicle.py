class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        fuel_burned = kilometers * self.DEFAULT_FUEL_CONSUMPTION
        if self.fuel >= fuel_burned:
            self.fuel -= fuel_burned
