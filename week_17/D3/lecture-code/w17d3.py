# TUPLES

# tup = ('red', 'blue')
# tup += ('green', "orange")

# print(tup)

# tup_2 = "Brad", "David", "Andrew"

# print(tup_2)

# tup_3 = 1,
# tup_4 = 2, 
# tup_5 = 3,

# # EMPTY TUPLES
# empty_tuple = ()
# empty_tuple2 = tuple()

# # SINGLETON TUPLE
# tup_6 = (1,)
# tup_7 = 2,


# def sum_and_average(lst):
#     list_sum = sum(lst)
#     average = list_sum / len(lst)
#     return (list_sum, average)


# ran_sum, ran_avg = sum_and_average([1, 2, 3, 4, 5])

# print(ran_avg, ran_sum)

DAYS = ("Mon", "Tue", "Wed", "Thurs", "Fri")
# weekend_days = ["Sat", 'Sun']

# sorted_days = sorted(DAYS)
# print(tuple(sorted_days))
# sorted_WED = sorted(weekend_days)
# print(sorted_WED)

# for day in DAYS:
#     print(day)

# print(DAYS[1:3])

# def compare(val):
#     return val[1]

# def index_sort(tuple_list):
#     # sorted_list = sorted(tuple_list, key=compare, reverse=True) # lambda val: val[1]
#     # return sorted_list
#     tuple_list.sort(key=compare)
#     return tuple_list


# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]



# ARGS & KWARGS
# def sum_function(num_1, num_2, num_3=15, *args, **kwargs):
#     print("OG parameters", num_1, num_2, num_3)
#     func_sum = num_1 + num_2 + num_3
#     print("args", args)
#     for arg in args:
#         func_sum += arg
    
#     print(kwargs)

#     return func_sum

# print(sum_function(5, 10, 20, 25, 30, 35, num_7=40, num_8=45))


# RANGES
# values = range(start,stop,step)
# vals = range(1,10,2)
# print(vals)
# print(tuple(vals))

lunch = ["wings", "pizza", "turkey", "salmon"]

# for index in range(len(lunch)):
#     print(index, lunch[index])

# more_vals = range(50, 0, -10)
# print(list(more_vals))

# enum_values = enumerate(lunch, 1)
# # print(enum_values)
# print(list(enum_values))

# for index, food in enumerate(lunch, 1):
#     print(f'{index}. {food}')


# Problem 3 - Factorial
# Write your function, here.
# def factorial(num):
#     total = 1
#     for val in range(1, num + 1):
#         total *= val
#     return total

# print(factorial(1))     #> 1
# print(factorial(8))     #> 40320  # [1, 2, 3, 4, 5, 6, 7, 8]
# print(factorial(12))    #> 479001600

# def recur_fact(num):
#     if num == 1:
#         return num

#     return num * recur_fact(num -1)


# print(recur_fact(1))     #> 1
# print(recur_fact(8))     #> 40320  # [1, 2, 3, 4, 5, 6, 7, 8]
# print(recur_fact(12))    #> 479001600

# Problem 4 - Check Nested Arrays
# Your code, here.

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
meals = {
    "breakfast": "coffee",
    "lunch": "wings",
    "dinner": "pizza",
    "dessert": "ice cream",
    4: "meals",
    True: "even more meals"
}

# print(meals)
# print(meals['dinner'])
# print(meals["second breakfast"])
# print(meals.get("dinner"))
# print(meals.get("second, breakfast", "No key with that name in dictionary"))

# if meals.get("second breakfast") is None:
#     meals["second breakfast"] = "apple"
# else:
#     print("Key already exists")

# print(meals)
# meals["second breakfast"] = "two apples"
# print(meals)
# del meals[True]
# print(meals)
# meals.update({"elevensies": "danish", "supper": "Roast Beef"})
# print(meals)

# print("second breakfast" in meals)
# print("Tea time" in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key in meals.keys():
#     print(key)

# for val in meals.values():
#     print(val)

# for key, val in meals.items():
#     print(f"{key}: {val}")


    # ARGS & KWARGS

# def sum_function(num_1, num_2, num_3=15, *args, **kwargs):
#     print("OG parameters", num_1, num_2, num_3)
#     func_sum = num_1 + num_2 + num_3
#     print("args", args)
#     for arg in args:
#         func_sum += arg
    
#     print(kwargs)
#     for kwarg in kwargs.values():
#         func_sum += kwarg

#     return func_sum

# print(sum_function(5, 10, 20, 25, 30, 35, num_7=40, num_8=45))


# SPLAT OPERATOR

# lst1 = ["a", "b", "c"]
# lst2 = [1, 2, 3]
# lst3 = [*lst1, *lst2]
# print(lst3)

# dict1 = {
#     "breakfast": "eggs",
#     "lunch": "wings",
#     "dinner": "pizza"
# }

# dict2 = {**dict1}

# print(dict2)


