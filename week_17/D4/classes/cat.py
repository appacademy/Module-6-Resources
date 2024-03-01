class Cat:
    """This is a cat class. Cats are fun but also mean"""

    demeanor = "aloof"

    def __init__(self, name, color, teeth, size, age):
        self.name = name
        self.color = color
        self.teeth = teeth
        self.size = size
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        if val > 35:
            print("Cats can't be that old!!!")
        else:
            self._age = val

    @staticmethod
    def speak():
        return "Meow!!!!!"

    @classmethod
    def cat_factory(cls, cats):
        new_cats = [cls(name, color, teeth, size, age) for name, color, teeth, size, age in cats]
        return new_cats

    def stretches_out(self):
        return f"{self.name} stretches out lazily!"

    @classmethod
    def demonstrate_aloofness(cls):
        return f"The cat sees that you are feeling sad. It is {cls.demeanor}!"

    def __len__(self):
        return self.age

    # @property
    # def __dict__(self):
        # return 5

    def __repr__(self):
        return f"<{self.name} is a {self.color} cat with {self.teeth} teeth>"


sunshine = Cat("Sunshine", "tabby", 400, "6 lbs", 20)


# print(Cat.demonstrate_aloofness())

# print(sunshine.stretches_out())

# print(sunshine.demonstrate_aloofness())


# new_cats = [Cat("Grey", "grey", 2, "25 lbs", 10), Cat("Sunshine", "tabby", 5000, "6 lbs", 2)]


# cats = [("Grey", "grey", 2, "25 lbs", 10), ("Sunshine", "tabby", 5000, "6 lbs", 2)]

# cats = Cat.cat_factory(cats)

# for cat in cats:
    # print(vars(cat))


# print(sunshine)
# print(sunshine.name)

# print(Cat)

# print(__name__)

# help(Cat)

# print(sunshine.speak())

# print(sunshine._age)

# sunshine._age += 1
# print(sunshine._age)
# print(sunshine.age)

# sunshine.age += 20

# print(sunshine.age)

# print(sunshine.age)


# print(vars(sunshine))

# print(len(sunshine))
# print(sunshine.__len__())

# print(dir(sunshine))

# class RegularPolygon:
#     type = "Polygon"
#
#     def __init__(self, num_sides, length):
#         if num_sides < 3:
#             raise Exception("A polygon must have at least 3 sides.")
#         self.num_sides = num_sides
#         self.length = length
#
#     def identify_polygon(self):
#         poly_type = {
#             3: "Triangle",
#             4: "Quadrilateral",
#             5: "Pentagon",
#             6: "Hexagon",
#             7: "Heptagon",
#             8: "Octagon",
#             9: "Nonagon",
#             10: "Decagon"
#         }
#         # try:
#             # self.type = poly_type[self.num_sides]
#         # except KeyError:
#             # self.type = f"Polygon with {self.num_sides} sides."
#
#         self.type = poly_type.get(self.num_sides,f"Polygon with {self.num_sides} sides.")
#         
#         return self.type
#
#     @classmethod
#     def polygon_factory(cls, polygons):
#         return [cls(num_sides, length) for num_sides, length in polygons]
#
#     @staticmethod
#     def get_perimeter(polygon):
#         return polygon.num_sides * polygon.length



    
# triangle = RegularPolygon(3, 1)
#
#
# # print(vars(triangle))
#
# # biangle = RegularPolygon(2, 1)
#
#
# print(triangle.type)
#
# print(triangle.identify_polygon())
#
# print(triangle.type)
# print(RegularPolygon.polygon_factory([(5, 5), (3, 2), (8, 10)]))
#
# pentagon = RegularPolygon(5, 5)
# octagon = RegularPolygon(8, 10)
# dodecagon = RegularPolygon(12, 1)
# print(RegularPolygon.get_perimeter(pentagon)) # 25
# print(RegularPolygon.get_perimeter(octagon)) # 80
# print(RegularPolygon.get_perimeter(dodecagon)) # 12
#
# print(dodecagon.identify_polygon())
