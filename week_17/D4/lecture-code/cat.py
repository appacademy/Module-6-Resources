


# def this_func():
#     pass


class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._age = age
        self._color = color
        self._name = name
        # self.breed = "Feisty Kitty Ninja"
        # print(f"You just created a cat named {self.name}")
        print(self.speak())


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_name):
        if len(new_name) > 15:
            print("Thats too long a name for a cat!")
        else:
            self._name = new_name


    @property 
    def age(self):
        return self._age


    @age.setter 
    def age(self, new_age):
        if new_age > 32:
            print('Thats too old an age for a cat')
        elif new_age < 0:
            print("Cats can't have negative age!")
        else:
            self._age = new_age



    def speak(self):
        return f"{self.name} says 'Meow!'"


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
        return f"< {self._color} Cat named {self.name} >"


    def __str__(self):
        return f"< {self._color} Cat named {self.name} >"



# make_cats = Cat.cat_factory([("black", 7, "Blue"),('tuxedo', 7, "Patch"),("gray", 12, "Mimi")])
# blue, patch, mimi = make_cats
# blue = Cat("black", 7, "Blue")
# patch  = Cat("tuxedo", 7, "Patch")
# print(blue._age)
# print(blue.speak())
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# Cat.breed = "American Long Hair"
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# blue.breed = "Feisty Kitty Ninja 🥷🏻"
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# print(blue.feed_me())
# print(blue.name)
# blue.name = "Festy Mr McNinja Pantalones!"
# print(blue.name)
# blue.name = "Freddy"
# print(blue.name)
# blue.age = 40
# print(blue.age)
# blue.age = -2
# print(blue.age)
# blue.age = 8
# print(blue.age)
# print(blue)