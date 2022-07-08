# import random as banana
# from random import choice, randint
# import random
# from random import choice
# from helpers.helpers import add2
# from helpers import add4, add2, add6

# choice()
# randint()

# 


# DECORATORS
from datetime import datetime

def timer(func):

    def wrapper(*args, **kwargs):
        start_time = datetime.now()

        val = func(*args, **kwargs)
        print(val)

        end_time = datetime.now()
        time_elapsed = end_time - start_time
        return time_elapsed

    return wrapper


# @timer
def say_hi(name="you"):
    return f'Hello {name}!'


# print(say_hi())

# @timer
def say_bye():
    return "See ya later!"

# print(say_bye())

timed_hi = timer(say_hi)
# print(timed_hi.__closure__)
# print(say_hi.__closure__)


# timed_bye = timer(say_bye)
# print(timed_bye())

#CLASSES
class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        print(f"You sucessfully made a cat named {self._name}")


    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self, new_name):
        self._name = new_name


    @property
    def age(self):
        return self._age


    @age.setter
    def age(self, new_age):
        if new_age > 25:
            print("Thats too old for a cat")
        elif new_age < 0:
            print("Can't have a negative age!")
        else:
            self._age = new_age

    
    def speak(self):
        return f"{self._name} says 'Meow!'"


    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(color, age, name) for color, age, name in cats]
        print([cat.speak() for cat in new_cats])
        return new_cats


    @staticmethod
    def feed_me():
        for i in range(5):
            print('Meowwwww!?!?')



blue = Cat(
    age=5,
    name="Blue",
    color="black"
)

# patch = Cat("tuxedo", 5, "Patch")
# make_cats = Cat.cat_factory([("tuxedo", 5, "Patch"), ("gray", 12, "Mimi")])
# patch, mimi = make_cats
# print(patch.speak())

# print(blue._color)
# print(patch)
# print(blue.speak())
# print(blue.breed)
# blue.breed = "Long Haired Cat"
# print(blue.breed)
# print(Cat.breed)
# blue.feed_me()
# print(blue.name)
# blue.name = "Maverick"
# print(blue.name)
# blue.age = 6
# print(blue.age)


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth

    def speak(self):
        return f"{self.name} says RAWRRRWRR!!!"


    def __repr__(self):
        return f"< {self.name} is a {self._color} Tiger!>"


    def __str__(self):
        return f"< {self.name} is a {self._color} Tiger!>"
    

    def __len__(self):
        return self.age


tony = Tiger("orange", 35, "Tony", 16)
print(tony.name)
print(tony.speak())
print(tony)
print(len(tony))