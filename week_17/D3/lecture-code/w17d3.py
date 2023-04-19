# TUPLES

tup = ("red", "blue")
tup += "green", "orange"

# print(tup)
# print(tup[1:2])

empty_tuple = ()

single_tuple = 1, 
single_tuple_2 = (1,)


def sum_and_average(lst):
    list_sum = sum(lst)
    average = list_sum / len(lst)
    return (list_sum, average)


list_sum, average = sum_and_average([1, 2, 3, 4])
# print(list_sum, average)


DAYS = ("Mon", "Tue", "Wed", "Thurs", "Fri")
sorted_days = sorted(DAYS)
# print(tuple(sorted_days))


# def function(num, *args):
#     print(args)
#     for arg in args:
#         print(arg)


# # function(4, 5, 6, 7, 8)


# x = (1, 2)
# y = (3, 4)
# print("x", id(x))
# print("y", id(y))
# y = x
# print(y)
# x += 3,
# print(x, y)
# print("x", id(x))
# print("y", id(y))


# INDEX SORT

def compare(val):
    return val[1]

def index_sort(tuple_list):
    sorted_list = sorted(tuple_list, key=compare) # lambda val: val[1]
    return sorted_list



# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]



# RANGES & ENUMERATE
# values = range(start, stop, step)
values = range(10)
# print(values)
# print(list(values))

# for index in range(10):
#     print(index)


lunch = ['wings', 'pizza', 'sandwich', 'fajitas', 'burger & fries']

# for index in range(len(lunch)):
#     print(index, lunch[index])

# print(list(enumerate(lunch)))

# for index, value in enumerate(lunch, 1):
#     print(f"{index}. {value}")


# FACTORIAL
# the product of all positive integers less than or 
# equal to a given positive integer and denoted by 
# that integer and an exclamation point.
# Write your function, here.
def factorial(num):
    total = 1
    for integer in range(1, num + 1):
        total *= integer
    
    return total

# print(factorial(1))     #> 1
# print(factorial(8))     #> 40320
# print(factorial(12))    #> 479001600
# print(factorial(1000))    #> 479001600


# CHECK NESTED LISTS
# Your code, here.
def can_nest(list1, list2):
    list1_min = min(list1)
    list1_max = max(list1)
    list2_min = min(list2)
    list2_max = max(list2)

    return list1_min > list2_min and list1_max < list2_max


# print(can_nest([1, 2, 3, 4], [0, 6]))  #> True
# print(can_nest([3, 1], [4, 0]))        #> True
# print(can_nest([9, 9, 8], [8, 9]))     #> False
# print(can_nest([1, 2, 3, 4], [2, 3]))  #> False


# DICTIONARIES

meals = {
    "breakfast": "coffee",
    "lunch": "chicken sandwich",
    "dinner": "wings",
    "dessert": "ice cream",
    4: "meals",
    True: "even more meals",
    "second breakfast": "apple",
    (1,2): "tuple key",
}

# print(meals)
# print(meals["breakfast"])
# print(meals[(1,2)])
# print(meals.get(1))
# print(meals.get("elevensies", "NOPE, WE DON'T GOT THAT KEY"))

# if meals.get("elevensies") is None:
#     meals["elevensies"] = "bagel"
# else:
#     print("Key already exists")

# print(meals)
# meals["dessert"] = "apple pie"
# print(meals)
# del meals[4]
# print(meals)

more_meals = {
    "elevensies": "bagel",
    "supper": "steak"
}

# meals.update(more_meals)
# print(meals)
# print("supper" in meals)
# print("brinner" in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key, value in meals.items():
#     print(key, " - ", value)


# for val in meals.values():
#     print(val)


# ARGS/KWARGS

def sum (num1, num2, num3=30, *args, **kwargs):
    total = num1 + num2 + num3
    print(args)
    for arg in args:
        total += arg
    print(kwargs)
    for kwarg in kwargs.values():
        total += kwarg
    return total

# print(sum(10, 20, 40, 50, 60, num6=70, num7=80))


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [*list1, *list2]
# print(list3)

dict1 = {
    "breakfast": 'eggs',
    "lunch": "wings",
    "dinner": "pizza",
}

# dict2 = {*dict1}
# print(dict2)
# 
# MERGE 2 LISTS
# Write your code here.
# def merge_lists(list1, list2):
#     merged_dict = {}
#     # index = 0
#     # while index < len(list1):
#     #     merged_dict[list1[index]] = list2[index]
#     #     index += 1 
#     # for index in range(len(list1)):
#     #     merged_dict[list1[index]] = list2[index]
#     for index, value in enumerate(list1):
#         merged_dict[value] = list2[index]
#     return merged_dict

