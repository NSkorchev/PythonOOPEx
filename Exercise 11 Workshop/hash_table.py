class HashTable:

    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity
        self.__values = [None] * self.__max_capacity

    def __setitem__(self, key, value):
        index = self.__calc_index(key)

        self.__keys[index] = key
        self.__values[index] = value

    def __calc_index(self, key):
        index = sum(ord(c) for c in key) % self.__max_capacity
        index = self.__get_index(index)

        return index

    def __get_index(self, index):
        while True:
            if self.__keys[index % self.__max_capacity] is None:
                return index % self.__max_capacity

            index += 1


table = HashTable()
table["name"] = "Peter"
table["age"] = 25
table["is_pet_owner"] = True
table["is_driver"] = False
# print(table)
# print(table.get("name"))
# print(table["age"])
# print(len(table))
