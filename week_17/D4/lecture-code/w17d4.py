# # IMPORTING MODULES

# # import random

# import random as randy

# # import superlongnamedmodulecomeonthisisridiculous as thing

# from random import choice, shuffle

# # list1 = [1, 2, 3, 4 ]

# # rand_int = randy.choice(list1)
# # print(rand_int)
# # randy.shuffle(list1)
# # print(list1)

# # IMPORTING FROM OTHER FILES

# # from helpers.helper1 import add2, nums
# # from helpers.helper2 import add6, add4


# from helpers import add2, names, add4, add6


# print(add2(4))
# print(add4(2))
# print(add6(6))
# print(names)

# from random import choice

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


@timer
def say_hi(name='you'):
    return f'Hello {name}!'

@timer
def say_bye():
    return "See you later!"


# timed_hi = timer(say_hi)
# print(timed_hi())
# print(dir(timed_hi))
# print(timed_hi.__closure__)
# print(say_hi.__closure__)
# timed_bye = timer(say_bye)
# print(timed_bye())
# print(say_hi("Brad"))

# CHAINED DECORATOR
# Problem 4 - Chain Decorator
# Write your function here.

def power_of_two(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return x * x
    return inner

def multiply_by_three(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return x * 3
    return inner


def chain_decorator(func):
    @power_of_two
    @multiply_by_three
    def inner(*args, **kwargs):
        val = func(*args, **kwargs)
        return val
    return inner


@chain_decorator
def num(a, b):
    return a + b


# print(num(5, 2))  #> 441  
# # 7 => 49 => 147  
# # 7 => 21 => 441
# print(num(8, 2))  #> 900
# print(num(4, 9))  #> 1521


# CLASSES

class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        # print(f"You made a cat named {self._name}")


    @property  # GETTER METHOD FOR NAME
    def name(self):
        return self._name

    
    @name.setter  #SETTER METHOD FOR NAME
    def name(self, new_name):
        if len(new_name) > 15:
            print("Thats too long of a name!")
        elif len(new_name) < 2:
            print("Please give your cat a real name!")
        else:
            print(f"{self._name} was renamed to {new_name}")
            self._name = new_name


    @property
    def age(self):
        return self._age

    
    @age.setter
    def age(self, new_age):
        if new_age > 25:
            print("That's too old for a cat's age!")
        elif new_age < 0:
            print("Cats can not have a negative age")
        else:
            print(f"{self._age} was updated to {new_age}")
            self._age = new_age

    
    def speak(self):
        return f'{self._name} says MEOW!!!'

    
    @classmethod
    def cat_factory(cls, cats):
        new_cats = [ cls(color, age, name) for color, age, name in cats]
        # print([cat.speak() for cat in new_cats])
        return new_cats


    @staticmethod
    def feed_me():
        for i in range(5):
            print("Meowwwww!?!?!")


blue, patch, mimi = Cat.cat_factory([('black', 6, 'Blue'), ('tuxedo', 6, 'Patch'), ('gray', 10, "Mimi")])


# print(blue.name)
# blue.name = "Tommy the totally tubular kitten"
# print(blue.name)


# print(blue.age)
# blue.age += 1
# print(blue.age)



# print(blue.speak())
# print(patch._color)
# blue = Cat('black', 6, 'Blue')
# patch = Cat('tuxedo', 6, 'Patch')
# print(blue)
# print(blue._name)
# print(blue.speak())
# print(blue.breed)
# print(patch.breed)
# Cat.breed = "American Long Hair"
# blue.breed = "Silly little ninja"
# print(blue.breed)
# print(patch.breed)
# patch.feed_me()


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        # print(self.speak())


    def speak(self):
        if self._name == "Tony":
            return f"{self._name} says 'They're GREAT!!!!!'"
        else:
            return f"{self._name} says 'RAWRRWWWRRR!!!'" 


    def __repr__(self):
        return f'< {self._name} is a {self._color} Tiger >'

    
    def __str__(self):
        return f'< {self._name} is a {self._color} Tiger >'


    def __len__(self):
        return self._age
    


tony = Tiger('orange', 20, "Tony", 30)
tigger = Tiger('orange', 12, "Tigger", 4)

print(tony)
print(tigger)

print(len(tony))
print(dir(Tiger))