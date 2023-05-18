LUNCH = "Turkey Sandwich"

class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        # self.breed = "Crazy Ninja Kitty"  # override a class 
        # atrribute by changing it on the intance
        # print(f"You made a cat named {self.name}")


    @property
    def age(self):
        return self._age

    @age.setter 
    def age(self, new_age):
        if new_age > 30:
            print("Thats too old for a cat!")
        elif new_age < 0:
            print("Cats can't have a negative age!")
        else:
            self._age = new_age

    
    @property 
    def name(self):
        return self._name


    @name.setter 
    def name(self, new_name):
        if len(new_name) > 20:
            print("That's too long of a name for a cat!")
        else:
            self._name = new_name


    
    def speak(self):
        return f'{self.name} says "MEOW!"'


    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(color, age, name) for color, age, name in cats]
        # print([cat.speak() for cat in new_cats])
        return new_cats


    @staticmethod 
    def feed_me():
        for i in range(5):
            print("Meowwww?!?!")


    def __repr__(self):
        return f"<{self.name} is a {self._color} Cat>"
    


# make_cats = Cat.cat_factory(
#     [   ("black", 6, "Blue"),
#         ("tuxedo", 6, "Patch"),
#         ("gray", 15, "Mimi")
#     ]
# )
# blue, patch, mimi = make_cats

# blue = Cat("black", 6, "Blue")
# patch = Cat("tuxedo", 6, "Patch")
# print(blue._color)
# print(blue.speak())
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# blue.breed = "Crazy Ninja Kitty"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# Cat.breed = "Long Hair"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# patch.feed_me()
# print(patch.age)
# patch.age = -1
# print(patch.age)
# blue.name = "Ninja"
# print(blue.name)
# print(blue)


# Declare your class here
# class BadCalculator:
#     def __init__(self, num1, num2):
#         self._num1 = num1
#         self._num2 = num2    

    
#     def change_nums(self, val1, val2):
#         self._num1 = val1
#         self._num2 = val2


#     def mult_nums(self):
#         return self._num1 * self._num2

    
#     def div_nums(self):
#         if self._num2 == 0:
#             print("Sorry we can not divide by zero!")
#         else:
#             return self._num1 / self._num2


#     def __repr__(self):
#         return f"<Bad Calculator - can only do {self._num1}*{self._num2} and {self._num1}/{self._num2}>"
    

#     def __str__(self):
#         return f"<Bad Calculator - can only do {self._num1}*{self._num2} and {self._num1}/{self._num2}>"



# pair_1 = BadCalculator(15, 3)
# print(pair_1) # <Bad Calculator - can only do 15*3 and 15/3>

# print(pair_1.mult_nums()) # 45 
# print(pair_1.div_nums()) # 5.0

# pair_1.change_nums(4, 0)
# print(pair_1) # <Bad Calculator - can only do 4*0 and 4/0>

# print(pair_1.mult_nums()) # 0
# print(pair_1.div_nums()) # Sorry, I cannot divide by zero
