class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
       
        # print(f"You just created a cat named {self.name}")
        print(self.speak())


    @property  
    def age(self):
        return self._age

    @age.setter 
    def age(self, new_age):
        if new_age > 25:
            print('Thats too old for a cat!')
        elif new_age <= 0:
            print("Cats need to have an age!")
        else:
            self._age = new_age


    @property
    def name(self):
        return self._name

    @name.setter 
    def name(self, new_name):
        if len(new_name) > 20:
            print("Thats too long a name for a cat")
        else:
            self._name = new_name


    def speak(self):
        return f"{self.name} says, 'Meow!'"


    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(color, age, name) for color, age, name in cats]
        # print([cat.speak() for cat in new_cats])
        return new_cats


    @staticmethod
    def feed_me():
        for _ in range(5):
            print("Meowwwwww!?!?!")


    def __repr__(self):
        return f"< name: {self.name} color: {self._color} age:{self.age} >"

    def __str__(self):
        return f"< {self.name} is a {self._color} Cat >"


    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "color": self._color
        }


make_cats = Cat.cat_factory([
    ("black", 7, "Blue"),
    ("tuxedo", 7, "Patch"),
    ("gray", 12, "Mimi"),
])
blue, patch, mimi = make_cats
# blue = Cat("black", 7, "Blue")
# patch = Cat("tuxedo", 7, 'Patch')
# print(blue._age)
# blue._age = 100
# print(blue._age)
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# blue.breed = "Feisty Cat Ninja 🥷🏻"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# Cat.breed = "American Long Hair"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# patch.feed_me()
# Cat.feed_me()
print(blue.age)
blue.age = 100
print(blue.age)
blue.age = -1
print(blue.age)
blue.age = 8
print(blue.age)
blue.name = "Mr Fancypants Fiesty Ninja"
print(blue.name)
blue.name = 'Blueberry'
print(blue.name)
print(blue)
print(blue.to_dict())
