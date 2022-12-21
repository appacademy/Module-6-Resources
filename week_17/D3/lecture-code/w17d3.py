# TUPLES

colored_lights = ("red", "blue")
# print(colored_lights)
colored_lights += "green", "yellow"
# print(colored_lights)
# print(colored_lights[1:3])
# colored_lights += 'green',
# print(colored_lights)

# EMPTY TUPLE
tup1 = ()
# SINGLETON TUPLE
tup2 = 1, 
tup3 = (1,)

# for light in colored_lights:
#     print(light)


DAYS = ("Mon", "Tue", "Wed", "Thurs", "Fri")

# def sum_and_average(lst):
#     list_sum = sum(lst)
#     average = list_sum / len(lst)
#     return (list_sum, average)

# sum1, avg1 = sum_and_average([1, 2, 3, 4])
# print(type(sum1))
# print(avg1)

# new_days = DAYS[:3] + "Funday" + DAYS[3:]

# print(type(DAYS))

sorted_days = sorted(DAYS)
# print(tuple(sorted_days))

# def function(num, *args):
#     print(args)


# function(1, 2, 3, 4)

# Problem 6 - Index Sort
# Write your function, here.

def compare(val):
    return val[len(val)//2]

def index_sort(tuple_list):
    tuple_list.sort(key=compare) # lambda x: x[1]
    return tuple_list



# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]


def add_value(tup, val):
  lst = list(tup).append(val)
  return tuple(lst)


# FILL TUPLE
# Create a function that takes in a tuple of tuples with 
# varying lengths, a given value, and a given length. 
# The function should return a copy of tuple where 
# each nested tuple has the specified length. 
# To increase a tuple's length, the function should append 
# the value the necessary number of times. 
# (You may assume that all tuples originally in the 
# tuple have a length <= length.)
# Write your function, here.
def fill_tuple(tup, val, length):
    return_lst = []
    for t in tup:
        return_lst.append( t + (val,) * (length - len(t)))
    return tuple(return_lst)

# print(fill_tuple(((58, 1, 5), (0, 3), (45, ), (24, 23)), 2, 3))    #> ((58, 1, 5), (0, 3, 2), (45, 2, 2), (24, 23, 2))
# print(fill_tuple(((1, ), (5, 7), (55, 22), (80, 52, 20)), 5, 4))   #> ((1, 5, 5, 5), (5, 7, 5, 5), (55, 22, 5, 5), (80, 52, 20, 5))
# print(fill_tuple(((), (0, 14), (5, 2, 8), (2, 4, 2, 3)), 0, 5))    #> ((0, 0, 0, 0, 0), (0, 14, 0, 0, 0), (5, 2, 8, 0, 0), (2, 4, 2, 3, 0))

# RANGES & ENUMERATE

# values = range(1, 10, 1)
# print(tuple(values))

carols = ["Deck the halls", "Silent Night", "Jingle Bells", "Santa Clause is coming to town"]

# for i in range(len(carols)):
#     print(carols[i])

# print(list(enumerate(carols, 1)))

# for i, v in enumerate(carols, 1):
#     print(f'{i}. {v}')

# DICTIONARY

xmas_meals = { 
    "breakfast": "coffee",
    "lunch": "pastries and more coffee",
    "dinner": "roast beast",
    "dessert": "pecan pie",
    4: "num of xmas meals",
}

# print(xmas_meals)
# print(xmas_meals['dinner'])
# print(xmas_meals['second breakfast'])

# print(xmas_meals.get("dinner"))
# print(xmas_meals.get("second breakfast", "key not in dictionary"))

# if xmas_meals.get("second breakfast") is None:
#     xmas_meals['second breakfast'] = 'apple'
# else:
#     print("Key already exists")

# print(xmas_meals)
# del xmas_meals['dinner']
# print(xmas_meals)
# print("dinner" in xmas_meals)
# print("third dinner" in xmas_meals)

# print(xmas_meals.keys())
# print(xmas_meals.values())
# print(xmas_meals.items())

# for key in xmas_meals.keys():
#     print(key)
#     print(xmas_meals[key])

# for k, v in xmas_meals.items():
#     print(k, v)
from time import sleep

days_of_xmas = {
    1: "Partridge in a pear tree",
    2: "Turtle doves",
    3: "French hens",
    4: "Calling birds",
    5: "Golden rings!",
    6: "Geese a laying",
}

# for i in range(1, len(days_of_xmas) + 1):
#     print(f"on the {i} day of xmas my true love gave to me...")
#     for j in range(i, 0, -1):
#         sleep(1)
#         print(j, days_of_xmas[j])


# ARGS/KWARGS
# 

def sum(num1, num2, num3 = 5, *args, **kwargs):
    total = num1 + num2 + num3
    print("total after positional and key word args",total)
    print(args)
    for val in args:
        total += val
    print("total after args are added in",total)
    print(kwargs)
    for more_vals in kwargs.values():
        total += more_vals
    print("total after kwargs are added in",total) 
    return total

# sum(10, 15, 10, 25, 30, num6 = 35, num7= 40)


lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]
lst3= [*lst1, *lst2]
# print(lst3)

