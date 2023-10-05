from cat import Cat


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth


    def speak(self):
        if self.name == "Tigger":
            return "T-I-double guh-er! That spells Tigger!"
        else:
            return f"{self.name} says 'RAWRRRRRR!!!!!'"
        

    def __repr__(self):
        return f"< {self.name} is a {self._color} Tiger >"


    def __str__(self):
        return f"< {self.name} is a {self._color} Tiger >"


    def __len__(self):
        return self.age


tigger = Tiger("orange", 50, "Tigger", 4)
hobbes = Tiger("orange", 40, "Hobbes", 12)
print(tigger)
print(tigger.speak())
print(hobbes.speak())
print(len(tigger))




