from datetime import datetime


def timer(func):
    """
    function that wraps another function 
    to time how low the wrapped function 
    takes to execute 
    """
    def wrapper(*args, **kwargs): #<- "Brad", "Autumn"
        # arg -> ("Brad", "Autumn") 
        start_time = datetime.now()
        val = func(*args, **kwargs) #< - "Brad", "Autumn"
        print(val)
        end_time = datetime.now()
        time_elapsed = end_time - start_time
        return time_elapsed
    return wrapper


@timer
def say_hi(name1, name2):
    return f"Hi {name1} and {name2}!"

@timer
def say_bye():
    return "See ya later buddy!"

@timer
def say_good_afternoon():
    return "Hope you have a swell afternoon!"

# timed_bye = timer(say_bye)
# print(timed_bye())
# timed_hi = timer(say_hi)
# print(timed_hi())
# print(say_bye())
# print(say_hi("Brad", "Autumn"))
# print(say_good_afternoon())


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


@power_of_two
@multiply_by_three
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
        # print(f'You made a cat named {self._name}')


    @property
    def age(self):
        return self._age


    @age.setter
    def age(self, new_age):
        if new_age > 25:
            print("Thats too old for a cat!")
        elif new_age < 0:
            print("Cat's can't have a negative age")
        else:
            self._age = new_age


    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 20:
            print("That's too long a name for a cat!")
        elif len(new_name) < 2:
            print("Cats deserve more than a single letter name")
        else:
            self._name = new_name


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
            print('Meeooowwwww?!?!?!')


    def __repr__(self):
        return f"< {self._name} is a {self._color} Cat >"


# blue = Cat("black", 6, "Blue")
# patch = Cat("tuxedo", 6, "Patch")
blue, patch, mimi = Cat.cat_factory([('black', 6, "Blue"), ("tuxedo", 6, "Patch"), ("gray", 12, "Mimi")])
# print(blue.speak())
# print(blue.breed)
# print(patch.breed)
# # blue.breed = "American Long Hair"
# Cat.breed = "Maine Coon"
# print(blue.breed)
# print(patch.breed)
# blue.feed_me()
# print(blue.age)
# blue.age = 26
# print(blue.age)
# blue.name = "Toothless"
# print(blue.name)
print(blue)


# INHERITANCE


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        print(f'You made a tiger named {self._name}')


    def speak(self):
        if self._name == "Tony":
            return f"{self._name} says 'They're Great!!!'"
        else:
            return f"{self._name} says 'RAWWWWRRRRRR!!!'"


    def __repr__(self):
        return f"< {self._name} is a {self._color} Tiger >"


    def __len__(self):
        return self._age


tony = Tiger("orange", 20, "Tony", 30)
hobbes = Tiger('orange', 10, "Hobbes", 10)
# print(tony.speak())
# print(hobbes.speak())
print(tony)
print(len(tony))