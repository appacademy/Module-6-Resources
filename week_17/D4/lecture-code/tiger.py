from cat import Cat


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth


    def speak(self, times=1):
        if self.name == "Tony":
            print(f"{self.name} says 'They\'re Great!!!'")
        else:
            print(f"{self.name} says 'RAWRRRWWRRR!!!!'")

    def __repr__(self):
        return f"< {self.name} is a {self._color} Tiger >"

    def __str__(self):
        return f"< {self.name} is a {self._color} Tiger >"






tony = Tiger("orange", 50, "Tony", 30)
print(tony)
print(len(tony))

