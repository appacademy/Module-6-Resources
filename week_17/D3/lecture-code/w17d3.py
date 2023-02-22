# TUPLES
tup = ("red", "blue")
tup += "green", "orange"

# print(tup)
# print(tup[2])
# print(tup[1:3])

# EMPTY TUPLES
tup_2 = ()
tup_3 = tuple()

# SINGELTON TUPLE
tup_4 = 1,
tup_5 = (2,)

DAYS = ("MON", "TUE", "WED", "THURS", "FRI")

def sum_and_average(lst):
    list_sum = sum(lst)
    average = list_sum / len(lst)
    return (list_sum, average)

sum_val, avg_val = sum_and_average([1, 2, 3, 4])
# print(sum_val, avg_val)

sorted_days = sorted(DAYS)
# print(tuple(sorted_days))


def function(num, *args):
    for arg in args:
        print(arg)

# function(1,2,3)

# INDEX SORT
# Write your function, here.
def compare(val):
    return val[1]

def index_sort(tup_list):
    # tup_list.sort(key=compare) # lambda x: x[1]
    # return tup_list 
    sorted_list = sorted(tup_list, key=compare) 
    return sorted_list  



# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]


# RANGES & ENUMERATE

values = range(10, 0, -1)
# print(values)
# print(list(values))

lunch = ["Wings", "Pizza", "Sandwich", "Soup"]

# for index in range(len(lunch)):
#     print(index, lunch[index])


# print(list(enumerate(lunch)))

# for index, value in enumerate(lunch, 1):
#     print(f"{index}.", value)


# Check Nested List
def can_nest(list_1, list_2):
    list_1_min = min(list_1)
    list_1_max = max(list_1)
    list_2_min = min(list_2)
    list_2_max = max(list_2)
    return list_1_min > list_2_min and list_1_max < list_2_max



# print(can_nest([1, 2, 3, 4], [0, 6]))  #> True
# print(can_nest([3, 1], [4, 0]))        #> True
# print(can_nest([9, 9, 8], [8, 9]))     #> False
# print(can_nest([1, 2, 3, 4], [2, 3]))  #> False


# DICTIONARIES

# meals = {
#     "breakfast": "coffee",
#     "lunch": "mac n cheese",
#     "dinner": "wings",
#     "dessert": "ice cream",
#     4: "meals",
#     6: "number of scoops of ice cream brad will eat",
# }

# print(meals["lunch"])
# print(meals)

# print(meals.get("second breakfast", "Key does not exist!"))
# print(meals["second breakfast"])

# if meals.get("second breakfast") is None:
#     meals["second breakfast"] = "apple"
# else:
#     print("Key already exists")

# print(meals)

# meals["dinner"] = "pizza"
# print(meals)
# del meals[4]
# print(meals)
# meals[1] = "apple"
# print(meals)

# print("lunch" in meals)
# print("brinner" in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key in meals.keys():
#     print(key)

# for value in meals.values():
#     print(value)


# for key, value in meals.items():
#     print(key, ": ", value)


# ARGS / KWARGS
def sum_stuff(num_1, num_2, num_3=15, *args, **kwargs):
    total = num_1 + num_2 + num_3
    print(args)
    for arg in args:
        total += arg
    print(kwargs)
    for val in kwargs.values():
        total += val
    return total


# print(sum_stuff(5, 10, 20, 25, 30, num_6=35, num_7=40 ))

list_1 = ['a', 'b', 'c']
list_2 = [1, 2, 4]
list_3 = [*list_1, *list_2]
# print(list_3)

meals = {
    "breakfast": "coffee",
    "lunch": "mac n cheese",
    "dinner": "wings",
    "dessert": "ice cream",
    4: "meals",
    6: "number of scoops of ice cream brad will eat",
}

dict_2 = {**meals}
# print(dict_2)

# Concat Dictionaries
def concatenate_dictionaries(lst):
    new_dict = {}
    for dct in lst:
        # new_dict = { **new_dict, **dct}
        new_dict.update(dct)
        # print(new_dict)
    return new_dict

lst = [
    {
        'a': 'this',
        'b': 'is'
    },
    {
        'c': 'the',
        'd': 'merged'
    },
    {
        'd': 'dictionary'
    }
]

# print(concatenate_dictionaries(lst))
"""
Prints: 
{
    'a': 'this',
    'b': 'is',
    'c': 'the',
    'd': 'dictionary'
}
"""

## Write your code here.
def merge_lists(list_1, list_2):
    # merged_dict = {}
    # for index, value in enumerate(list_1):
    #     merged_dict[value] = list_2[index]

    # return merged_dict
    return dict(zip(list_1, list_2))


