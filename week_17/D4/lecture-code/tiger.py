from w17d4 import Cat


# blue = Cat(age=6, color="black", name='Blue')
# print(blue)

class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        # print(self.speak())


    def speak(self):
        # print(super().speak())
        if self.name == "Tony":
            return f"{self.name} says 'They're GREAT!!!'"
        else:
            return f"{self.name} says  'RAWWRRRRWWWWRRR!'"

    

    def __repr__(self):
        return f'<{self.name} is a {self._color} Tiger!>'

    def __str__(self):
        return f'<{self.name} is a {self._color} Tiger!>'


    def __len__(self):
        return self._age


tony = Tiger("orange", 8, "Tony", 30)
hobbes = Tiger("orange", 5, "Hobbes", 12)
print(tony.speak())
print(len(tony))