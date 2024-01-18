from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            animal_type = type(animal).__name__
            return f"{animal.name} the {animal_type} added to the zoo"

        elif price > self.__budget and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        is_capacity_left = self.__workers_capacity > len(self.workers)
        if is_capacity_left:
            self.workers.append(worker)
            worker_type = type(worker).__name__
            return f"{worker.name} the {worker_type} hired successfully"

        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        salaries = sum([s.salary for s in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        animal_care = sum([a.money_for_care for a in self.animals])
        if self.__budget >= animal_care:
            self.__budget -= animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = [leo for leo in self.animals if leo.__class__.__name__ == 'Lion']
        tigers = [t for t in self.animals if t.__class__.__name__ == 'Tiger']
        cheetahs = [c for c in self.animals if c.__class__.__name__ == 'Cheetah']

        lion_reprs = [repr(lion) for lion in lions]
        tiger_reprs = [repr(tiger) for tiger in tigers]
        cheetah_reprs = [repr(cheetah) for cheetah in cheetahs]

        lions_str = " ".join(lion_reprs)
        tigers_str = " ".join(tiger_reprs)
        cheetahs_str = " ".join(cheetah_reprs)

        return f"You have {len(self.animals)} animals\n"\
               f"----- {len(lion_reprs)} Lions:\n"\
               f"{lions_str}\n" \
               f"----- {len(tiger_reprs)} Tigers:\n" \
               f"{tigers_str}\n" \
               f"----- {len(cheetah_reprs)} Cheetahs:\n" \
               f"{cheetahs_str}"

    def workers_status(self):
        caretakers = [c for c in self.workers if c.__class__.__name__ == 'Caretaker']
        vets = [v for v in self.workers if v.__class__.__name__ == 'Vet']
        keepers = [k for k in self.workers if k.__class__.__name__ == 'Keeper']

        caretakers_reprs = [repr(caretaker) for caretaker in caretakers]
        vets_reprs = [repr(vet) for vet in vets]
        keepers_reprs = [repr(keeper) for keeper in keepers]

        caretakers_str = " ".join(caretakers_reprs)
        vets_str = " ".join(vets_reprs)
        keepers_str = " ".join(keepers_reprs)

        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers_reprs)} Keepers:\n" \
               f"{keepers_str}\n" \
               f"----- {len(caretakers_reprs)} Caretakers:\n" \
               f"{caretakers_str}\n" \
               f"----- {len(vets_reprs)} Vets:\n" \
               f"{vets_str}"
