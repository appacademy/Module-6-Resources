# IMPORTING

from random import choice as pick, shuffle, randint

nums = [1, 2, 3, 4, 5]

# print(pick(nums))

from helpers import add2, add4, add6

# print(add2(2))
# print(add4(2))
# print(add2(add6(2)))


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
    return f"Hello {name}!"

@timer
def say_bye():
    return "Goodbye!"

@timer
def say_good_afternoon():
    return "Have a great afternoon!"

# print(say_hi("Brad"))   
# print(say_bye()) 
# print(say_good_afternoon())

# timed_hi = timer(say_hi)
# print(timed_hi())
# print(timed_hi.__closure__)
# print(say_hi.__closure__)

# timed_bye = timer(say_bye)
# print(timed_bye.__closure__)
# print(say_hi.__closure__)


# CLASSES
class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        # print(f'You make a cat named {self._name}')


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_name):
        if len(new_name) > 15:
            print("That's too long of a name!")
        else:
            self._name = new_name


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


    def speak(self):
        return f'{self._name} says "Meow!"'


    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(color, age, name) for color, age, name in cats]
        # print([cat.speak() for cat in new_cats])
        return new_cats


    @staticmethod
    def feed_me():
        for i in range(5):
            print('Meowwww?!?!')


make_cats = Cat.cat_factory([("black", 5, "Blue"), ("tuxedo", 5, "Patch"), ("gray", 12, 'Mimi')])
blue, patch, mimi = make_cats

# blue.feed_me()
# print(blue.name)
# blue.name = "MaverickIsAWildNameForACat"
# print(blue.name)
# print(blue.age)
# blue.age = 6
# print(blue.age)
# blue._name = "Peter"

# print(blue._name)

# print(blue.speak())
# blue = Cat(
#     age=5,
#     name='Blue',
#     color="Black"
# )

# print(blue._name)
# patch = Cat('tuxedo', 5, 'Patch')
# print(patch._name, patch._color)
# print(blue.breed)
# print(patch.breed)
# Cat.breed = "Long Hair"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# print(blue)

# GETTERS & SETTERS Problem
class Game:
    def __init__(self):
        self._score = 50
       

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value * 10

my_game = Game()
# print(my_game.score) # 0

# my_game.score = 5
# print(my_game.score) # 50
# print(my_game._score)


# INHERITANCE & POLYMORPHISM
class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        print(self.speak())

    def speak(self):
        if self._name == "Tony":
            return f"{self._name} says 'They're Great!!!'"    
        else:
            return f"{self._name} says 'RAWRRRRRWWWRRR!'"    


    def __repr__(self):
        return f'< {self._name} is a {self._color} Tiger!>'

    
    def __str__(self):
        return f'< {self._name} is a {self._color} Tiger!>'


    def __len__(self):
        return 12


tony = Tiger('orange', 20, "Tony", 30)
# print(tony.name)
# print(tony.speak())
# print(tony)
# print(len(tony))
tiger = Tiger('orange', 10, 'Tiger', 4)