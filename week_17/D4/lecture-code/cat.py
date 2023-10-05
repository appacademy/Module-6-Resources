
class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):
        self._color = color
        self._age = age
        self._name = name
        # self.breed = "Feisty Ninja Kitty"
        # print(f"You just made a cat named {self.name}")
        # print(self.speak())


    def speak(self):
        return f"{self.name} says 'Meow!'"


    @property
    def name(self):
        return self._name

    
    @name.setter 
    def name(self, new_name):
        if len(new_name) > 25:
            print("Thats too long a name for a cat")

        elif len(new_name) < 2:
            print("Cats should have names with more than 1 letters")
        
        else:
            self._name = new_name


    @property 
    def age(self):
        return self._age

    
    @age.setter 
    def age(self, new_age):
        if new_age > 30:
            print("Thats too old of an age for a cat")

        elif new_age < 0:
            print("Cat do need positive ages")

        else:
            self._age = new_age


    @classmethod
    def cat_factory(cls, cats):
       new_cats = [cls(color, age, name) for color, age, name in cats]
    #    print([cat.speak() for cat in new_cats]) 
       return new_cats 

    @staticmethod
    def feed_me():
        # _ = [print("Meowwwww?!?!?!") for i in range(5)]
        for i in range(5):
            print("Meowwwww?!?!?!")


    def __repr__(self):
        return f"< {self.name} is a {self._color} Cat >"


    def __str__(self):
        return f"< {self.name} is a {self._color} Cat >"

    
# blue, patch, mimi = Cat.cat_factory([
#     ("black", 7, "Blue"),
#     ("tuxedo", 7, "Patch"),
#     ("gray", 12, "Mimi")
# ])    


# blue = Cat("black", 7, 'Blue')
# patch = Cat("tuxedo", 7, 'Patch')

# print(blue._name)
# print(blue.name)
# print(blue.speak())
# blue.name = "P"
# print(blue.name)
# blue.name = "Mr Fiesty Crazy Ninja Cat with too much energy"
# print(blue.name)
# blue.name = 'Blueberry'
# print(blue.name)
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# # Cat.breed = "American Long Hair"
# blue.breed = "Feisty Ninja Kitty"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# blue.feed_me()
# blue.age = 45
# print(blue.age)
# blue.age = -4
# print(blue.age)
# blue.age += 50
# print(blue.age)
# print(blue)