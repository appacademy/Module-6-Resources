# from random import choice, shuffle

# desserts = ['Ice cream', 'Cake', 'Pie', 'More Pie']
# print(choice(desserts))
# print(desserts)
# shuffle(desserts)
# print(desserts)
# from helpers import add2 
# from helpers.helpers import add4

# print(add2(4))
# print(add4(4))


# DECORATORS
# from datetime import datetime

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = datetime.now()
#         val = func(*args, **kwargs)
#         print(val)
#         end_time = datetime.now()
#         total_time = end_time - start_time
#         return total_time

#     return wrapper

# @timer
# def say_hi(num, name="brad"):
#     return "hello!"

# # timed_hi = timer(say_hi)
# # print(timed_hi())
# print(say_hi(4, name="John"))


# CLASSES
class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._age = age
        self._color = color
        self._name = name
        self._breed = 'American'
        print(f"You successfully created a cat named {self.name}!")


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name    

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age > 25:
            print("That is too old for a cat!")
        elif new_age < 0:
            print("You can't have a negative age!")
        else:
            self._age = new_age
    
    
    def speak(self):
        return f'{self.name} says Meow!'


    @staticmethod
    def feed_me():
        for i in range(5):
            print("Meowwwww!?")

    @classmethod
    def cat_factory(cls, cats):
        cats = [cls(color, age, name) for color, age, name in cats]
        print([cat.speak() for cat in cats])
        return cats


# blue = Cat(
#     age=5, 
#     name='Blue', 
#     color="black"
# )
# new_cats = Cat.cat_factory([("tuxedo", 5, "Patch"), ('gray', 12, 'Mimi')])
# patch, mimi = new_cats

# blue.feed_me()
# print(blue.name)
# blue.name = "Not Blue"
# print(blue.name)
# blue.age = 12
# print(blue.age)
# print(len(blue))
# patch = Cat("tuxedo", 5, 'Patch')
# print(blue.name)
# print(blue.breed)
# # print(blue.speak())
# print(patch.name)
# print(patch.breed)
# patch.breed = "Long Hair"
# print(patch.breed)
# print(blue.breed)
# Cat.breed = "Minx"
# print(patch.breed)
# print(blue.breed)

class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self.teeth = teeth

    def speak(self):
        return f'{self.name} says RAWRWWRRR!'

    def __repr__(self):
        return f'< {self.name} is a {self._color} Tiger!>'

    def __str__(self):
        return f'< {self.name} is a {self._color} Tiger!>'

    def __len__(self):
        return self.age


tigger = Tiger("orange", 35, "Tigger", 4)
print(tigger.name)
print(tigger.speak())
# print(dir(tigger))
print(tigger)
print(len(tigger))

