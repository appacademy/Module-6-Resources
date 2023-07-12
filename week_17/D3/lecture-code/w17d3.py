# TUPLES

# tup = ('red', "blue")
# tup += "green", "orange"
# print(tup)

# print(tup[1:3])

# # EMPTY TUPLE
# tup_2 = ()
# tup_2_5 = tuple()
# # SINGLETON TUPLES
# tup_3 = ("purple",)
# tup_4 = "pink",


# def sum_and_average(lst):
#     list_sum = sum(lst)
#     list_avg = list_sum / len(lst)
#     return (list_sum, list_avg)


# ret_sum, ret_avg = sum_and_average([1, 2, 3, 4, 5])
# print(ret_sum, ret_avg)

DAYS = ("Mon", 'tue', "Wed", "thurs", "Fri")

# colors = ("Red", "Green", "Orange")

# red, green, _ = colors

# sorted_days = sorted(DAYS, key=lambda val: val.upper())
# print(sorted_days)

# Index Sort
# def compare(val):
#     return val[1]


def index_sort(tup_list):
    sorted_list = sorted(tup_list, key=compare, reverse=True )  # lambda tup: tup[1]
    return sorted_list



# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]


# RANGES

# test_range = range(8,0,-1)
# print(test_range)
# print(set(test_range))

lunch = ["wings", "sandwich", "hot dog", "waffle"]

# for index in range(len(lunch)):
#     print(lunch[index])

# ENUMERATE

# print(list(enumerate(lunch)))

# for index, value in enumerate(lunch, 1):
#     print(f"{index}. {value}")


# Factorial Range
# def factorial(num):
#     total = 1
#     for value in range(1, num + 1):
#         total *= value
#     return total

# print(factorial(1))     #> 1
# print(factorial(8))     #> 40320
# print(factorial(12))    #> 479001600

# def recursive_factorial(num):
#     if num == 1:
#         return num
#     else:
#         return num * recursive_factorial(num - 1)

# print(recursive_factorial(1))     #> 1
# print(recursive_factorial(8))     #> 40320
# print(recursive_factorial(12))    #> 479001600

# DICTIONARIES
# meals = {
#     "breakfast": "coffee",
#     "lunch": "wings",
#     "dinner": "pizza",
#     "dessert": "ice cream",
#     4: "meals",
#     "second breakfast": "apple"
# }
# print(meals)

# print(meals["dinner"])
# # print(meals["brinner"])
# print(meals.get("brinner", "Key not found"))

# meals["brinner"] = "pancakes"

# WAYS TO CHECK IF KEY IS ALREADY THERE
# if meals.get("brinner") is None:
#     meals["brinner"] = "pancakes"
# else:
#     Print("Key already exists")

# if "brinner" not in meals:
#      meals["brinner"] = "pancakes"

# print(meals)

meals = {
    "breakfast": "coffee",
    "lunch": "wings",
    "dinner": "pizza",
    "dessert": "ice cream",
    4: "meals",
    "second breakfast": "apple"
}

# meals["dessert"] = "pie"
# print(meals)
# del meals[4]
# print(meals)
# meals.update({"supper": "turkey leg", "elevensies": "cookie"})
# print(meals)


# print("dinner" in meals)
# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key in meals.keys():
#     print(key)

# for val in meals.values():
#     print(val)

# for key, val in meals.items():
#     print(key, val)


# ARGS/KWARGS
# def sum(num_1, num_2, num_3=15, *args, **kwargs):
#     print(num_1, num_2, num_3)
#     total = num_1 + num_2 + num_2 
#     print(args)
#     for arg in args:
#         total += arg
#     print(kwargs)
#     for kwarg in kwargs.values():
#         total += kwarg
#     return total

# total_vals = sum(5, 10, 20, 25, 30, 40, num_7=45, num_8=50)
# print(total_vals)

# lst_1 = ['a', 'b', 'c', 'd']
# lst_2 = [1, 2, 3, 45 ]
# lst_3 = [*lst_1, *lst_2]
# print(lst_3)

# dict1 = {
#     "breakfast": "eggs",
#     "lunch": "wings",
#     "dinner": "pasta"
# }

# dict2 = {**dict1}
# print(dict2)

# print(dict1 == dict2)


# def merge_lists(list_1, list_2):
#     return_dict = {}
#     for index, value in enumerate(list_1):
#         return_dict[value] = list_2[index]

#     return return_dict