dict1 = {
    'breakfast': "eggs",
    'lunch': "wings",
    'dinner': "pizza",
}
# dict2 = {*dict1}
# print(dict2)

# SETS

new_set = set()
set2 = {1, 2, 3, 4}
# print(new_set)
# print(set2)

# list1 = [1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 7]
# print(list(set(list1)))

# string1 = "hello"
# print(set(string1))

# my_set = {1, 2, 3, 4}
# print(1 in my_set)

# for val in my_set:
#     print(val)

# my_set.add(5)
# print(my_set)
# my_set.update([6, 7])
# print(my_set)
# my_set.remove(4)
# print(my_set)
# my_set.add(2)
# print(my_set)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# UNION
# print( a | b)
# print(a.union(b))

# INTERSECTION
# print( a & b)
# print( a.intersection(b))

# DIFFERENCE
# print( a - b)
# print( a.difference(b))
# print( b - a)
# print(len(a))

# SYMMETRIC DIFFERENCE
# print(a ^ b)
# print(a.symmetric_difference(b))


def remove_repeats(str1, str2):
    set_intersection = set(str1) & set(str2)
    results = set()
    all_chars = set(str1 + str2)
    for char in all_chars:
        if char not in set_intersection:
            results.add(char)

    return results

str1 = 'aloha'
str2 = 'bonjour'

# print(remove_repeats(str1, str2)) #{'r', 'a', 'l', 'h', 'n', 'b', 'j', 'u'}



# BUILT IN FUNCTIONS

# names = ["JAMES", "julie", "Ana", "Ria"]
# sorted_names = sorted(names, key= lambda x: x.lower(), reverse=True)
# print(sorted_names)

# ANY / ALL

test = [ 0, "yes"]
test2 = {}
# print(all(test))
# print(any(test))
# print(all(test2))
# print(any(test2))

# FILTER
scores = [90, 86, 75, 91, 62, 99, 88, 90, 61, 62]
# only_as = filter(lambda num: num >= 90, scores)
# print(tuple(only_as))


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

mapped_grades = map(get_grade, scores)
# print(mapped_grades)
mapped_grades_list = list(mapped_grades)
# print(list(mapped_grades))

# ZIP
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
# combined = zip(grades, scores)
# print(combined)
# print(list(combined))

phones = [
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "alpine green"
    },
    {
        "brand": "Samsung",
        "model": "Galaxy S22+",
        "cost": 999,
        "color": "black"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "kinda coral"
    },
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "gold"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "stormy black"
    }
]

# REMOVE DUPLICATES SOLUTION EXPLAINED

# def get_unique_models(phone_list):
#     # just_models = map(lambda phone: phone["model"], phone_list)
#     comp_models = [ phone["model"] for phone in phone_list]
#     # print(list(set(just_models)))
#     print(set(comp_models))

# get_unique_models(phones)

# def get_unique_models(phone_list):
#     seen = []
#     return filter(lambda phone:  seen.append(phone['model'] is None  if phone['model'] not in seen else False, phone_list))
    
#     # so what is going on here in the filter method???
#     # think of the lambda statement being written like this...
#     if phone['model'] not in seen:
#         return seen.append(phone['model']) is None
#     else:
#         return False
#     #
#     # Because this is a callback in a filter, it needs to return True or False
#     # to determine if the value gets added to our filtered list
#     #
#     # In the else, we return False, makes sense...
#     # The append method does not have a return, but we know that if a
#     # function does not have a set return value, it returns None!
#     # So we check if the return value is None, which will evaluate to true!

# COMPREHENSION

# my_list = [1, '2', "THREE", True, None]
# my_list_copy = [item for item in my_list]
# my_list_copy2 = [*my_list]
# print(my_list_copy)

nums = [ -5, 5, 10, 23, 44]
mapped_nums = map(lambda num: num * 2, nums)
# print(list(mapped_nums))
# nums_comp = [ num * 2 for num in nums]
# print(nums_comp)

filtered_nums = filter(lambda num: num > 9, nums)
# print(list(filtered_nums))
# comp_filter = [num for num in nums if num > 9]
# print(comp_filter)

map_and_filter = [ num * 2 for num in nums if num > 9 ]
# print(map_and_filter)


number_dictionary = { num: num**2 for num in range(6)}
# print(number_dictionary)

breaks = {
    'lunch': 2,
    'afternoon': 6,
    'EOD': 7,
}

daylight_savings = { k: v + 1 for k, v in breaks.items()}
print(daylight_savings)