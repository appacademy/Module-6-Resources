# # # TUPLES

# # tup = ('red', 'blue')
# # tup += "green", "orange"

# # print(tup)

# # # EMPTY TUPLE
# # tup_2 = ()

# # # SINGLETON TUPLE
# # tup_3 = 1,
# # tup_4 = (2,)

# DAYS = ("Mon", "Tue", "Wed", "Thurs", "Fri")

# def sum_and_average(lst):
#     list_sum = sum(lst)
#     average = list_sum / len(lst)
#     return (list_sum, average)


# list_sum, list_average = sum_and_average([1, 2, 3, 4])
# print(list_sum, list_average)

# print(DAYS[1:3])

# for day in DAYS:
#     print(day)


# sorted_days = sorted(DAYS)
# print(tuple(sorted_days))


# def function(num_1, num_2, num_3 = 15, *args):
#     print(num_1, num_2, num_3)
#     print(args)


# function(5, 10, 20, 25, 30)

# INDEX SORT

# Write your function, here.

# def compare(val):
#     return val[1]

# def index_sort(lst):
#     sorted_tuples = sorted(lst, key=compare) # lambda val: val[1]
#     return sorted_tuples

# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]


# RANGES & ENUMERATE
# values = range(start,stop,step)
# values = range(10, 0, -1)
# print(values)
# print(tuple(values))


lunch = ['wings', 'pizza', 'sandwich', 'soup', 'salad']

# for i in range(len(lunch)):
#     print(f"{i}. {lunch[i]}")

# ENUMERATE

# print(enumerate(lunch))
# print(list(enumerate(lunch)))


# for index, value in enumerate(lunch, 1):
#     print(f"{index}. {value}")


# RANGE FACTORIAL
# Write your function, here.
# def factorial(n):
#     total = 1
#     for i in range(1, n + 1):
#         total *= i
#     return total

# def recur_factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * recur_factorial(n - 1)


# print(recur_factorial(1))     #> 1
# print(recur_factorial(8))     #> 40320
# print(recur_factorial(12))    #> 479001600


# CAN NEST
# list1's min is greater than list2's min
# list1's max is less than list2's max

# def can_nest(list_1, list_2):
#     list1_min = min(list_1)
#     list1_max = max(list_1)
#     list2_min = min(list_2)
#     list2_max = max(list_2)
#     return list1_min > list2_min and list1_max < list2_max


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
    4: "neals",
    "second breakfast": "apple",
}

# print(meals)
# print(meals["dinner"])
# print(meals["brinner"])
# print(meals.get("brinner", "Key not in dictionary"))

# if meals.get("brinner") is None:
#     meals["brinner"] = "pancakes"
# else:
#     print("Key already exists")

# print(meals)
# del meals["second breakfast"]
# print(meals)

# meals.update({"elevensies": "biscuit", "supper": "roast"})
# print(meals)

# print("lunch" in meals)
# print(5 in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for k, v in meals.items():
#     print(f"{k}, {v}")

# for val in meals.values():
#     print(val)


# ARGS / KWARGS

# def sum(num_1, num_2, num_3 = 15, *args, **kwargs):
#     total = num_1 + num_2 + num_3
#     print("args", args)
#     for val in args:
#         total += val
#     print("kwargs", kwargs)
#     for more_vals in kwargs.values():
#         total += more_vals
#     return total

# print(sum(10, 20, 30, 40 , 50, num_6=60, num_7=70))

# lst_1 = ['a', 'b', 'c']
# lst_2 = [1, 2, 3]
# lst_3 = [*lst_1, *lst_2]
# print(lst_3)

# dict_1 = {
#     "breakfast": "eggs",
#     "lunch": "wings",
#     "dinner": "pizza"
# }

# dict_2 = {**dict_1}
# print(dict_2)



# MERGE 2 Lists
# Write your code here.
# def merge_lists(list_1, list_2):
#     return_dict = {}
#     for index, value in enumerate(list_1):
#         return_dict[value] = list_2[index]

#     return return_dict


# def merge_lists_2(list_1, list_2):
#     merged_list = []
#     for index in range(len(list_1)):
#         merged_tuple = (list_1[index], list_2[index])
#         merged_list.append(merged_tuple)

#     return dict(merged_list)



