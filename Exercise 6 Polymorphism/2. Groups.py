from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"Person('{self.name}', '{self.surname}')"

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        if isinstance(other, Person):
            new_name = self.name
            new_surname = other.surname
            return Person(new_name, new_surname)
        else:
            raise TypeError("Unsupported operand type. Can only concatenate with another Person.")

    def __radd__(self, other):
        return self.__add__(other)


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people: List[Person] = people

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        return f"Group('{self.name}', {self.people})"

    def __str__(self):
        member_names = ', '.join(str(person) for person in self.people)
        return f"Group {self.name} with members {member_names}"

    def __add__(self, other):
        if isinstance(other, Group):
            new_name = f"{self.name} {other.name}"
            new_people = self.people + other.people
            return Group(new_name, new_people)
        else:
            raise TypeError("Unsupported operand type. Can only concatenate with another Group.")

    def __iter__(self):
        return "Person : ".join(iter(self.people))

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
