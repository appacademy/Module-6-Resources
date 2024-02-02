from cat import Cat


class Tiger(Cat):
    def __init__(self, name, age, color, stripes):
        super().__init__(name, age, color)
        self.stripes = stripes


    def speaks(self):
        return "ROOOOAAAAARARRR!!!!!"

    def __repr__(self):
        return f"<{self.name} is a Tiger with {self.stripes} stripes>"
    


hobbes = Tiger(name="Hobbes", color="orange", age="35", stripes="15")
tigger = Tiger("Tigger", 75, "orange", 20)


# print(hobbes.speaks())


# hobbes.hungry_cat(10)

print(hobbes)
print(tigger)
