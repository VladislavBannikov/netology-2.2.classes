'''
Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:

гусей "Серый" и "Белый"
корову "Маньку"
овец "Барашек" и "Кудрявый"
кур "Ко-Ко" и "Кукареку"
коз "Рога" и "Копыта"
и утку "Кряква"
Со всеми животными вам необходимо как-то взаимодействовать:

кормить
корову и коз доить
овец стричь
собирать яйца у кур, утки и гусей
различать по голосам(коровы мычат, утки крякают и т.д.)
'''

from random import random


class Animal():
    breed = "generic animal"
    voice = "generic voice"
    name = ''
    weight = 0

    def toFeed(self, kind_of_food="grass"):
        print(f"{self.name} likes {kind_of_food}")

    def makeSound(self):
        print(f"{self.breed} {self.name} said {self.voice}!!!")

    def __init__(self,name_weight):
        self.name = name_weight[0]
        self.weight = name_weight[1]

    @staticmethod
    def getTotalWeight(self, *animals):
        total = 0
        for animal in animals:
            if isinstance(animal,Animal):
                total += animal.weight
        return total

    def __gt__(self, other):
        if self.weight > other.weight:
            return True
        else:
            return False

    @staticmethod
    def getHeaviest(self, *animals):
        animals_local = list(animals)
        max_animal = animals_local.pop()
        for animal in animals_local:
            if animal > max_animal:
                max_animal = animal
        return max_animal


class MilkAnimal(Animal):
    breed = "dairy animal"

    def toGetMilk(self):
        return round(random()*10)


class FurAnimal(Animal):
    breed = "pack animal"


class EggAnimal(Animal):
    breed = "oviparous animal"

    def toGetEggs(self):
        return round(random()*10)


class Goose(EggAnimal):
    breed = "Goose"
    voice = "Quack"


class Cow(MilkAnimal):
    breed = "Cow"
    voice = "Moo"


class Sheep(FurAnimal):
    breed = "Sheep"
    voice = "Baa"

    def toGetFur(self):
        return round(random()*10)


class Chicken(EggAnimal):
    breed = "Chicken"
    voice = "cluck"


class Goat(FurAnimal):
    breed = "Goat"
    voice = "baa"


class Duck(EggAnimal):
    breed = "Duck"
    voice = "Quack"


breeds = {"cow": Cow, "chicken": Chicken, "goose":Goose, "goat":Goat, "sheep": Sheep, "duck": Duck}

