from __future__ import annotations

from abc import abstractmethod, ABC
from uuid import uuid4
import random
import csv
import time


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
                self.current_power += 0.4 * self.current_power
                jungle.remove_animal(random_animal)
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
            self.current_power += self.current_power * 0.4
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


def animal_generator():
    animal_list = []
    for i in range(int(input('With how many animals you want to play?: '))):
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


def csv_upload(path):
    with open(path, 'w') as csv_file:
        field_name = ['Class', 'max_power', 'speed']
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_name, delimiter=',')
        csv_writer.writeheader()
        list_of_animals = animal_generator()
        while True:
            try:
                animal = next(list_of_animals)
                csv_writer.writerow({'Class': animal.__class__.__name__,
                                     'max_power': animal.max_power,
                                     'speed': animal.speed})
            except StopIteration:
                break


def csv_load(path):
    count = 0
    with open(path, 'r') as read_csv:
        csv_reader = csv.reader(read_csv)
        for row in csv_reader:
            if count == 0:
                count += 1
                continue
            class_of_animal = row[0]
            max_power = int(row[1])
            speed = int(row[2])
            if class_of_animal == "Predator":
                animal = Predator(max_power, speed)
                jungle.add_animal(animal)
            else:
                animal = Herbivorous(max_power, speed)
                jungle.add_animal(animal)


if __name__ == "__main__":
    # Create jungle
    # Create few animals
    # Add animals to jungle
    # Iterate throw jungle and force animals to eat until no predators left
    # animal_generator to create a random animal

    # gen_animal = animal_generator()

    csv_upload('animal_configuration.csv')

    jungle = Jungle()

    csv_load('animal_configuration.csv')

    # while True:
    #     try:
    #         animal = next(gen_animal)
    #         jungle.add_animal(animal)
    #     except StopIteration:
    #         break

    print('Let`s look at the animals in the jungle ', '\n')
    time.sleep(1)
    for animal in jungle:
        print(f'Class:{animal.__class__.__name__}, max_power:{animal.max_power}, speed:{animal.speed}')

    time.sleep(1)
    print('The HUNT began', '\n')
    while True:
        if any(isinstance(animal, Predator) for animal in jungle.animals.values()):
            try:
                for animal in jungle.animals.values():
                    animal.eat(jungle=jungle)
            except RuntimeError:
                continue
        else:
            break
    time.sleep(0.5)
    print('jungle after hunting', '\n')
    time.sleep(0.5)
    if jungle.animals == {}:
        print('No animals in jungle')
    else:
        for an in jungle.animals.values():
            print(f'Class:{an.__class__.__name__}, current_power:{an.current_power}, speed:{an.speed}')
