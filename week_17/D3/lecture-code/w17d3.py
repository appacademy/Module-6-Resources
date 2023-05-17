# TUPLE

# tup = ("red", "blue")
# tup += ("green", "orange")
# print(tup)
# print(tup[1:3])

# tup2 = 'Brad', "David", "Andrew", "Keegan"
# print(tup2)

# # EMPTY TUPLE
# tup3 = ()
# print(tup3)

# SINGLE VALUE TUPLE
tup4 = (1,)
tup5 = 2, 


def sum_and_average(lst):
    list_sum = sum(lst)
    average = list_sum / len(lst)
    return (list_sum, average)

# return_average, return_sum = sum_and_average([1, 2, 3, 4])
# print(return_average, return_sum)

DAYS = ("Mon", "Tue", "Wed", "Thurs", "Fri")

sorted_days = sorted(DAYS)
# print(tuple(sorted_days))


def function(num1, num2, num3=15, *args):
    total = sum((num1, num2, num3, *args))
    print(args)
    # for arg in args:
    #     total += arg
    print(total)


# function(5, 10, 20, 25, 30)


# INDEX SORT
def compare(val):
    return val[1]


def index_sort(tuple_list):
    sorted_list = sorted(tuple_list, key=compare, reverse=True)  #lambda val: val[1]
    return sorted_list

    tuple_list.sort()

# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]



# RANGES

# values = range(10, 0, -1)
# print(list(values))

lunch = ["wings", "sandwich", "pizza", "chicken parm"]

# for index in range(len(lunch)):
#     print(index, lunch[index])

# for index in lunch:
#     print(index)

# ENUMERATE
# print(tuple(enumerate(lunch)))

# print("Today's lunch menu: ")
# for index, food in enumerate(lunch, 1):
#     print(f"{index}. {food}")


# FACTORIAL
def factorial(n):
    total = 1
    for number in range(1, n + 1):
        total *= number
    return total


# print(factorial(1))     #> 1
# print(factorial(8))     #> 40320
# print(factorial(12))    #> 479001600






# Problem 4 - Check Nested Arrays
# Your code, here.

# def can_nest(list1, list2):
#     list1_min = min(list1)
#     list1_max = max(list1)
#     list2_min = min(list2)
#     list2_max = max(list2)
#     return list1_min > list2_min and list1_max < list2_max


can_nest = lambda list1, list2: min(list1) > min(list2) and max(list1) < max(list2)

# print(can_nest([1, 2, 3, 4], [0, 6]))  #> True
# print(can_nest([3, 1], [4, 0]))        #> True
# print(can_nest([9, 9, 8], [8, 9]))     #> False
# print(can_nest([1, 2, 3, 4], [2, 3]))  #> False


# DICTIONARIES

meals = {
    "breakfast": "coffee",
    "lunch": "wings",
    "dinner": "pizza",
    "dessert": "ice cream",
    4: "meals",
    True: "even more meals",
    "second breakfast": "apple",
}


# print(meals)
# print(meals["lunch"])
# # print(meals["brinner"]) # -> will throw a keyerror


# print(meals.get("lunch"))
# print(meals.get("brinner", "Nope.  Sorry buddy no key for you!"))


# if meals.get("second breakfast") is None:
#     meals["second breakfast"] = "pear"
# else:
#     print("Key already exists")

# print(meals)

# meals["dinner"] = "steak"
# meals.update({"supper": "roast", "elevensies": "donut"})
# print(meals)
# del meals[4]
# print(meals)

# print("second breakfast" in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key in meals.keys():
#     print(key)

# for value in meals.values():
#     print(value)

# for key, value in meals.items():
#     print(key, value)



def sum_stuff(num1, num2, num3=15, *args, **kwargs):
    total = sum((num1, num2, num3, *args))
    print(args)
    # for arg in args:
    #     total += arg
    # inner(*args, **kwargs)
    print(kwargs)
    for val in kwargs.values():
        total += val
    print(total)


# sum_stuff(5, 10, 20, 25, 30, num6=35, num7=40)


lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3 ]
lst3 = [*lst1, *lst2]

# print(lst3)

