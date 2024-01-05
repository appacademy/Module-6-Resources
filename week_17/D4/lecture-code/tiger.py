from cat import Cat


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self.teeth = teeth
        print(self.speak())


    def speak(self):
        if self.name == "Tony":
            return f"{self.name} says 'They're GREAT!!!'"
        else:
            return f"{self.name} says 'RAWRRRRRRWWW!!!!'"


    def __len__(self):
        return self.age


tony = Tiger("orange", 70, "Tony", 30)
tigger = Tiger("orange", 90, "Tigger", 4) 
print(len(tony))