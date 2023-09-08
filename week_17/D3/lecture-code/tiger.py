from cat import Cat

class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        print(self.speak())


    def speak(self):
        if self.name == "Tony":
            return f"{self.name} says'They're GREAT!!!'"
        else:
            return f"{self.name} says 'Rawwrrrrrwww!!!'"
 
    def __str__(self):
        return f"< {self.name} is a {self._color} Tiger >"


    def __len__(self):
        return self.age

 
tony = Tiger("orange", 20, "Tony", 30)
hobbes = Tiger("orange", 30, "Hobbes", 4)
print(tony)
print(len("Hobbes"))
print(len(tony))