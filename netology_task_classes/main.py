from netology_tesk_classes.animals import Animal, Cow, Chicken, Goose, Goat, Sheep, Duck, breeds
import random


if __name__ == "__main__":
    # structure intention - breed: [name, weight]
    animals_accounting = {"goose":[["Серый",20], ["Белый",10]],
                  "cow":[["Манька",150]],
                  "sheep":[["Барашек",30],["Кудрявый",50]],
                  "chicken":[["Ко-Ко",5],["Кукареку",4]],
                  "goat":[["Рога",30], ["Копыта",34]],
                  "duck":[["Кряква",7]],
                  }

    my_animals = []
    # =================task2==============
    # create your farm
    for breed, names_weights in animals_accounting.items():
        for nw in names_weights:
            my_animals.append(breeds[breed](nw))

    # check all animals are alive
    for animal in my_animals:
        animal.makeSound()

    print()
    print("==Now I will feed you")
    food = ["grass", "corn", "bread"]

    for animal in my_animals:
        animal.toFeed(kind_of_food=random.choice(food))

    print()
    print("==Now I will get something from you")

    resources_from_animals= {"toGetEggs": "eggs",
                            "toGetMilk": "litres of milk",
                            "toGetFur": "kg of fur"}
    for animal in my_animals:
        operations = set(resources_from_animals.keys()) & set(dir(animal))
        for op in operations:
            print(f"{animal.name} gave you {getattr(animal,op)()} {resources_from_animals[op]}")

    # ===============task3======================
    print()
    print (f'Total weight of my animals is: {Animal.getTotalWeight(*my_animals)} kg')
    heaviest = Animal.getHeaviest(*my_animals)
    print(f'The heaviest animal is: {heaviest.name} {heaviest.weight} kg')
