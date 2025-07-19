# OOP - Object Oriented Programming

# Class construction

class Food:
    def __init__(self, name, is_healthy):
        self.name = name
        self.is_healthy = is_healthy

generic_food = Food("Random Food", False)
some_other_food = Food("Some Other Food", False)

print(generic_food, some_other_food)

# Encapsulation

# Data inside a class is protected from code outside the class
# getters ans setters = get_age and set_age

class Person:
    def __init__(self, age = 0):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, newAge):
        if (newAge > 0):
            self._age = newAge
        else:
            print ("New age is not valid!")

alex = Person(26)

print(alex.get_age())

alex.set_age(-1)

print(alex.get_age())

alex.set_age(27)

print(alex.get_age())

# Inheritance

# A class can inherit attributes and methods from another class making the former a child class and the later a parent class.
# super() = keyword refer to parent class

class Food:
    def __init__(self, name, is_healthy):
        self.name = name
        self.is_healthy = is_healthy

class Fruit(Food):
    def __init__(self, name, has_seeds, has_stone):
        super().__init__(name, True)
        self.has_seeds = has_seeds
        self.has_stone = has_stone

class Vegetable(Food):
    def __init__(self, name, has_roots, has_leaves):
        super().__init__(name, True)
        self.has_roots = has_roots
        self.has_leaves = has_leaves
        
# Abstraction

# hide the implementation of methods
# ABC = Abstract Base Class

from abc import ABC, abstractmethod

class Meal(ABC):
    
    @abstractmethod
    def required_cutlery(self):
        pass

class FingerFood(Meal):
    def required_cutlery(self):
        print("Your own hands!")

class PoshFood(Meal):
    def required_cutlery(self):
        print("Five different forks, ten different spoons, and four-and-a-half knives.")


# Polymorphism

# Note: __str__  is a special method which is called when we try to print out the class instance itself. In the above example, when print(food_item) is called, it will execute the __str__ method of the class.
# relies on inheritance
# because each of those classes inherit from a shared parent class, they can be treated as if they are that parent class
# function overriding
# method written in the child class overrides the method inherited from the parent class. It means that when the __str__ method of the child class is executed, it runs the __str__ method defined in the child class rather than the one inherited from the parent class.

class Food:
    def __init__(self, name, is_healthy):
        self.name = name
        self.is_healthy = is_healthy

    def __str__(self):
        return "The {name} food {healthy_status} healthy.".format(name=self.name, healthy_status="is" if self.is_healthy == True else "is not")

class Fruit(Food):
    def __init__(self, name, has_seeds, has_stone):
        super().__init__(name, True)
        self.has_seeds = has_seeds
        self.has_stone = has_stone

    def __str__(self):
        return "The healthy {name} fruit {seeds_status} contain seeds and {stone_status} contain a stone.".format(name=self.name, seeds_status="does" if self.has_seeds == True else "does not", stone_status="does" if self.has_stone == True else "does not")

class Vegetable(Food):
    def __init__(self, name, has_roots, has_leaves):
        super().__init__(name, True)
        self.has_roots = has_roots
        self.has_leaves = has_leaves

    def __str__(self):
        return "The healthy {name} vegetable {roots_status} contain roots and {leaves_status} include any leaves.".format(name=self.name, roots_status="does" if self.has_roots == True else "does not", leaves_status="does" if self.has_leaves == True else "does not")

apple = Fruit("Apple", True, False)
potato = Vegetable("Potato", False, False)

for food_item in (apple, potato):
    print (f'Looks like we have at least one {food_item.name} available!')
    print(food_item)


# Ed excersize 1 - Class construction

class Pokemon():
    def __init__(self, name, pokedexNumber, type):
        self.name = name
        self.pokedexNumber = pokedexNumber
        self.type = type

pikachu = Pokemon("Pikachu", 25, "Electric")
print(pikachu.name)
print(pikachu.pokedexNumber)
print(pikachu.type)

