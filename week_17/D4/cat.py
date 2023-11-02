
class Cat:
    breed = "American short hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        self._toys = []
        # self.breed = "Feisty Cat Ninja 🥷🏻"
        print(self.speak())


    @property
    def age(self):
        return self._age

    
    @age.setter 
    def age(self, new_age):
        if new_age > 25:
            print("Thats too old for a cat")
        elif new_age < 0:
            print("Cats can't have negative ages")
        else:
            self._age = new_age

    
    @property
    def name(self):
        return self._name


    @name.setter 
    def name(self, new_name):
        if len(new_name) > 20:
            print(f"{new_name} is too long a name for a cat")
        elif len(new_name) < 2:
            print("Thats too short of a name for a cat!")
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
        for _ in range(5):
            print("Meowwww?!?!")

    def __repr__(self):
        return f"< {self.name} is a {self._color} Cat>"



# blue = Cat("black", 7, "Blue")
# patch = Cat("tuxedo", 7, "Patch")
# blue, patch, mimi = Cat.cat_factory([
#     ("black", 7, "Blue"),
#     ("tuxedo", 7, "Patch"),
#     ("gray", 12, "Mimi"),
# ])
# print(blue.age)
# blue.age = 80
# print(blue.age)
# blue.age = -80
# print(blue.age)
# blue.age = 8
# print(blue.age)
# print(blue.name)
# blue.name = "Mr Fancypants Ninja kitty!!!!!!!!"
# print(blue.name)
# blue.name = "b"
# print(blue.name)
# blue.name = "Blueberry"
# print(blue.name)
# print(blue.speak())

# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# Cat.breed = 'American long hair'
# blue.breed = "Feisty Cat Ninja 🥷🏻"
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# blue.feed_me()
