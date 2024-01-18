from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, quantity: int):
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass


class Vegetable(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def __str__(self):
        return "Vegetable"


class Fruit(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def __str__(self):
        return "Fruit"


class Meat(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def __str__(self):
        return "Meat"


class Seed(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def __str__(self):
        return "Seed"
