class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size  # 100
        self.quantity = quantity  # 50

    def fill(self, quantity):  # 40
        if (self.size - self.quantity) >= quantity:
            self.quantity += quantity
            return self.size

    def status(self):
        cup_status = self.size - self.quantity
        return cup_status


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())