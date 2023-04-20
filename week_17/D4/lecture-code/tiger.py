from cat import Cat

class Tiger(Cat):
    breed = "Tiger"
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        print(self.speak())   


    def speak(self):
        if self._name == "Tony":
            return f"{self._name} says 'They're GREAT!!!!!'"
        else:
            return f"{self._name} says 'RAWRRRRRRRRR!!!'" 

    
    def __repr__(self):
        return f'< {self._name} is a {self._color} Tiger >'


    def __str__(self):
        return f'< {self._name} is a {self._color} Tiger >'


    def __len__(self):
        return self._age


khan = Tiger("orange", 20, "Shere Khan", 30)
tony = Tiger("orange", 60, "Tony", 14)
print(khan.name)
print(khan.breed)
print(khan)
print(len(khan))
print(len([1, 2, 3, 4, 5]))



