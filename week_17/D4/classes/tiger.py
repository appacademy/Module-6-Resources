from cat import Cat


class Tiger(Cat):
    def __init__(self, name, color, teeth, size, age, stripes):
        super().__init__(name, color, teeth, size, age)
        self.stripes = stripes

    def stretches_out(self):
        return f"{self.name} stretches out majestically. His {self.stripes} stripes look pretty cool."

    def __repr__(self):
        return f"<{self.name} is a {self.color} tiger with {self.stripes} stripes>"




tony = Tiger("Tony", "orange and black", 0, "large", 80, 15)

print(tony)


print(tony.stretches_out())
