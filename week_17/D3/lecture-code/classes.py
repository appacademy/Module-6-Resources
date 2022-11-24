class Pie:
    def __init__(self, name, slices, toppings):
        self._name = name
        self._slices = slices
        self._toppings = toppings
        print(f"You just made a {self._name} pie!")


    @property
    def slices(self):
        return self._slices


    @slices.setter 
    def slices(self, val):
        if val <= 0:
            print("You can't have a pie with no slices!")
        elif val > 12:
            print("Woah, those slices are too small, you need to share better!")
        elif val == 1:
            self._slices = val
            print("Hope you enjoy your pie Brian!")
        else:
            self._slices = val
    


    def is_ready(self):
        for i in range(3):
            print(f"Ding pies are done, I love {self._name} pie!")


    def __repr__(self):
        return f"< {self._name} Pie with {self._slices} slices left >"


    def __str__(self):
        return f"< {self._name} Pie with {self._slices} slices left >"


pecan_pie = Pie('Pecan', 8, ['whipped cream', 'vanilla ice cream'])
# print(pecan_pie)
# print(pecan_pie._name)
print(pecan_pie.slices)
pecan_pie.slices = 1
print(pecan_pie.slices)
# pecan_pie.is_ready()


class BerryPie(Pie):
    def __init__(self, name, slices, toppings, berries=['mystery']):
        super().__init__(name, slices, toppings)
        self._berries = berries


wild_berry = BerryPie('Wilb Berry', 12, ['more berries', 'sugar', 'whipped cream'], ['blueberry', 'blackberry'])    
    

