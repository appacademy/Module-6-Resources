# TUPLES

# soup_tup = ("French Onion", "Chicken Noodle")
# soup_tup += "Tom Yum Goong", "New England Clam Chowder"

# print(soup_tup)

# # EMPTY TUPLE
# tup1 = ()
# tup2 = tuple()

# # SINGLETON TUPLE 
# tup3 = 1, 
# tup4 = (1,)

# print(soup_tup[1:3])
# print(soup_tup[::-1])

# for soup in soup_tup:
#     print(soup)

# DAYS = ("Mon", "Tue", "Wed", "Thur", "Fri")

# sorted_days = sorted(DAYS)
# print(tuple(sorted_days))


# def sum_and_average(lst):
#     list_sum = sum(lst)
#     list_avg = list_sum / len(lst)
#     list_other = "its another something"
#     return list_sum, list_avg, list_other

# calc_sum, calc_avg, _ = sum_and_average([1,2,3,4,5])
# print(calc_sum, calc_avg)


# def summer(num1, num2, num3=30, *args):
#     """function that sums all possible arguements provided to it"""
#     total = sum([num1, num2, num3 ])
#     print(args)
#     for arg in args:
#         total += arg
#     return total

# print(summer(10, 20, 40, 50, 60))

# def compare(val):
#     return val[1]


# def index_sort(tuple_list):
#     sorted_list = sorted(tuple_list, key=compare, reverse=True)  # lambda val: val[1]
#     return sorted_list


# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]

# RANGES & ENUMERATE
# some_range = range(10, -1, -1)
# print(list(some_range))
# print(tuple(some_range))

# for index in range(10):
#     print(index)


# soup_tup = ("French Onion", "Chicken Noodle")
# soup_tup += "Tom Yum Goong", "New England Clam Chowder"

# # for index in range(len(soup_tup)):
# #     print(f"{index}. {soup_tup[index]}")

# print(list(enumerate(soup_tup)))

# for index, value in enumerate(soup_tup, 1):
#     print(f"{index}. {value}")

# Problem 3 - Factorial
# Write your function, here.
# def factorial(num):
#     total = 1
#     for index in range(1, num + 1):
#         total *= index
#     return total

# def recur_factorial(num):
#     if num == 1:
#         return num
#     else:
#         return num * recur_factorial(num - 1)


# print(recur_factorial(1))     #> 1
# print(recur_factorial(8))     #> 40320
# print(recur_factorial(12))    #> 479001600



# def can_nest(list1, list2):
#     list1_min = min(list1)
#     list1_max = max(list1)
#     list2_min = min(list2)
#     list2_max = max(list2)
#     return list1_min > list2_min and list1_max < list2_max


# print(can_nest([1, 2, 3, 4], [0, 6]))  #> True
# print(can_nest([3, 1], [4, 0]))        #> True
# print(can_nest([9, 9, 8], [8, 9]))     #> False
# print(can_nest([1, 2, 3, 4], [2, 3]))  #> False


# DICTIONARIES

# meals = {
#     "breakfast": "eggs",
#     "elevensies": "bagel",
#     "lunch": "sandwich",
#     "dinner": "french onion soup",
#     4: "meals",
#     True: "even more meals",
#     "second breakfast": "apple"
# }

# another_dict = {1: "one", 2: "two", 3:"three"}
# print(meals)

# print(meals[4])
# print(meals["lunch"])

# print(meals.get("lunch"))
# print(meals.get("second breakfast", "no key for you!"))

# if meals.get("second breakfast") is None:
#     meals["second breakfast"] = "apple"
# else:
#     print("Key already exsists in dictionary")

# if "second breakfast" in meals:
#     meals["second breakfast"] = "apple"
# else:
#     print("Key already exsists in dictionary")

# print(meals)

meals = {
    "breakfast": "eggs",
    "elevensies": "bagel",
    "lunch": "sandwich",
    "dinner": "french onion soup",
    4: "meals",
    True: "even more meals",
    "second breakfast": "apple"
}

# meals["supper"] = "roast beast"
# print(meals)
# meals["second breakfast"] = "banana" 
# print(meals)
# del meals[True]
# print(meals)
# meals.update({"afternoon tea": "earl gray", "dessert": "apple pie"})
# print(meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for value in meals.values():
#     print(value)


# for key, value in meals.items():
#     print(key, value)    

# def summer(num1, num2, num3=30, *args, **kwargs):
#     """function that sums all possible arguements provided to it"""
#     total = sum([num1, num2, num3 ])
#     print(args)
#     for arg in args:
#         total += arg
#     print(kwargs)
#     for kwarg in kwargs.values():
#         total += kwarg
#     return total

# print(summer(10, 20, 40, 50, 60, num6=70, num7=80))

# lst1 = ['a', 'b', 'c']
# lst2 = [1, 2, 3]
# lst3 = [*lst1, *lst2]
# print(lst3)

