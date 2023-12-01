

class Cat:
    breed = 'American Short Hair'
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        self._toys = []
        print(self.speak())


    @property
    def age(self):
        return self._age


    @age.setter
    def age(self, new_age):
        if new_age > 38:
            print("Thats too old for a cat")
        elif new_age < 0:
            print("Cat's can't have a negative age")
        else:
            self._age = new_age
  
    
    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 15:
            print('Thats too long a name for a cat')
        elif len(new_name) < 2:
            print('Cats need more than a 1 letter name')
        else:
            self._name = new_name


    def speak(self):
        return f"{self.name} says 'Meow!'"


    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(color, age, name) for color, age, name in cats]
        # print([cat.speak() for cat in new_cats])
        return new_cats

    
    @staticmethod
    def feed_me():
        [print("Meowwww?!?!") for _ in range(5)]


    def __repr__(self):
        return f"< {self.name} is a {self._color} Cat >"

    def __str__(self):
        return f"< {self.name} is a {self._color} Cat >"


# blue, patch, mimi = Cat.cat_factory([
#     ("black", 7, "Blue"),
#     ("tuxedo", 7, "Patch"),
#     ("gray", 12, "Mimi"),
# ])
# blue = Cat("black", 7, "Blue")
# patch = Cat("tuxedo", 7, "Patch")
# print(blue.age)
# print(blue.name)
# print(blue.speak())
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# Cat.breed = "American Long Hair"
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# blue.breed = "Feisty Cat Ninja 🥷🏻"
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# blue.feed_me()
# print(blue.age)
# blue.age = 39
# print(blue.age)
# blue.age = -2
# print(blue.age)
# blue.age = 8
# print(blue.age)
# patch.name = "Mr Patcheamaquati Oreo Mc Mittens"
# print(patch.name)
# patch.name = "p"
# print(patch.name)
# patch.name = 'Patrick'
# print(patch.name)
# print(blue)