class Cat:
    num_teeth = 44
    def __init__(self, name, age, color="black"):
        self._name = name
        self.age = age
        self.color = color
        self.demeanor = "aloof"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if len(val) > 10:
            print("That's too long a name for a cat!!!")
        else:
            self._name = val

    def stretches_out(self):
        print(f"{self.name} stretches out lazily!")

    def has_birthday(self):
        self.age += 1

    def speaks(self):
        return "Meooowwwww!!"

    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(name, age, color) for name, age, color in cats]
        return new_cats

    @staticmethod
    def hungry_cat(how_hungry):
        for _ in range(how_hungry):
            print("Meoooowwwww!!!")

    # def __len__(self):
    #     return self.age
    #
    # def __lt__(self, other):
    #     return self.age < other.age

    def __repr__(self):
        return f"<{self.name} is a {self.color} Cat>"

    


# Cat.hungry_cat(9)



# print(Cat.age)

new_cats = [("Grey", 10, "grey"), ("Sunshine", 29, "tabby"), ("Henry", 3, "black")]

cats = Cat.cat_factory(new_cats)
grey, sunshine, henry = cats

# print(cats)
# cats.sort()
# print(cats)

# print(grey)

# print(len(grey))

# new_cats = [Cat(name, age, color) for name, age, color in new_cats]



# grey = Cat("Grey", 10, "grey")
# sunshine = Cat("Sunshine", 29, "tabby")


# print(type(grey))
# print(grey.name)
# print(grey.age)
# print(grey.color)
# print()
# print(sunshine.name)
# print(sunshine.age)
# print(sunshine.color)
# print()
# grey.stretches_out()
# sunshine.stretches_out()

# grey.has_birthday()
# print(grey.age)
# print(grey.num_teeth)
# print(Cat.num_teeth)
#
# grey.num_teeth = 43
#
# print(grey.num_teeth)


# sunshine.name = "Grendelllllllll"
# sunshine.name = "Grendel"
# print(sunshine.name)


# print(sunshine._name)

# sunshine._name = "GREEEEEEEEEEEENNNNNNSEEEEL"

# print(sunshine.name)



