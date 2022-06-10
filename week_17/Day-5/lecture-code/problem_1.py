class Cat:
    def __init__(self, color, age, name="Kitty"):
        self._age = age
        self._color = color
        self._name = name


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name    

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age > 25:
            print("That is too old for a cat!")
        elif new_age < 0:
            print("You can't have a negative age!")
        else:
            self._age = new_age
    
    
    def speak(self):
        return f'{self.name} says Meow!'


    @staticmethod
    def feed_me():
        for i in range(5):
            print("Meowwwww!?")

    @classmethod
    def cat_factory(cls, cats):
        cats = [cls(color, age, name) for color, age, name in cats]
        print([cat.speak() for cat in cats])
        return cats