# dict1 = {
#     "breakfast": "eggs",
#     "lunch": "turkey sandwich",
#     "dinner": "french onion soup",
# }

# dict2 = {**dict1}
# print(dict2)


# def merge_lists(lst1, lst2):
#     merged_list = []
#     for index in range(len(lst1)):
#         merged_tuple = (lst1[index], lst2[index])
#         print(merged_tuple)
#         merged_list.append(merged_tuple)

#     print(merged_list)
#     return dict(merged_list)


# def merge_lists2(lst1, lst2):
#     return_dict = {}

#     for index, value in enumerate(lst1):
#         return_dict[value] = lst2[index]
    
#     return return_dict

# def merge_lists3(lst1, lst2):
#     dict_maker = zip(lst1, lst2)
#     print(list(dict_maker))
#     return dict(dict_maker)
  

# lst1 = ('a', 'b', 'c')
# lst2 = (1, 2, 3)
# merged_dict = merge_lists3(lst1, lst2)
# print(merged_dict)      # { 'a': 1, 'b': 2 }


# SETS
# empty_set = set()

# not_empty_set = {1, 1, 1, 2, 2, 2, 3, 4, 5}
# print(not_empty_set)

# vals = [ 1, 1, 1, 2, 2, 2, 3, 4, 5 ]

# print(list(set(vals)))

# print(set("hello!"))


# for val in not_empty_set:
#     print(val)

# print(2 in not_empty_set)

# print(not_empty_set[2])

# my_set = {1, 2, 3, 4}
# my_set.add("a")
# print(my_set)
# my_set.update([4, 5, 6])
# print(my_set)
# my_set.remove("a")
# print(my_set)
# print(len(my_set))

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# # UNION
# print(a | b)
# print(a.union(b))
# # INTERSECTION
# print(a & b)
# print(a.intersection(b))
# # DIFFERENCE
# print(a - b)
# print(a.difference(b))
# print(b - a) 
# SYMETTRIC DIFFERENCE
# print(a ^ b)
# print(a.symmetric_difference(b))





# def check_binary(string):
#     str_set = set(string)
#     # return str_set == ({"0", "1"} or {"0"} or {"1"})
#     # return str_set.issubset({"0", "1"})
#     # list_of_sets = [{'0', '1'}, {"0"}, {'1'}]
#     # return str_set in list_of_sets
#     binary_set = {"1", "0"}
#     return not str_set ^ binary_set


# str1 = '1010001010010100101'
# str2 = '1010010015010101010'

# print(check_binary(str1))       # True
# print(check_binary(str2))   


# BUILT IN FUNCTIONS

# SORTED
# names = ["JAMES", "julie", "Ana", "Ria"]
# sorted_names = sorted(names, key=lambda name: name.upper())
# print(sorted_names)

# ALL / ANY

# test = ['', False, "8"]
# test2 = [1, 2, 3]
# test3 = {}
# # print(all(test))
# # print(all(test2))
# # print(all(test3))
# # ALL IS 'HAPPY' IF NOTHING INSIDE IS FALSE
# print(any(test))
# print(any(test2))
# print(any(test3))
# ANY IS HAPPY IF AT LEAST 1 THING IS TRUTHY

# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# only_as = filter(lambda score: score >= 90, scores)
# only_as_tupl = tuple(only_as)
# print(list(only_as_tupl))


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
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]

# combined = zip(grades, scores)
# print(combined)
# combined_list = list(combined)
# print(combined_list)
# combined_dict = dict(combined_list)
# print(combined_dict)

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
#     #
#     # Because this is a callback in a filter, it needs to return True or False
#     # to determine if the value gets added to our filtered list
#     #
#     # In the else, we return False, makes sense...
#     # The append method does not have a return, but we know that if a
#     # function does not have a set return value, it returns None!
#     # So we check if the return value is None, which will evaluate to true!

# LIST COMPREHENSIONS

# my_list = [1, "2", "Five", True, None]
# my_list_copy = [item for item in my_list]
# print(my_list_copy)
# my_list_copy2 = [*my_list]
# print(my_list_copy2)

# nums = [-4, 1, 4, 67, 256]
# mapped_nums = [num * 2 for num in nums]
# print(mapped_nums)
# filtered_nums = [num for num in nums if num > 3]
# print(filtered_nums)

# mapped_and_filtered_nums = [num * 2 for num in nums if num > 0]
# print(mapped_and_filtered_nums)
# foods = ["wings", "pizza", "soup"]
# upper_foods = [len(food) for food in foods]
# print(upper_foods)

# DICTIONARY COMPREHENSION
# number_dictionary = { num: num**2 for num in range(5) }
# print(number_dictionary)

# breaks = {
#     'lunch': 2,
#     'afternoon': 6,
#     'EOD': 7
# }

# daylights_savings = { key: value + 1 for key, value in breaks.items() }
# print(daylights_savings)
