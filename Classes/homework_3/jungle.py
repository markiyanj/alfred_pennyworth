from __future__ import annotations

from typing import Dict, Any
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
        print('eat')


class Predator(Animal):

    def eat(self, jungle: Jungle):
        random_animal = random.choice([a for a in jungle.animals.values()])
        if self.current_power <= 0:
            jungle.remove_animal()
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


# AnyAnimal = Any[Herbivorous, Predator]


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
        animal_list_values = [a for a in self.animals.values()]
        animal_list_keys = [k for k in self.animals.keys()]
        index_of_animal = animal_list_values.index(animal)
        key = animal_list_keys[index_of_animal]
        del self.animals[key]


def is_predator_in_jungle(jungle: Jungle):
    count = 0
    for i in jungle:
        if isinstance(i, Predator):
            count += 1
    if count == 0:
        return False
    else:
        return True


def animal_generator():
    animal_list = []
    for i in range(5):
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
        if is_predator_in_jungle(jungle):
            for animal in jungle:
                animal.eat(jungle=jungle)
