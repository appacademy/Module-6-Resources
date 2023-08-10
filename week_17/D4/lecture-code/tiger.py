from cat import Cat


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        print(self.speak())


    def speak(self):
        if self.name == "Tony":
            return f"{self.name} says 'They're Great!!!!!'"
        else:
            return f"{self.name} says 'RAWWWRWRWRRWW!!!!'"


    def __repr__(self):
        return f"< {self.name} is an {self._color} Tiger >"   


    def __str__(self):
        return f"< {self.name} is an {self._color} Tiger >"   


    def __len__(self):
        return self.age


tigger = Tiger("orange", 97, 'Tigger', 4)
tony = Tiger("orange", 71, "Tony", 30)
print(tigger.speak())
print(tony.speak())
print(tony)
print(len(tigger))
# # print(len(True))
# print(len("Tiger"))