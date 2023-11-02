from cat import Cat


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        # print(self.speak())

    def speak(self):
        if self.name == 'Tony':
            return f"{self.name} says 'They're GREAT!!!!'"
        else:
            return f"{self.name} says 'RAWRR!!!!!!'"


    def __repr__(self):
        return f"< {self.name} is a {self._color} Tiger>"


    def __str__(self):
        return f"< {self.name} is a {self._color} Tiger>"


    def __len__(self):
        return self.age



tony = Tiger("orange", 70, "Tony", 30)
tigger = Tiger("orange", 95, "Tigger", 4)
print(tony)
print(len(tony))


