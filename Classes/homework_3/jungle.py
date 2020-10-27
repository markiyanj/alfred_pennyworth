from __future__ import annotations

from abc import abstractmethod, ABC
from uuid import uuid4
import random


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = uuid4()
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, jungle: Jungle):
        raise NotImplementedError


class Predator(Animal):

    def eat(self, jungle: Jungle):
        random_animal = random.choice([a for a in jungle.animals.values()])
        if self.current_power <= 0:
            jungle.remove_animal(self)
        elif self.id == random_animal.id:
            self.current_power -= 0.3 * self.max_power
        else:
            if self.speed > random_animal.speed and self.current_power > random_animal.current_power:
                self.current_power += 40
                if self.current_power > self.max_power:
                    self.current_power = self.max_power
            else:
                self.current_power -= 0.3 * self.max_power
                random_animal.current_power -= 0.3 * random_animal.max_power


class Herbivorous(Animal):

    def eat(self, jungle: Jungle):
        if self.current_power <= 0:
            jungle.remove_animal(self)
        else:
            self.current_power += 40
            if self.current_power > self.max_power:
                self.current_power = self.max_power


class Jungle:

    def __init__(self):
        self.animals = dict()

    number: int = -1

    def __getitem__(self, item):
        length = len(self.animals)
        if self.number >= length - 1:
            raise StopIteration
        self.number += 1
        return self.animals[str(self.number)]

    def add_animal(self, animal):
        animal_count = 0
        for i in self.animals.keys():
            animal_count += 1
        self.animals[str(animal_count)] = animal

    def remove_animal(self, animal):
        if animal in self.animals.values():
            for key, value in self.animals.items():
                if value == animal:
                    del self.animals[key]
                    break


def is_predator_in_jungle(jungle: Jungle):
    if any(isinstance(animal, Predator) for animal in jungle.animals.values()):
        return True
    else:
        return False


def animal_generator():
    animal_list = []
    for i in range(10):
        power = random.randint(20, 100)
        speed = random.randint(20, 100)
        if random.randint(0, 1) == 0:
            new_animal = Herbivorous(power, speed)
            animal_list.append(new_animal)
        else:
            new_animal = Predator(power, speed)
            animal_list.append(new_animal)
    for animal in animal_list:
        yield animal


if __name__ == "__main__":
    # Create jungle
    # Create few animals
    # Add animals to jungle
    # Iterate throw jungle and force animals to eat until no predators left
    # animal_generator to create a random animal
    gen_animal = animal_generator()

    jungle = Jungle()

    while True:
        try:
            animal = next(gen_animal)
            jungle.add_animal(animal)
        except StopIteration:
            break

    while True:
        if any(isinstance(animal, Predator) for animal in jungle.animals.values()):
            try:
                for animal in jungle.animals.values():
                    animal.eat(jungle=jungle)
            except RuntimeError:
                continue
        else:
            break
