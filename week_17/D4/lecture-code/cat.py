
class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        # print(f"You just created a cat named {self._name}")
        # print(self.speak())


    @property
    def name(self):
        return self._name

    @name.setter 
    def name(self, new_name):
        if len(new_name) > 15:
            print("Thats too long a name for a cat")
        elif len(new_name) < 2:
            print("Cats should have at least 2 letter names")
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
            print("Cats can't have negative ages!")
        else:
            self._age = new_age


    def speak(self):
        return f"{self._name} says 'Meow!'"


    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(color, age, name) for color, age, name in cats]
        # print([cat.speak() for cat in new_cats])
        return new_cats


    @staticmethod
    def feed_me():
        for i in range(5):
            print("Meowwww?!?!?")


    def __repr__(self):
        return f"< {self._name} is a {self._color} Cat! >"

    def __str__(self):
        return f"< {self._name} is a {self._color} Cat! >"


make_cats = Cat.cat_factory([("black", 6, "Blue"),
                            ("tuxedo", 6, "Patch"),
                            ("gray", 12, "Mimi")])

blue, patch, mimi = make_cats
# blue = Cat("black", 6, "Blue")
# patch = Cat("tuxedo", 6, "Patch")
# print(blue.name)
# blue.name = "Mr. Fantastic Ninja Cat Blueberry"
# print(blue.name)
# print(blue.age)
# blue.age += 1
# print(blue.age)
# print(blue.speak())
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# # Cat.breed = "American Long Hair"
# blue.breed = "Crazy Ninja Kitty"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# blue.feed_me()
print(blue)