# import random
# from random import choice as pick, shuffle, randint

# from helpers.helpers import add2, add4
# from helpers.helpers2 import add6, add8

# from helpers import add2, add4, add6, add8, add10
# from random import choice, choices, randint, randfloat


# nums = [1, 2, 3, 4, 5, 6]

# def choice(num):
#     pass

# print(pick(nums))

# print(add2(4))

# print(add8(4))

# print(add10(10))

# DECORATORS
from datetime import datetime

def timer(func):
    """ decorator fefinition for a function 
    that times how long the function it wraps 
    takes to execute"""
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
def say_goodafternoon():
    return "What a lovely afternoon!"


# timed_bye = timer(say_bye)
# print(timed_bye())
# timed_hi = timer(say_hi)
# print(timed_hi())

# print(say_hi())
# print(say_bye())
# print(say_goodafternoon())



# CHAIN DECORATOR
def square_decorator(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return x * x
    return inner


def multiply_decorator(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return 3 * x
    return inner


@multiply_decorator
@square_decorator
def num(a, b):
    return a + b

print(num(5, 2))  # > 441 -> 7 -> 49 -> 147
                  # -> 7 -> 21 -> 441  
print(num(8, 2))  # > 900
print(num(4, 9))  # > 1521





def chain_decorator(func):
    @square_decorator
    @multiply_decorator
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return x
    return inner


@chain_decorator
def num(a, b):
    return a + b


# CLASSES


class Human:
  price = 500
  def __init__(self, name, age):
    self.name = name
    self._age = age
  
  def do_something_human(self):
    return f"{self.name} does something a normal human would do."
  
  @classmethod
  def human_facts(cls):
    return f"The average human is worth ${cls.price}"
  
  @staticmethod
  def more_human_facts():
    return "Technically, humans are edible."
  
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, val):
    if 0 < val < 125:
      self._age = val
    else:
      print("No one is that age.")
  
    
  
david = Human("David", 30)

# print(david.name)

# print(david.do_something_human())

# print(Human.price)
# print(david.price)
david.price = 1000000
# print(david.price)
# print(Human.price)

# Human.price = 1

# print(Human.price)

brad = Human("Brad", 30)

# print(brad.price)
# print(david.price)

# print(Human.human_facts())
# print(david.human_facts())
# print(brad.human_facts())

brad.price = 1000000000

# print(brad.price)

# print(Human.more_human_facts())
# print(david.more_human_facts())

# print(david.age)
# david.age = 126
# print(david.age)
# david._age = 5
# print(david._age)

class AppAcademyStudent(Human):
  price = 30000
  def __init__(self, name, age, level_of_sleep):
    super().__init__(name, age)
    self.level_of_sleep = level_of_sleep
  
  def do_something_human(self):
    return f"{self.name} does something a human might do. Everyone is very impressed."
  
  @classmethod
  def human_facts(cls):
    return f"App academy students are worth {cls.price}"
  
  def __repr__(self):
    return f"<{self.name} is an app Academy student who is worth ${self.price}>"
    
# chris = AppAcademyStudent("Christopher", 25, "Not enough")

# print(chris.level_of_sleep)
# print(chris.age)
# print(chris.name)

student = AppAcademyStudent("Student", 20, "way too much")

# print(student.price)

# print(student.do_something_human())
# print(student.human_facts())
print(student)

# class MyInt(int):
#   def __init__(self, num):
#     super().__init__()
    
#   def __add__(val1, val2):
#     return 10



# num1 = MyInt(1)
# num2 = MyInt(2)

# print(num1)
# print(num2)