# IMPORTING
# import random 
# random.randint()
# random.choices()

# import random as randy
# randy.randint(a, b)
# randy.choices()

# from random import choice, randint, shuffle
# randint()
# choice()

# from helpers.helper1 import add2, add4
# from helpers.helper2 import add6, nums

from helpers import add2, add4, add6, nums

# print(add2(2))
# print(add4(2))
# print(add6(2))

# print(nums)
# nums.append(7)
# print(nums)


# DECORATORS
from datetime import datetime

def timer(func):
    """ decorator definition for a function that times how long
    it takes for the function it is decorating to run """
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        val = func(*args, **kwargs)
        print(val)
        end_time = datetime.now()
        time_elapsed = end_time - start_time
        return time_elapsed
    return wrapper


@timer
def say_hi(age, color, name="you"):
    """ function that takes in an age & color for no appearant reason
    and also a name, which it will use to say hi to a person"""
    return f"Hello {name}!"


@timer
def say_bye():
    return "See ya later!"


@timer
def say_good_afternoon():
    return "Good afternoon!"


# print(say_bye())
# print(say_hi("Brad"))
# timed_hi = timer(say_hi)
# print(timed_hi())
# print(dir(say_hi))
# print(say_hi.__closure__)
# print(timed_hi.__closure__)
# print(say_bye.__closure__)
# print(say_good_afternoon())

# def square_decorator(func):
#     def inner(*args, **kwargs):
#         x = func(*args, **kwargs)
#         return x * x
#     return inner

# def multiply_decorator(func):
#     def inner(*args, **kwargs):
#         x = func(*args, **kwargs)
#         return 3 * x
#     return inner
  
# def chain_decorator(func):
#   @square_decorator
#   @multiply_decorator
#   def inner(*args, **kwargs):
#     return func(*args, **kwargs)
#   return inner

# @chain_decorator
# def num(a, b):
#     return a + b

# print(num(5, 2))  #> 441
# print(num(8, 2))  #> 900
# print(num(4, 9))  #> 1521

# CLASSES

class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        # print(f"You created a intance of Cat named {self._name}")

    
    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 15:
            print("Thats too long a name for a cat")
        elif len(new_name) < 3:
            print('Thats too short of a name for a cat')
        else:
            self._name = new_name


    @property
    def age(self):
        return self._age

    
    @age.setter
    def age(self, new_age):
        if new_age > 25:
            print("Thats too old for a cat!")
        elif new_age < 0:
            print("Cats can't have negative ages")
        else:
            self._age = new_age


    def speak(self):
        return f'{self._name} says "Meow!"'


    @classmethod
    def cat_factory(cls, cats):
        new_cats = [ cls(color, age, name) for color, age, name in cats]
        print([cat.speak() for cat in new_cats])
        return new_cats

    
    @staticmethod
    def feed_me():
        for i in range(5):
            print("Meowwwwww?!?!")


    @classmethod
    def oldest_cat(cls, cats):
        oldest = cats[0].age
        oldest_cat = cats[0].name
        for cat in cats:
            print(cat.name, cat.age)
            if oldest < cat.age:
                oldest = cat.age
                oldest_cat = cat.name
        return oldest_cat



# blue = Cat("black", 5, "Blue")
# patch = Cat('tuxedo', 5, "Patch")
cats = [("black", 5, "Blue"), ("tuxedo", 5, "Patch"), ("gray", 10, "Mimi")]
blue, patch, mimi = Cat.cat_factory(cats)
oldest_cat = Cat.oldest_cat([blue, patch, mimi])
print("oldest cat", oldest_cat)
# print(blue._age)
# print(blue.speak())
# blue.breed = "Long Hair"
# print(blue.name)
# blue.name = "Mr FancyPants Better Blue"
# print(blue.name)
# print(patch._color)
# patch.feed_me()
# print(blue.age)
# blue.age = 10
# print(blue.age)

# raise Exception("Text for the exception")

# INHERITANCE & POLYMORPHISM
class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        print(self.speak())

    
    def speak(self):
        if self._name == "Tony":
            return f"{self._name} says'They're GREAT!!!'"
        else:
            return f"{self._name} says 'RAWRRRRRWRRR!'"


    def __repr__(self):
        return f'< {self._name} is a {self._age} yr old {self._color} Tiger >'

    
    def __str__(self):
        return f'< {self._name} is a {self._age} yr old {self._color} Tiger >'


    def __len__(self):
        return self._age
        


# tony = Tiger("orange", 20, "Tony", 24)
# tigger = Tiger("orange", 30, "Tigger", 4)
# print(tony.name)
# print(tony)
# print(len(tony))
# print(tony.__str__())