# dict1 = {
#     "breakfast": "coffee",
#     "lunch": "wings",
#     "dinner": "pizza",
# }

# dict2 = {**dict1}
# print(dict2)

# for key in *{dict1}:
#     print(key)


# Merged 2 Lists
# def merge_lists(lst1, lst2):
#     merged_list = []
#     for index in range(len(lst1)):
#         merge_tuple = (lst1[index], lst2[index])
#         merged_list.append(merge_tuple)
#     print(merged_list)
#     return dict(merged_list)



# def merge_lists2(lst1, lst2):
#     return_dict = {}
#     for index, value in enumerate(lst1):
#         return_dict[value] = lst2[index]
#     return return_dict
  

# def merge_lists_OG(lst1, lst2):
#     merged_dict = {}
#     ind = 0
#     while ind < len(lst1):
#         merged_dict[lst1[ind]] = lst2[ind]
#         ind += 1
#     return merged_dict

# lst1 = ['a', 'b']
# lst2 = [1, 2]
# merged_dict = merge_lists(lst1, lst2)
# print(merged_dict)      # { 'a': 1, 'b': 2 }


# SETS
not_a_set = {}
set1 = set()
set2 = {1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5}
# print(set2)

# list1 = [1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 6, 8, 8, 8, 9]
# print(set(list1))

# string = "hello"
# print(set(string))

my_set = {1, 2, 3, 4}
# print(1 in my_set)

# for val in my_set:
#     print(val)

# my_set.add(5)
# print(my_set)
# my_set.update({5, 6, 7})
# print(my_set)
# my_set.remove(3)
# print(my_set)


set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}

# UNION 
# print( set_1 | set_2)
# print( set_1.union(set_2))


# INTERSECTION
# print( set_1 & set_2 )
# print( set_1.intersection(set_2))


# # DIFFERENCE
# print( set_1 - set_2)
# print( set_2 - set_1)
# print( set_1.difference(set_2))


# # SYMETTRIC DIFFERENCE
# print( set_1 ^ set_2 )
# print( set_1.symmetric_difference(set_2))


# BUILT IN FUNCTION
# SORTED
names = ("JAMES", "julie", "Ana", "Ria")
nums = [1, 4,  2, 7]
# names.sort(key=lambda x: x.lower())
# print(names)
sorted_names = sorted(names, key=lambda x: x.lower(), reverse=True)
# print(sorted_names)

# ALL & ANY
test1 = ['2', False, 0]
test2 = {}
test3  = [True, "Hello", 243]
# print(all(test1))
# print(all(test2))
# print(all(test3))
# ALL is "happy" if nothing inside is False
# print(any(test1))
# print(any(test2))
# print(any(test3))
# ANY is "happy" if a least 1 thing is True

# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# only_as = filter(lambda score: score >= 90 , scores)
# list_as = list(only_as)
# set_as = set(list_as)

# print(list_as)
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
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
# combined = zip(grades, scores)
# combined_list = list(combined)
# combined_dict = dict(combined_list)
# print(combined_dict)

# num = 1_000_000_000
# print(num)


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
#     just_models = map(lambda phone: phone["model"], phone_list)
#     return list(set(just_models))


# print(get_unique_models(phones))

# def get_unique_models(phone_list):
#     seen = []
#     return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)
    
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


# COMPREHENSIONS

# my_list = [1, "2", True, "Wednesday"]
# my_list_copy = [item for item in my_list]
# my_list_copy2 = [*my_list]
# print(my_list_copy)
# print(my_list_copy2)


# nums = [-10, -5, 2, 6, 8, 10]
# mapped_nums = [num * 2 for num in nums]
# print(mapped_nums)
# filter_nums = [num for num in nums if num > 0]
# print(filter_nums)
# mapped_and_filtered_num = [num*2 for num in nums if num > 0]
# print(mapped_and_filtered_num)

# DICTIONARY COMPREHENSIONS

numbers_dict = { num: num**2 for num in range(6)}
print(numbers_dict)

breaks = {
    "lunch": 2,
    "afternoon": 6,
    "EOD": 7,
}

breaks_CST = {k: v - 1 for k, v in breaks.items()}
print(breaks_CST)