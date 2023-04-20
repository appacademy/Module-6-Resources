
class Cat:
    breed = "American Short Hair"
    def __init__(self, color, age, name="Kitty"):       
        self._color = color
        self._age = age
        self._name = name
        # print(self.speak())


    def speak(self):
        """method to make your cat talk!"""
        return f'{self.name} says "Meow!"'


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_name):
        if len(new_name) > 20:
            print("Thats to long of a name")
        elif len(new_name) < 2:
            print("Cats should have a name thats not a single letter")
        else:
            self._name = new_name 


    @property 
    def age(self):
        return self._age


    @age.setter
    def age(self, new_age):
        if new_age > 25:
            print("Thats a bit old for a cat")
        elif new_age < 0:
            print("Cat ages should be positive values")
        else:
            self._age = new_age



    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(color, age, name) for color, age, name in cats]
        # print([cat.speak() for cat in new_cats])
        return new_cats


    @staticmethod
    def feed_me():
        for i in range(5):
            print("Meowwww?!?!")


# make_cats = Cat.cat_factory([
#     ("black", 6, "Blue"),
#     ("tuxedo", 6, "Patch"),
#     ("gray", 12, "Mimi")
# ])

# blue, patch, mimi = make_cats 
# blue = Cat("Black", 6, "Blue")
# patch = Cat("Tuxedo", 6, "Patch")
# print(blue._name)
# print(blue._age)
# print(blue.speak())
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# blue.breed = "Furry Ninja"
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# Cat.breed = "American Long Hair"
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# patch.feed_me()
# print(blue.name)
# blue.name = "S"
# print(blue.name)
# blue.name = "Mr. Blueberry Banana Pants"
# print(blue.name)
# blue.age = 29
# print(blue.age)
# blue.age = -2
# print(blue.age)



# GETTERS & SETTERS Problem
class Game:
    def __init__(self):
        self._score = 0

    @property 
    def score(self):
        return self._score

    @score.setter 
    def score(self, new_score):
        self._score = new_score * 10


# my_game = Game()
# print(my_game.score) # 0

# my_game.score = 5
# print(my_game.score) # 50