lst1 = ['a', 'b']
lst2 = [1, 2]
merged_dict = merge_lists(lst1, lst2)
# print(merged_dict)      # { 'a': 1, 'b': 2 }


# SETS
# new_set = set()
# another_set = {1, 2, 2, 3, 3}
# print(another_set)

# listy_1 = [1, 2, 2, 3, 4, 4, 4, 4, 5, 6, 7]
# print(list(set(listy_1)))

# string = "hello"
# print(set(string))

# my_set = {1, 2, 3, 4}
# print(1 in my_set)
# # print(my_set[1])
# print(my_set.add(5))
# print(my_set)
# print(my_set.update((7, 8)))
# print(my_set)
# print(my_set.remove(7))
# print(my_set)

set_1 = {0, 1, 2, 3}
set_2 = {0, 1, 5, 6}

# UNION
# print(set_1 | set_2) 
# print(set_1.union(set_2))

# INTERSECTION
# print(set_1 & set_2)
# print(set_1.intersection(set_2))

# DIFFERENCE
# print(set_1 - set_2)
# print(set_2 - set_1)
# print(set_1.difference(set_2))

# SYMMETRIC DIFFERENCE
# print(set_1 ^ set_2)
# print(set_1.symmetric_difference(set_2))

# BUILT IN FUNCTIONS
# def name_to_upper(name):
#     return name.lower()

# names = {"JAMES", "julie", "Ana", "Ria"}
# sorted_names = sorted(names, key=name_to_upper, reverse=True ) # lambda name: name.lower()
# print(set(sorted_names))

# ALL ANY
test = ['', True, 0]
test_2 = []

# ALL is happy (TRUE) if nothing inside is falsey
# print(all(test))
# print(all(test_2))

# ANY is happy (TRUE) if at least one thing is truthy
# print(any(test))
# print(any(test_2))


# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# only_as = filter(lambda grade: grade >= 90, scores)
# list_as = list(only_as)
# set_as = set(only_as)
# print(list_as)
# # print(set(list_as))
# print(set_as)

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
scores = {90, 86, 75, 91, 62, 99, 88, 90, 89, 78, 90}
grades = {"A", "B", "C", "A", "D", "A", "B", "A"}
combined = zip(scores, grades)
# new_dict= dict(combined)
# print(new_dict)
# print(list(combined))


# REMOVE DUPLICATES
# def get_unique_models(phone_list):
#     seen = []
#     return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)
    
#     # so what is going on here in the filter method???
#     # think of the lambda statement being written like this...
#     if phone['model'] not in seen:
#         return seen.append(phone['model']) is None
#     else:
#         return False
    #
    # Because this is a callback in a filter, it needs to return True or False
    # to determine if the value gets added to our filtered list
    #
    # In the else, we return False, makes sense...
    # The append method does not have a return, but we know that if a
    # function does not have a set return value, it returns None!
    # So we check if the return value is None, which will evaluate to true!


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

# def get_unique_models(list_of_phones):
#     just_models = map(lambda phone: phone["model"], list_of_phones)
#     print(list(set(just_models)))

# get_unique_models(phones)

# COMPREHENSIONs

my_list = [1, "2", 'Three', True, None]
my_list_copy = [val for val in my_list]
my_list_copy_2 = [*my_list]

# print(my_list_copy)
# print(my_list_copy_2)

nums = [-5, 11, 10, 14]
# mapped_nums = map(lambda num: num * 2, nums)
# print(list(mapped_nums))
mapped_nums = [num * 2 for num in nums]
# print(mapped_nums)
# print(mapped_nums)
# print([num * 2 for num in nums])
filter_nums = [num for num in nums if num > 0]
# print(filter_nums)
# mapped_and_filtered_nums = [num * 10 for num in nums if num > 0]
# print(mapped_and_filtered_nums)

# new_list = []
# for num in nums:
#     if num > 0:
#         new_list.append(num * 10)

# print(new_list)

# DICTIONARY
num_dict = { num: num**2 for num in range(5)}
# print(num_dict)

breaks = {
    "lunch": 2,
    "afternoon": 6,
    "EOD": 7
}

daylight_saving = {key: value + 1 for key, value in breaks.items()}
print(daylight_saving)

# alternate_daylight = {key: breaks[key] += 1 for key in breaks.keys }
alternate_comp = [ breaks[key] + 1 for key in breaks.keys() ]
print(alternate_comp)
print(breaks)

names = ["brad", "drew", "david", "andrew", "keegan"]
upper_names = [name.upper() for name in names]
print(upper_names)