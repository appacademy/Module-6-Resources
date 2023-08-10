class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name='Kitty'):
        self._color = color
        self._age = age
        self._name = name
        # print(f"You just created a cat named {self.name}")
        # print(self.speak())


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 20:
            print("That's too big for a cat name!")
        elif len(new_name) < 2:
            print("That's too small a name for a cat!")
        else:
            self._name = new_name
    
    
    @property
    def age(self):
        return self._age

    
    @age.setter 
    def age(self, new_age):
        if new_age > 30:
            print("That's too old for a cat!")
        elif new_age < 0:
            print("Cats can't have negative ages")
        else:
            self._age = new_age


    def speak(self):
        return f"{self.name} says 'Meow!'"


    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(color, age, name) for color, age, name in cats]
        print([cat.speak() for cat in new_cats])
        return new_cats


    @staticmethod
    def feed_me():
        for _ in range(5):
            print("Meowwww?!?!")


    def __repr__(self):
        return f"< {self.name} is an {self._color} Cat >"   


    def __str__(self):
        return f"< {self.name} is an {self._color} Cat >"   


# make_cats = Cat.cat_factory([
#     ("black", 7, "Blue"),
#     ("tuxedo", 7, "Patch"),
#     ("gray", 14, "Mimi"),
# ])
# blue, patch, mimi = make_cats 
# # blue = Cat("black", 7, "Blue")
# patch = Cat("tuxedo", 7, "Patch")
# print(blue.color)
# print(blue.speak())
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# Cat.breed = "American Long Hair"
# blue.breed = "Feisty Kitty Ninja"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# blue.feed_me()
# blue._color = "purple"
# print(blue.name)
# blue.name = "Freddy the super feisty cat ninja 🥷🏻"
# blue.name("Freddy")
# print(blue.name)
# blue.name = "Q"
# print(blue.name)
# blue.age = 200
# print(blue.age)
# blue.age = -2
# print(blue.age)
# blue.age = 8
# print(blue.age)
# print(blue)