
class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        self.speak(1)


    @property
    def age(self):
        return self._age

    @age.setter 
    def age(self, new_age):
        if new_age > 25:
            print("That's too old for a cat!")
        elif new_age < 0:
            print("Cat's need to have a positive age!")
        else:
            self._age = new_age


    @property
    def name(self):
        return self._name


    @name.setter 
    def name(self, new_name):
        if len(new_name) < 2:
            print("That's too short of a name for a cat")
        
        elif len(new_name) > 15:
            print("That's too long of a name for a cat")

        else:
            self._name = new_name


    def speak(self, times=1):
        for num in range(times):
            print(f"{self.name} says 'Meow!'")
    

    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(color, age, name) for color, age, name in cats]
        # _ = [cat.speak() for cat in new_cats]
        return new_cats


    @staticmethod
    def feed_me():
        for _ in range(5):
            print("Meowwww?!?!")


    def __repr__(self):
        return f"< {self.name} is a {self._color} Cat >"

    def __str__(self):
        return f"< {self.name} is a {self._color} Cat >"

    def __len__(self):
        return self.age
        

# many_cats = Cat.cat_factory([
#     ("black", 7, "Blue"),
#     ("tuxedo", 7, "Patch"),
#     ('gray', 11, "Mimi")
# ])
# blue, patch, mimi = many_cats
# blue = Cat("black", 7, "Blue")
# patch = Cat("tuxedo", 7, "Patch")
# print(blue._name)
# # print(blue.speak(2))
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# Cat.breed = "Long Hair"
# blue.breed = "Crazy fiesty ninja 🥷🏻"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# print(patch.feed_me())
# print(blue.age)
# blue.age = 27
# print(blue.age)
# blue.age = -4
# print(blue.age)
# blue.age = 8
# print(blue.age)
# blue.name = "T"
# print(blue.name)
# blue.name = "Mr Fancy Pants Kitty McGee"
# print(blue.name)
# blue.name = "Ninja"
# print(blue.name)
# print(blue)