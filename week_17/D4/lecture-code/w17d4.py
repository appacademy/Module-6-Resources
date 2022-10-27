from random import choice as picky, shuffle, randint
from helpers import add_2, add_4, add_10, evens, Pizza


# nums = [1, 2, 3, 4, 5]
# print(picky(nums))

# print(add_2(2))
# print(add_4(2))
# print(evens)

# DECORATIONS
from datetime import datetime


def timer(func):
    """ decorator that will time the execution 
    of any function it decorates"""
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        val = func(*args, **kwargs)
        print(val)
        end_time = datetime.now()
        time_elapsed = end_time - start_time
        return time_elapsed
    return wrapper


@timer
def say_hi(name='you'):
    return f"Hello {name}!"


@timer
def say_bye():
    return "See ya later!"

@timer
def say_good_afternoon(name='buddy'):
    return f'Good afternoon {name}!'


# print(say_good_afternoon())
# print(say_bye())
# print(say_hi())

# timed_hi = timer(say_hi)
# print(timed_hi())
# timed_bye = timer(say_bye)
# print(timed_bye())


# Problem 4 - Chain Decorator
# Write your function here.

# def power_of_two(func):
#     def inner(*args, **kwargs):
#         x = func(*args, **kwargs)
#         return x * x
#     return inner


# def multiply_by_three(func):
#     def inner(*args, **kwargs):
#         x = func(*args, **kwargs)
#         return x * 3
#     return inner


# @power_of_two
# @multiply_by_three
# def num(a, b):
#     return a + b

# print(num(5, 2))  #> 441  7 => 49 => 147  
#                        # 7 => 21 => 441
# print(num(8, 2))  #> 900
# print(num(4, 9))  #> 1521

# John Lee's Chain Decorator solution

# def chain_decorator(func):
#     @multiply_decorator
#     @square_decorator
#     def inner(*args, **kwargs):
#         x = func(*args, **kwargs)
#         return x
#     return inner


# @chain_decorator
# def num(a, b):
#     return a + b



# CLASSES
class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        # print(f"You made a cat named {self._name}")
        # print(self.speak())


    @property
    def age(self):
        return self._age

    
    @age.setter
    def age(self, new_age):
        if new_age > 25:
            print("That's too old for a cat")
        elif new_age < 0:
            print("Cats can't have a negative age!")
        else:
            self._age = new_age


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_name):
        if len(new_name) > 15:
            print("Thats too long of a name for a cat!")
        elif len(new_name) < 2:
            print("Cats should have more than 1 letter names")
        else:
            print(f"{self._name}'s name was changed to '{new_name}'")
            self._name = new_name


    def speak(self):
        return f'{self._name} says MEOW!'


    def __repr__(self):
        return f"< {self._name} is a {self._color} Cat >"
  

    def __str__(self):
        return f"< {self._name} is a {self._color} Cat >"


    def __len__(self):
        return self._age


    @staticmethod
    def feed_me():
        for i in range(5):
            print("Meeeooowwww?!?!!")

    
    @classmethod
    def cat_factory(cls, cats):
        new_cats = [ cls(color, age, name) for color, age, name in cats ]
        # print([cat.speak() for cat in new_cats])
        return new_cats


blue, patch, mimi = Cat.cat_factory([("black", 6, 'Blue'),
    ("tuxedo", 6, "Patch"), ('grey', 12, "Mimi")])
# blue = Cat("black", 6, "Blue")
# patch = Cat('tuxedo', 6, "Patch")
# print(blue._color)
# blue.feed_me()
# Cat.feed_me()
# print(blue.speak())
# print(blue.breed)
# print(patch.breed)
# Cat.breed = "American Long Hair"
# print(blue.breed)
# print(patch.breed)
# print(blue.age)
# blue.age = 2
# print(blue.age)
# print(blue.name)
# blue.name = 'Quark'
# print(blue, patch)
# # print(dir(blue))
# print(len(blue))

# cats = ["Blue", "Patch", "Mimi"]
# print(cats)
# print(len(cats))

# def __repr__(self):
#     return f'[{[item.name for item in self._items]}]'


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        print(self.speak())


    def speak(self):
        if self._name == 'Tony':
            return f"{self._name} says 'They're GREAT!!!!'"
        else:
            return f"{self._name} says 'RRAAAWWWRRR!!!!'"


    def __repr__(self):
        return f'< {self.name} is a {self._color} Tiger >'

    
    def __str__(self):
        return f'< {self.name} is a {self._color} Tiger >'



tony = Tiger('orange', 20, "Tony", 30)
hobbes = Tiger('orange', 8, "Hobbes", 20)
tigger = Tiger("orange", 50, "Tigger", 4)
print(tony.name)
print(tony._name)
print(tony)