# TUPLES

# tup = ('red', 'blue')
# tup += ('green', 'orange')
# print(tup)

# tup2 = 'Brad', 'John', 'Cesar'
# print(tup2)

# tup3 = ()
# tup4 = 1,
# print(tup4)

# days = ("Mon", "Tues", "Wed", "Thur", "Fri")

# sorted_days = sorted(days)
# print(tuple(sorted_days))

# def function(num, *args):
#     print(args)

# function(1, 3, 4)

# print(days[2:4])

# RANGES & ENUMERATE
# values = range(1,10)
# print(list(values))
# values2 = range(10,0,-1)
# print(list(values2))


# drinks = ['Coffee', 'Tea', 'Soda']

# for i in range(len(drinks)):
#     print(i, drinks[i])

# print(list(enumerate(drinks)))

# for i, val in enumerate(drinks, 1):
#     print(f"{i}. {val}")


# for i in range(1,10,2):
#     print(i)

# DICTIONARIES

meals = {
    "breakfast": 'coffee',
    "lunch": "sandwich",
    "dinner": "hamburger",
    "dessert": "ice cream",
    4: "meals",
    True: "even more meals"
}

if meals.get("second breakfast") is None:
    meals["second breakfast"] = "banana"
else:
    print("Key already exists")

# print(meals)
# print(meals.get("dinner", "No brinner for you!"))
# meals["brinner"]
# print(meals['dessert'])
# meals["dessert"] = "key lime pie"
# print(meals)
# del meals['lunch']
# print(meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key in meals.keys():
#     print(key, meals[key])


# for k, v in meals.items():
#     print("key:", k, "val:", v)

# ARGS / KWARGS

def sum (num1, num2, *args, **kwargs):
    total = num1 + num2
    print(args)
    print(kwargs)
    for val in args:
        total += val
    for more_vals in kwargs.values():
        total += more_vals
    return total

# print(sum(10, 15, 25, 35, num5=15, num6=20 ))

lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]
lst3= [*lst1, *lst2]
# print(lst3)

dict1 = {
    "breakfast": "cereal",
    "lunch": "salad",
    "dinner": "chicken"
}

dict2 = {**dict1}

# print(id(dict1))
# print(id(dict2))

# SETS
# new_set = set()
# another_new_set = {1, 2, 3}

# lst = [1, 1, 3, 3, 4, 5, 6, 6]
# print(set(lst))

# my_string = 'hello'
# print(set(my_string))

# new_thing = set()
# print(type(new_thing))

# SET UNION
a = {0, 1, 3}
b = {0, 1, 2, 5}

# print(a | b)
# print(a.union(b))

# SET INTERSECTION
# print(a & b)
# print(a.intersection(b))

# SET DIFFERENCE
# print(a - b)
# print(b - a)
# print(a.difference(b))

# SYMMETRIC DIFFERENCE
# print(a ^ b)
# print(b.symmetric_difference(a))

# BUILT IN FUNCTION
# SORTED
names = ["JAMES", "julie", "Ana", "Ria"]
sorted_names = sorted(names, key= lambda x: x.lower(), reverse=True)
# print(sorted_names)

# ANY & ALL
test = [0, False, ""]
# print(all(test)) # False
# print(any(test)) # True

# FILTER
scores = [90, 86, 75, 91, 62, 99, 88, 90]
only_a_scores = filter(lambda num: num >= 90, scores)
# print(list(only_a_scores))

# MAP
def get_grade(num):
    if (num >= 90):
        return "A"
    elif (num <90 and num >= 80):
        return "B"
    elif (num < 80 and num >= 70):
        return "C"
    elif (num < 70 and num >= 60):
        return "D"
    else:
        return "F"


scores = [90, 86, 75, 91, 62, 99, 88, 90]
# print(map(get_grade, scores))  # <map object at 0x106faffa0>
# grades = list(map(get_grade, scores))
# print(grades)

scores = [90, 86, 75, 91, 62, 99, 88, 90, 80, 100]
grades = ['A', 'B', 'C', 'A', 'D', 'A', 'B', 'A']

combined = zip(scores, grades)
combined_list = list(combined)
combined_dict = dict(combined_list)
# print(combined)       # <zip object at 0x1023a9600>
# print(combined_list)  # [(90, 'A'), (86, 'B'), (75, 'C'), (91, 'A'), (62, 'D'), (99, 'A'), (88, 'B'), (90, 'A')]
# print(dict(combined_list))


# COMPREHENSIONS
my_list = [1, "2", "three", True, None]
my_list_copy = [ item for item in my_list]
# print(my_list)
# print(my_list_copy)

for item in my_list:
    my_list_copy.append(item)

nums = [-5, 11, 10, 14]

# mapped_nums = map(lambda n: n * 2, nums)
# print(list(mapped_nums))
# comprehension_nums = [ num * 2 for num in nums]
# print(comprehension_nums)

# filter_nums = filter(lambda n: n > 0, nums)
# print(list(filter_nums))
# filter_comp_nums = [ num for num in nums if num > 0 ]
# print(filter_comp_nums)

number_dict = {num: num**2 for num in range(5)}
# print(number_dict) 

breaks = {
    "lunch": 3,
    "afternoon": 5,
    "EOD": 7
}

daylight_savings = { k: v + 1 for k, v in breaks.items()}
print(daylight_savings)