# merge_lists = lambda list1, list2: dict(zip(list1, list2))


# lst1 = ['a', 'b']
# lst2 = [1, 2]
# merged_dict = merge_lists(lst1, lst2)
# print(merged_dict)      # { 'a': 1, 'b': 2 }

# SETS

# empty_set = set()

# not_empty_set = { 1, "hello", None }
# another_set = {1, 1, 2, 3, 4, 4, 6}
# print(another_set)


# my_list = [1, 1, 1, 1, 2, 3, 4, 4, 4]
# print(list(set(my_list)))
# my_string = "hello"
# print(set(my_string))

# my_set = {1, 2, 3, 4, 5}
# print(1 in my_set)
# # print(my_set[1])
# my_set.add(6)
# print(my_set)
# my_set.update({7, 8})
# print(my_set)
# my_set.remove(2)
# print(my_set)
# for num in my_set:
#     print(num)

a = {1, 2, 3}
b = {3, 4, 5}

# UNION
# print(a | b)
# print(a.union(b))

# INTERSECTION
# print(a & b)
# print(a.intersection(b))

# DIFFERENCE
# print(a - b)
# print(b - a)
# print(a.difference(b))

# SYMMETRIC DIFFERENCE
# print(a ^ b)
# print(a.symmetric_difference(b))

# a = {1, 2, 3}
# b = {3, 4, 5}


# BUILT IN FUNCTIONS
# SORTED
names = ("JAMES", "julie", "Ana", "Ria")

# sorted_names = sorted(names, key=lambda val: val.lower(), reverse=True)
# print(tuple(sorted_names))


# ALL & ANY

test = ['', False, 0]
test2 = {}
test3= ("Brad", "David", "Keegan", "Andrew")

# all is happy if nothing inside is falsy 
# any is happy if at least one thing is truthy
# print(all(test))
# print(all(test2))
# print(all(test3))
# print(any(test))
# print(any(test2))
# print(any(test3))

# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# only_as = filter(lambda num: num >=90, scores)
# print(only_as)
# new_list = list(only_as)
# print(new_list)
# print(set(new_list))


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


# mapped_grades = map(get_grade, scores)
# print(mapped_grades)
# print(list(mapped_grades))


# ZIP 
# scores = [90, 86, 75, 91, 62, 99, 88, 90, 91, 90]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]

# zipped_scores = zip(grades, scores)
# print(zipped_scores)
# combined_list = list(zipped_scores)
# combined_dict = dict(combined_list)
# print(combined_dict)


# REMOVE DUPLICATES PROBLEM
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
#     seen = []
#     return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)
    
    # so what is going on here in the filter method???
    # think of the lambda statement being written like this...
    # if phone['model'] not in seen:
    #     return seen.append(phone['model']) is None
    # else:
    #     return False
    #
    # Because this is a callback in a filter, it needs to return True or False
    # to determine if the value gets added to our filtered list
    #
    # In the else, we return False, makes sense...
    # The append method does not have a return, but we know that if a
    # function does not have a set return value, it returns None!
    # So we check if the return value is None, which will evaluate to true!

# def get_unique_models(phone_list):
#     just_models = map(lambda phone: phone["model"], phone_list)
#     print(list(set(just_models)))

# get_unique_models(phones)


# COMPREHENSIONS

my_list = [1, "2", 'THREE', True, None]
my_list_copy = [item for item in my_list]
my_list_copy2 = [*my_list] 
# print(my_list_copy2)


nums = [-5, 11, 10, 14]
mapped_nums = [num * 2 for num in nums]
# print(mapped_nums)
# filter_nums = [num for num in nums if num > 0]
# print(filter_nums)
# mapped_and_filtered_nums = [num * 2 for num in nums if num > 0]
# print(mapped_and_filtered_nums)

# names = ["fred", "danny", "jennie", "andy"]
# mapped_names = [name.title() for name in names]
# print(mapped_names)

# DICTIONARY COMPREHENSIONS

number_dict = {num: num**2 for num in range(11)}
print(number_dict)


breaks = {
    'lunch': 2,
    "afternoon": 6,
    "EOD": 7
}

daylight_savings = {key: value + 1 for key, value in breaks.items() }
print(daylight_savings)
