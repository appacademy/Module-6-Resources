# IMPORTS

# IMPORTING FROM MODULES
# import random
# import os 
# from random import choice as pick, shuffle

# nums = [1, 2, 3, 4, 5]
# print(pick(nums))

# IMPORTING FROM FILES
from helpers import add2, add4, names
# from all_helpers.helpers2 import add6
# from all_helpers.helpers3 import add8
from all_helpers import add10, add6, add8

# print(add2(2))
# print(add4(2))
# print(add6(2))
# print(add8(2))


from datetime import datetime

def timer(func):
  def wrapper(*args, **kwargs):
    start_time = datetime.now()
    val = func(*args, **kwargs)
    end_time = datetime.now()
    print(val)
    elapsed_time = end_time - start_time
    return elapsed_time
  return wrapper

@timer
def say_hello(name="David"):
  return f"Hello {name}!"

@timer
def say_bye(name):
  return f"Goodbye {name}!"

@timer
def say_hello_many_times(name1, name2):
  return f"Hello {name1} and {name2}!"

print(say_hello_many_times("Andrew", "Keegan"))

# timed_hello = timer(say_hello)

# print(timed_hello("Brad"))

print(say_hello(name="Brad"))
print(say_bye("Brad"))

@timer
def do_stuff(num):
  count = 0
  for val in range(num):
    count += 1
  return count

# print(do_stuff(1))
# print(do_stuff(100))
# print(do_stuff(1000))
# print(do_stuff(100000000))


# # Problem 4 - Chain Decorator
# # Write your function here.

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


# @multiply_by_three
# @power_of_two
# def num(a, b):
#     return a + b



# def chain_decorator(func):
#     @square_decorator
#     @multiply_decorator
#     def inner(*args, **kwargs):
#         x = func(*args, **kwargs)
#         return x
#     return inner


# @chain_decorator
# def num(a, b):
#     return a + b


# print(num(5, 2))  #> 441  7 => 49 => 147  
#                        # 7 => 21 => 441
# print(num(8, 2))  #> 900
# print(num(4, 9))  #> 1521

# def timer(func):
#     """ decorator definition for a function that times how long
#     it takes for the function it is decorating to run """
#     def wrapper(*args, **kwargs):
#         start_time = datetime.now()
#         val = func(*args, **kwargs)
#         print(val)
#         end_time = datetime.now()
#         time_elapsed = end_time - start_time
#         return time_elapsed    
#     return wrapper


# CLASSES
class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        print(self.speak())


    @property  
    def name(self):
        return self._name

    @name.setter 
    def name(self, new_name):
        if len(new_name) < 2:
            print("That's too short a name for a cat!")
        else:
            self._name = new_name


    @property
    def age(self):
        return self._age

    @age.setter 
    def age(self, new_age):
        if new_age > 25:
            print("thats too old for a cat!")
        elif new_age < 0:
            print("Cats can't have a negative age!")
        else:
            self._age = new_age

    
    def speak(self):
        return f"{self._name} says 'Meow!'"


    def __repr__(self):
        return f"< {self.name} is a {self._color} cat >"

    
    def __str__(self):
        return f"< {self.name} is a {self._color} cat >"


    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(color, age, name) for color, age, name in cats]
        # print([cat.speak() for cat in new_cats])
        return new_cats


    @staticmethod
    def feed_me():
        for i in range(5):
            print('Meowwwww?!?!')



make_cats = Cat.cat_factory([("Black", 6, "Blue"),
        ("Tuxedo", 6, "Patch"),("Gray", 14, "Mimi")])
blue, patch, mimi = make_cats
# blue = Cat("Black", 6, "Blue")
# patch = Cat("Tuxedo", 6, "Patch")
# print(blue._name)
# print(blue.speak())
# print(blue.breed)
# # blue.breed = "Long Hair Kitty"
# Cat.breed = "Good Kitty"
# print(blue.breed)
# print(patch.breed)
# patch.feed_me()
# print(blue._age)
# print(blue.age)
# blue.age = 7
# print(blue.age)
# print(blue._name)
# print(blue.name)
# blue.name = "Mr. Fancypants McGoo"
# print(blue.name)
# print(blue)

# GETTERS & SETTERS
# Implement a class called Game with the
# following:
# A constructor that takes no arguments and sets an
# instance variable called score to an initial value of 0.
# A getter
# method named score that returns the value of a private instance property
# called _score.
# A setter method named score that sets the value of
# the private property _score. This method should take a single argument for the
# value and set _score to this value * 10.

class Game:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter 
    def score(self, new_score):
        self._score = new_score * 10


my_game = Game()
print(my_game.score) # 0

my_game.score
my_game.score(5)
my_game.score = 5
print(my_game.score) # 50