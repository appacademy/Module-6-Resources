from cat import Cat

class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        print(self.speak())


    def speak(self):
        if self.name == "Tony":
            return f"{self.name} says 'They're Great!!!'"
        else:
            return f"{self.name} says 'RAWRRRRRRWWWRRRR!!!'"


    def __repr__(self):
        return f"<{self.name} is an {self._color} Tiger>"


    def __len__(self):
        return self.age


tony = Tiger("orange", 50, "Tony", 6)
hobbes = Tiger("orange", 30, "Hobbes", 30)
print(tony)
print(len(tony))