# lst1 = ['a', 'b']
# lst2 = [1, 2]
# merged_dict = merge_lists_2(lst1, lst2)
# print(merged_dict)      # { 'a': 1, 'b': 2 }


# SETS
# EMPTY SETS
# new_set = set()

# other_set = {"pizza", "wings", "burrito"}

# print(new_set, other_set)

# values = [1, 1, 2, 2, 3, 4, 4, 5, 7]
# print(set(values))

# string = "hello"
# print(set(string))

# my_set = {1, 2, 3, 4}
# print(1 in my_set)

# # print(my_set[2])

# my_set.add(5)
# print(my_set)
# my_set.update({6, 7})
# print(my_set)
# my_set.remove(5)
# print(my_set)

# for val in my_set:
#     print(val)


a = {0, 1, 2, 3, 4}
b = {3, 4, 5, 6, 7}

# UNION
# print( a | b )
# print(a.union(b))


# INTERSECTION
# print( a & b )
# print(a.intersection(b))


# DIFFERENCE
# print( a - b )
# print( b - a )
# print(a.difference(b))

# SYMMETRIC DIFFERENCE
# print( a ^ b )
# print( a.symmetric_difference(b))


# BUILT IN FUNCTIONS


# SORTED
# names = ("JAMES", "julie", "Ana", "Ria")
# #  ['james', "julie", 'ana", "ria"]
# sorted_names = sorted(names, key=lambda name: name.lower(), reverse=True)
# print(set(sorted_names))

# ALL & ANY
# test = ["", "pizza", 2, 0]
# test_2 = {}
# print(all(test))
# print(all(test_2))

# test = ["", "pizza", 2, 0]
# test_2 = {}
# print(any(test))
# print(any(test_2))

# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# only_as = filter(lambda num: num >= 90, scores)
# print(only_as)
# list_scores = list(only_as)
# print(list_scores)
# print(tuple(list_scores))


# MAP
# def get_grade(num):
#     if (num >= 90):
#         return "A"
#     elif (num <90 and num >= 80):
#         return "B"
#     elif (num < 80 and num >= 70):
#         return "C"
#     elif (num < 70 and num >= 60):
#         return "D"
#     else:
#         return "F"


# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# mapped_grades = map(get_grade, scores)
# print(mapped_grades)
# print(list(mapped_grades))

# ZIP
# scores = [90, 86, 75, 91, 62, 99, 88, 90, 40, 40]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
# combined = zip(scores, grades)
# print(combined)
# tuple_list = list(combined)
# combined_dict = dict(tuple_list)
# print(combined_dict)


# REMOVE DUPLICATES

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

# def get_unique_models(phone_list):
#     just_models = map(lambda phone: phone["model"], phone_list)
#     print(list(set(just_models)))


# get_unique_models(phones)

# def get_unique_models(phone_list):
#     seen = []
#     return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)
    
#     # so what is going on here in the filter method???
#     # think of the lambda statement being written like this...
#     if phone['model'] not in seen:
#         return seen.append(phone['model']) is None
#     else:
#         return False
    
    # Because this is a callback in a filter, it needs to return True or False
    # to determine if the value gets added to our filtered list
    
    # In the else, we return False, makes sense...
    # The append method does not have a return, but we know that if a
    # function does not have a set return value, it returns None!
    # So we check if the return value is None, which will evaluate to true!

   

# def map_to_names(phone_list):
#     return list(map(lambda phone: phone['model'], phone_list))


# COMPREHENSIONS
# my_list = [2, 4, 6, 8, 10]
# my_list_copy = [num for num in my_list]
# print(my_list_copy)
# another_copy = [*my_list]
# print(another_copy)

nums = [-5, -2, 5, 13, 27, 3_000_000]
# mapped_num = map(lambda num: num * 2, nums)
# print(list(mapped_num))
# mapped_nums = [num * 2 for num in nums]
# print(mapped_nums)
# filtered_nums = [num for num in nums if num > 0]
# print(filtered_nums)
# mappped_and_filtered_num = [num * 2 for num in nums if num > 0]
# print(mappped_and_filtered_num)


# DICTIONARY COMPREHENSIONS
# number_dictionary = {num: num**2 for num in range(6)}
# print(number_dictionary)

breaks = {
    "lunch": 2,
    "afternoon": 6,
    "EOD": 7,
}

print(breaks)
daylight_savings = {k: v + 1 for k, v in breaks.items()}
print(daylight_savings)