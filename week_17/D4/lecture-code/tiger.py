from cat import Cat


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth


    def speak(self):
        if self.name == 'Tony':
            return f"{self.name} says 'They're Great!!!!'"
        else:
            return f"{self.name} says 'RAWRRRR!!!!'"


    def __str__(self):
        return f"< {self.name} is a {self._color} Tiger >"


    def __len__(self):
        return self.age


tony = Tiger("orange", 71, 'Tony', 30)
tigger = Tiger("orange", 95, "Tigger", 28)
print(tony)
print(tony.name)
print(len(tony))