# def merge_lists2(list_1, list_2):
#     merged_list = []
#     for index in range(len(list_1)):
#         merge_tuple = (list_1[index], list_2[index])
#         print(merge_tuple)
#         merged_list.append(merge_tuple)
    
#     print(merged_list)
#     return dict(merged_list)

# def merge_lists3(list_1, list_2):
#     return dict(zip(list_1, list_2))



# lst1 = ['a', 'b']
# lst2 = [1, 2]
# merged_dict = merge_lists3(lst1, lst2)
# print(merged_dict)      # { 'a': 1, 'b': 2 }


# SETS
# new_set = set()
another_set = {1, 1, 2, 2, 3, 4, 5, 5}
# print(another_set)
# yet_another_set = {1}

# another_list = [1, 1, 1, 2, 2, 2, "a", 'a', 'b']
# print(set(another_list))
# string = "hello"
# print(set(string))

# print(another_set[1])
# another_set.add(6)
# print(another_set)
# another_set.update([7,8])
# print(another_set)
# another_set.remove(4)
# print(another_set)
# print(5 in another_set)

# for val in another_set:
#     print(val)

a = {0, 1, 2, 3}
b = {0, 1, 5, 6}

#UNION
# print(a | b)
# print(a.union(b))

# INTERSECTION
# print(a & b)
# print(a.intersection(b))

# DIFFERENCE
# print(a - b)
# print(a.difference(b))
# print(b - a)

# SYMMETRIC DIFFEREMCE
# print(a ^ b)
# print(a.symmetric_difference(b))
# def check_binary(string):
#     binary_set = set(string)
#     # return binary_set == {"1", "0"} or binary_set == {"1"} or binary_set == {"0"}
#     # return binary_set.issubset({"0", '1'})
#     list_of_sets = [{"0"}, {"1"}, {"0", "1"}]
#     return binary_set in list_of_sets


# str1 = '1010001010010100101'
# str2 = '1010010015010101010'

# print(check_binary(str1))       # True
# print(check_binary(str2))       # False

# BUILT INS
# names = ("JAMES", "julie", "Ana", "Ria")
# # names = ("james", "julie", "ana", "ria")
# def compare(val):
#     return val.lower()

# sorted_names = sorted(names, key=compare, reverse=True) # lambda val: val.lower()
# print(tuple(sorted_names))

# ALL/ANY
# test = ["", False, 5 ]
# test_1 = []
# print('all', all(test))
# print('all', all(test_1))
# # all is happy (True) if nothing inside is false
# print('any', any(test))
# print('any', any(test_1))
# any is happhy (True) if a least 1 items is truty


# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# only_as = filter(lambda grade: grade >= 90, scores)
# print(only_as) 
# only_as_list = list(only_as)
# print(set(only_as_list)) 

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

# mapped_grades = map(get_grade, scores)
# print(mapped_grades)
# print(list(mapped_grades))

# ZIP
# scores = [90, 86, 75, 91, 62, 99, 88, 90, 45, 45, 45]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]

# combined = zip(grades, scores)
# print(combined)
# combined_list = list(combined)
# print(dict(combined_list))

# REMOVE DUPLICATES
# def get_unique_models(phone_list):
#     seen = []
    # return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)
    
#     # so what is going on here in the filter method???
#     # think of the lambda statement being written like this...
#     if phone['model'] not in seen:
#         # reminder append has no defined return so it returns None
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

# def get_unique_models(phone_list):
#     just_models = map(lambda phone: phone["model"], phone_list)
#     return list(set(just_models))

# print(get_unique_models(phones))

# LIST COMPREHENSIONS
# my_list = [1, '2', "THREE", True, None]
# my_list_copy = [ value for value in my_list ]

# for item in my_list:
#     my_list_copy.append(item)

# print(my_list_copy)
# my_list_splat = [*my_list]
# print(my_list_splat)

# nums = [-5, 11, 10, 14]
# mapped_nums = [value * 2 for value in nums]
# print(mapped_nums)
# filtered_nums = [value for value in nums if value > 0]
# print(filtered_nums)
# map_and_filter_nums = [value * 2 for value in nums if value > 0]
# print(map_and_filter_nums)

# users = [ user.to_dict() for user in User.query.all()]

number_dict = { num: num ** 2 for num in range(6)}
print(number_dict)

breaks = {
    "lunch": 2,
    "afternoon": 6,
    "EOD": 7
}

daylight_savings = {key: value - 1 for key, value in breaks.items()}
print(daylight_savings)