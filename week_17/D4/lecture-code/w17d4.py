import random 
from random import choice as picker, randint
from helpers import add2, add4, add6, add8, add10

# random.choice()
# random.randint()
# picker()
# randint()

# def choice(num):
#     pass

# print(add2(4))
# print(add4(4))
# print(add6(4))
# print(add8(4))


# DECORATORS
from datetime import datetime

def timer(func):
    """ decorator for a function that times how long it takes for 
    the decorated function to execute"""

    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        val = func(*args, **kwargs)
        print(val)
        end_time = datetime.now()
        time_elapsed = end_time - start_time
        return time_elapsed
    
    return wrapper


@timer
def say_hi(name="you"):
    return f"Hello {name} !"

@timer
def say_bye():
    return "Goodbye!"


# timed_hi = timer(say_hi)
# print(timed_hi())
# print(say_bye())
# print(say_hi("Brad"))
# print(say_bye())


# fun do stuff timer
@timer
def do_stuff(num):
  counter = 1
  for val in range(num):
    counter += 1
  return counter

# print(do_stuff(10_000))
# print(do_stuff(100_000_000))
# print(do_stuff(1_000_000_000)) # 1.32 minutes to run



# CHAIN DECORATOR
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


@multiply_by_three
@power_of_two
def num(a, b):
    return a + b


print(num(5, 2))  #> 441  7 => 49 => 147  
                       # 7 => 21 => 441
print(num(8, 2))  #> 900
print(num(4, 9))  #> 1521



def chain_decorator(func):
    @power_of_two
    @multiply_by_three
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return x
    return inner


@chain_decorator
def num(a, b):
    return a + b


# ORDER DECORATOR
# Write your function here.
def order_decorator(func):
    def wrapper(*args, **kwargs):
        print(1)
        x = func(*args, **kwargs)
        print(3)
        return x
    
    return wrapper


@order_decorator
def middle(num):
      print(num)
      return num * num

print(middle(2)) #> 1 2 3 4









lunch = ["pizza", "burger", "sandwick"]

def is_even(num):
    return num % 2 == 0

class Thing:
    pass