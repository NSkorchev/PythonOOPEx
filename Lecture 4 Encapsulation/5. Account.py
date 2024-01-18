from typing import Union


class Account:
    
    def __init__(self, id: int, balance: float, pin: int):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin: int) -> Union[str, int]:
        if self.__pin == pin:
            return self.__id

        return "Wrong pin"

    def change_pin(self, old_pin: int, new_pin: int) -> str:
        if old_pin == self.__pin:
            self.__pin = new_pin

        return "Pin changed"
