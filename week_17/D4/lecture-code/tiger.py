from w17d4 import Cat


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth


    def __repr__(self):
        return f"< {self.name} is a {self._color} tiger! >"

    def __str__(self):
        return f"< {self.name} is a {self._color} tiger! >"


    def __len__(self):
        return self.age


    def speak(self):
        if self.name == "Hobbes":
            return f"{self.name} says RWARRRA!!!.  And 'hey Calvin'"
        elif self.name == "Tony":
            return f"They're GREAT!!!"
        else:
            return f"{self.name} says RWARRRRRRR!!!"


hobbes = Tiger('orange', 10, "Hobbes", 30)
tony = Tiger('orange', 30, "Tony", 30)
print(hobbes)
print(hobbes.speak())
print(tony.speak())
print(len(hobbes))