# def merge_lists(list_1, list_2):
    # SOLVE 1
    # return_dict = {}
    # for index, value in enumerate(list_1):
    #     return_dict[value] = list_2[index]

    # return return_dict

    # SOLVE 2
    # merged_list = []
    # for index in range(len(list_1)):
    #     merge_tuple = (list_1[index], list_2[index])
    #     merged_list.append(merge_tuple)
    # print(merged_list)
    # return dict(merged_list)

    # SOLVE 3
    # return dict(zip(list_1, list_2))

# lst1 = ['a', 'b']
# lst2 = [1, 2]
# merged_dict = merge_lists(lst1, lst2)
# print(merged_dict)      # { 'a': 1, 'b': 2 }

# SETS

# empty_set = set()

# not_empty_set = {1, "hello", 3}
# print(not_empty_set)
# print({1})

# list_27 = [1, 2, 2, 3, 4, 5, 5, 5, 5, 7, 9, 9, 12]
# print(set(list_27))

# string_1 = "hello"
# print(set(string_1))
# list_of_strings = ["pizza", "wings", "beverages", "wings"]
# print(set(list_of_strings))
# # print(not_empty_set[2])

# for val in not_empty_set:
#     print(val)


# my_set = {1, 2, 3, 4 }
# print(1 in my_set)
# my_set.add(5)
# print(my_set)
# my_set.update({5, 5, 6})
# print(my_set)
# my_set.remove(5)
# print(my_set)

a = {0, 1, 2, 3}
b = {2, 3, 4, 5, 6}

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

# Write your code here.
# def check_binary(string):
#     set_str = set(string)
#     # return set_str == {"0", '1'} or set_str == {"0"} or set_str == {'1'}
#     # return set_str.issubset({"0", "1"})
#     list_of_sets = [{"0", "1"}, {"0"}, {'1'}]
#     return set_str in list_of_sets

# str1 = '1010001010010100101'
# str2 = '1010010015010101010'

# print(check_binary(str1))       # True
# print(check_binary(str2))       # False

# BUILT IN FUNCTIONS

# SORTED
# names = ["JAMES", "julie", "Ana", "Ria"]

# sorted_names = sorted(names, key=lambda val: val.lower(), reverse=True)
# print(tuple(sorted_names))

# ALL & ANY
# test = ["1", False, 0]
# test_2 =  []
# test_3 = {1, 2, 3}
# ALL is happy if nothing inside is falsy
# print(all(test))
# print(all(test_2))
# print(all(test_3))
# ANY is haooy if at least 1 item is truthy
# print(any(test))
# print(any(test_2))
# print(any(test_3))

# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# only_as = filter(lambda grade: grade >= 90, scores)
# print(only_as)
# list_grades = list(only_as)
# print(set(list_grades))

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
# scores = [90, 86, 75, 91, 62, 99, 88, 90, 100, 3000]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]

# combined = zip(scores, grades)
# print(combined)
# combined_list = list(combined)
# zipped_dict = dict(combined_list)
# print(combined_list)
# print(zipped_dict)

# TUPLE = ("Hello")
# TUPLE = ("Goodbye")
# print(TUPLE)

# phones = [
#     {
#         "brand": "Apple",
#         "model": "iPhone 13 Pro",
#         "cost": 929,
#         "color": "alpine green"
#     },
#     {
#         "brand": "Samsung",
#         "model": "Galaxy S22+",
#         "cost": 999,
#         "color": "black"
#     },
#     {
#         "brand": "Google",
#         "model": "Pixel 6",
#         "cost": 599,
#         "color": "kinda coral"
#     },
#     {
#         "brand": "Apple",
#         "model": "iPhone 13 Pro",
#         "cost": 929,
#         "color": "gold"
#     },
#     {
#         "brand": "Google",
#         "model": "Pixel 6",
#         "cost": 599,
#         "color": "stormy black"
#     }
# ]

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


# COMPREHENSTIONS
# my_list = [1, "2", True, "butter", None]
# my_list_copy = [item for item in my_list] 
# print(my_list_copy)
# my_list_copy2 = [*my_list]
# print(my_list_copy)

nums = [-11, -5, 11, 10, 14]
# mapped_nums = map(lambda num: num * 2, nums)
# print(list(mapped_nums))
# mapped_comp = [num * 2 for num in nums]
# print(mapped_comp)

# new_list = []
# for num in nums:
#     new_list.append(num * 2)

# print(new_list)

# filtered_comp = [num for num in nums if num > 0]
# print(filtered_comp)

# mapped_and_filtered_comp = [num * 2 for num in nums if num > 0]
# print(mapped_and_filtered_comp)

# names = ['brad', 'david', 'andrew', 'dan', 'keegan']
# cap_comp = [ name.title() for name in names ]
# print(cap_comp)

# users = [user.to_dict() for user in User.query.all()]


# DICTIONARY COMPREHENSIONS
# number_dictionary = { num: num**2 for num in nums }
# print(number_dictionary)

breaks = {
    "lunch": 2,
    "afternoon": 6,
    "EOD": 7,
}

print(breaks)
daylight_savings = { key: value - 1 for key, value in breaks.items()}
print(daylight_savings)