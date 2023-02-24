# DECORATORS
from datetime import datetime

def timer(func):
  """ decorator function that times how long
  it takes the passed in function to execute"""
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
  return f"Hello {name}!"

@timer
def say_bye(name="buddy"):
  return f"Goodbye {name}!"

# timed_hi = timer(say_hi)
# print(timed_hi())

# timed_bye = timer(say_bye)
# print(timed_bye())
# print(say_bye("Brad"))
# print(say_hi())

@timer
def do_stuff(num):
  counter = 1
  for val in range(num):
    counter += 1
  return counter

# print(do_stuff(10_000))
# print(do_stuff(10_000))
# print(do_stuff(10_000_000))
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


# print(num(5, 2))  #> 441  7 => 49 => 147  
#                        # 7 => 21 => 441
# print(num(8, 2))  #> 900
# print(num(4, 9))  #> 1521

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


# CLASSES

class Cat:
  breed = "American Short Hair"
  def __init__(self, color, age, name="Kitty"):
    self._color = color
    self._age = age
    self._name = name
    # self._hashed_password
    # print(f"You made a cat named {self._name}")

  def speak(self):
    return f'{self._name} says "Meow!"'


  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, new_name):
    bad_names = ["cat", "kitty", "kitty kitty"]

    if len(new_name) > 15:
      print("Thats to long of a name for a cat!")
    elif len(new_name) < 2:
      print("Cats need a longer name than that!")
    elif new_name in bad_names:
      print("Pick a better name for your cat!")
    else:
      self._name = new_name


  @property  
  def age(self):
    return self._age

  @age.setter
  def age(self, new_age):
    if new_age > 25:
      print("Thats too old for a cat's age")
    elif new_age < 0:
      print("Cat's cant have negative ages")
    else:
      self._age = new_age


  @classmethod
  def cat_factory(cls, cats):
    new_cats = [cls(color, age, name) for color, age, name in cats]
    # print([cat.speak() for cat in new_cats])
    return new_cats


  @staticmethod
  def feed_me():
    hunger_level = int(input("From 1 to 9, how hungry is the kitty?: "))
    for i in range(hunger_level):
      print("Meeeooowwww?!?!")


  def __repr__(self):
    return f'<{self.name} is a {self._color} Cat!>'

  def __str__(self):
    return f'<{self.name} is a {self._color} Cat!>'


make_cats = Cat.cat_factory([("black", 6, "Blue"), ("tuxedo", 6, "Patch"), ("grey", 13, "Mimi")])
blue, patch, mimi = make_cats

# blue = {
#   "age": 6,
#   "name": "Blue",
#   "color": "black"
# }
# blue = Cat(**blue)
# blue = Cat(age=6, color="black", name='Blue')
# patch = Cat(age=6, color="tuxedo", name='Patch')
# print(blue)
# print(blue._age)
# print(blue.speak())
# print(blue.breed)
# blue.breed = "Long Hair"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# Cat.breed = 'Long Hair'
# print(blue.breed)
# print(patch.breed)
# # print(Cat.breed)
# print(mimi._color)
# patch.feed_me()
# print(blue.name)
# blue.name = 'Mr Fancy Pants Kittenpuss'
# print(blue.name)
# print(blue)