import copy


class Person:

    def __init__(self, position):
        self.position = position


class FreePerson(Person):

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False

    def move(self, distance):
        new_position = [self.position[0] + distance, self.position[1] + distance]
        if self.is_free or self.within_prison(new_position):
            self.position = new_position

    @staticmethod
    def within_prison(position):
        return 0 <= position[0] <= 6 and 0 <= position[1] <= 6


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")
try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass
print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")
