# from random import choice as pick
# import random as rand
# from random import choice, shuffle 

# nums = [1, 2, 3, 43, 5]
# print(rand.choice(nums))

# from helpers1 import add2
# from helpers.helpers2 import add4
# from helpers import add2, add4, add6
# import helpers 

# helpers.add2()

# print(add2(4))
# print(add4(4))
# print(add6(4))

# import random
# from random import shuffle, choice


# DECORATORS
from datetime import datetime

def timer(func):
    """
    decorator function that will time how long 
    the wrapped fucntion takes to execute
    """
    def wrapper(*args, **kwargs):
        # say_hello("Brad", "Alex")
        # print(args) -> ("Brad", "Alex")
        start_time = datetime.now()
        val = func(*args, **kwargs) # -> args will be spread to "Brad", "Alex"
        print(val)
        end_time = datetime.now()
        time_elapsed = end_time - start_time
        return time_elapsed
    return wrapper


@timer
def say_hi(name='you'):
    return f"Hello {name}!"

@timer
def say_bye(time="later"):
    return f"See ya {time}!"

@timer
def say_good_afternoon():
    return 'Have a great afternoon'

# timed_hi = timer(say_hi)
# print(timed_hi())

# timed_bye = timer(say_bye)
# print(timed_bye())
# print(say_hi("Brad"))
# print(say_bye("next year!"))
# print(say_good_afternoon())

def function(func):
    return func


# def close_it():
#     multipler = 5
#     def times_by(arg):
#         print(arg * multipler)
#     return times_by

# closed_times = close_it()
# closed_times(4)

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

# @power_of_two
# @multiply_by_three
# def num(a, b):
#     return a + b


def chain_decorator(func):
    @multiply_by_three
    @power_of_two
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return x
    return inner


@chain_decorator
def num(a, b):
    return a + b


# print(num(5, 2))  #> 441  7 => 49 => 147  
#                        # 7 => 21 => 441
# print(num(8, 2))  #> 900
# print(num(4, 9))  #> 1521



# Hello world

def hello_world_decorator(func):
    def inner():
        print("Hello", end=' ')
        func()
        print("Goodnight")
    return inner

@hello_world_decorator
def world():
  print("World", end=' ')

# world() #> Hello World Goodnight


# CLASSES
class Cookie:
    calories = 90
    def __init__(self, color, quantity, name="cookie"):
        self._color = color
        self._quantity = quantity
        self._name = name + " cookie"
        self._baking_time = 60
        print(f'You made a {self._name}!')
        self.cookies_are_great()

    @property
    def name(self):
        return self._name

    @name.setter  
    def name(self, new_name):
        if len(new_name) <= 3:
            print("Thats too short of a name for a cookie")
        else:
            print(f"{self._name} cookie has been renamed to {new_name}")
            self._name = new_name


    @property 
    def quantity(self):
        return self._quantity

    @quantity.setter 
    def quantity(self, new_quantity):
        if new_quantity < 1:
            print("we need to have at least 1 cookie")
        else:
            output = "Yay we now have more cookies" if new_quantity >= self._quantity else "Awww we lost cookies"
            print(output)
            self._quantity = new_quantity


    def eat_cookie(self):
        print("Yum, that was a delicious cookie!")
        self._quantity -= 1


    def __repr__(self):
        return f"<{self._name} with {self._quantity} left>"
   

    def __str__(self):
        return f"<{self._name} with {self._quantity} left>"


    @classmethod
    def cookie_factory(cls, cookies):
        new_cookies = [cls(color, quantity, name) for color, quantity, name in cookies]
        return new_cookies


    @staticmethod
    def cookies_are_great():
        for i in range(3):
            print("I love cookies they are awesome and deliious!")



new_cookies = [
    ("tan", 24, "Oatmeal"),
    ('tan with brown chips', 12, "Chocolate chip"),
    ("tan", 36, "Sugar")
]
# oatmeal, choco_chip, sugar = Cookie.cookie_factory(new_cookies)
# print(oatmeal, choco_chip, sugar)
# oatmeal = Cookie("tan", 24, "Oatmeal")
# choco_chip = Cookie('tan with brown chips', 12, "Chocolate chip")
# print(oatmeal)
# print(oatmeal._quantity)
# oatmeal.eat_cookie()
# print(oatmeal._quantity)
# print(oatmeal.calories)
# print(choco_chip.calories)
# Cookie.calories = 120
# print(oatmeal.calories)
# print(choco_chip.calories)
# oatmeal.cookies_are_great()
# print(oatmeal.name)
# oatmeal.name = "PB"
# print(oatmeal.name)
# oatmeal.name = "Peanut butter"
# print(oatmeal.name)
# print(oatmeal.quantity)
# oatmeal.quantity = 30
# print(oatmeal.quantity)
# oatmeal.quantity = 12
# print(oatmeal.quantity)

class HolidayCookie(Cookie):
    def __init__(self, color, quantity, name, shape):
        super().__init__(color, quantity, name)
        self._shape = shape

    def eat_cookie(self):
        if self.name == 'gingerbread cookie':
            print("Not my gumdrop buttons!")
        else:
            print("Yum, that was a delicious holiday cookie!")
        self._quantity -= 1


    def __len__(self):
        return self._quantity

    def __repr__(self):
        return f"< 🎄 Holiday {self._name} with {self._quantity} left 🎄 >"

    def __str__(self):
        return f"< 🎄 Holiday {self._name} with {self._quantity} left 🎄 >"

gingerbread = HolidayCookie("brown", 12, "gingerbread", "small humanoid")
print(gingerbread)
# print(gingerbread.name)
gingerbread.eat_cookie()
print(len(gingerbread))
gingerbread._quantity = 0










def identify_polygon(self):
    # num sides 3 or greater

    identifier_dict = {
                3: "Triangle",
                4: "Quadrilateral",
                5: "Pentagon",
                6: "Hexagon",
                7: "Heptagon",
                8: "Octagon",
                9: "Nonagon",
                10: "Decagon"
            }
    try:
        self.type = identifier_dict[self.num_sides]
    except KeyError:
        self.type = f"Polygon with {self.num_sides} sides"


    self.type = identifier_dict.get(self.num_sides, f"Polygon with {self.num_sides} sides")

    