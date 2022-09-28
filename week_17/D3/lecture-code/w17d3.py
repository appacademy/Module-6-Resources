# # TUPLE

# tup = ("red", "blue")
# print(id(tup))
# print(tup)
# tup += 'green', 'orange'
# print(id(tup))
# print(tup)
# num = 2
# num += 2
# num = 4 
# print(tup[1])

# tup2 = 'Brad', 'John', 'Cesar'
# print(tup2)

# # EMPTY TUPLE
# tup3 = ()

# # SINGLETON TUPLE
# tup4 = 1,
# tup5 = (1,)

# tup6 = ([1, 2, 3], [4, 5, 6])
# print(tup6)

def sum_and_average(lst):
    list_sum = sum(lst)
    average = list_sum / len(lst)
    return (list_sum, average)


# returned_sum, returned_average = sum_and_average([1, 2, 3, 4])
# print(returned_sum, returned_average)

# DO NOT CHANGE THE VALUE OF DAYS PLEASE
# DAYS = ("Mon", "Tue", "Wed", "Thur", "Fri")

# sorted_days = sorted(DAYS)
# print(tuple(sorted_days))
# print(DAYS[1:3])

# def funct(num, *args):
#     func_sum = num
#     for arg in args:
#         print(arg)
#         func_sum += arg
#     return func_sum

# print(funct(1, 2, 3))

# Write your function, here.
def big_words(tup):
#   return tuple([x for x in tup if len(x) > 8])

    final_list = []
    for t in tup:
        if len(t) > 8:
            final_list.append(t)
    return tuple(final_list)    

# print(big_words(('earth', 'jupiter', 'mars', 'neptune'))) #> ()
# print(big_words(('wakanda', 'melbourne', 'london', 'france'))) #> ('melbourne',)
# print(big_words(('app', 'academy', 'app academy', 'xylophone'))) #> ('app academy', 'xylophone')


# Problem 6 - Index Sort
# Write your function, here.

def compare(val):
    return val[1]

def index_sort(tuple_list):
    tuple_list.sort(key=compare) # lambda x: x[1]
    return tuple_list

# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]


# RANGES & ENUMERATE
values = range(1, 5, 1)
# print(list(values))

lunch = ["wings", "pizza", "sandwich"]

# for index in range(len(lunch)):
#     print(index, lunch[index])

# revered range
range(10, 0, -1)

# print(list(enumerate(lunch, 1)))

# for i, v in enumerate(lunch, 1):
#     print(f'{i}. {v}')


# Check Nested Arrays

# Your code, here.
# def list_max(lst):
#   max = lst[0]
#   for i in range(1, len(lst)):
#     l = lst[i]
#     if l > max:
#       max = l
#   return max

# def list_min(lst):
#   min = lst[0]
#   for i in range(1, len(lst)):
#     l = lst[i]
#     if l < min:
#       min = l
#   return min

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
    "lunch": "wings",
    "dinner": "pizza",
    "dessert": "ice cream",
    4: "meals",
    True: "even more meals",
    'second breakfast': 'apple'
}

# print(meals)
# print(meals.get('second breakfast', "Key not in dictionary"))

# if meals.get('second breakfast') is None:
#     meals['second breakfast'] = 'apple'
# else:
#     print("Key already exists")

# print(meals)
# meals['second breakfast'] = 'cake'
# print(meals)
# del meals[4]
# print(meals)

# print("breakfast" in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key in meals.keys():
#     print(key)

# for val in meals.values():
#     print(val)

# for key, val in meals.items():
#     print(key, "  ", val)


# ARGS/KWARGS

def sum(num1, num2, *args, **kwargs):
    total = num1 + num2
    print("args", args)
    for val in args:
        total += val
    print("kwargs", kwargs)
    for more_vals in kwargs.values():
        total += more_vals
    return total

# print(sum(10, 15, 25, 30, num5=15, num6=20))

lst_1 = ['a', 'b', 'c']
lst_2 = [1, 2, 3]
lst_3 = [*lst_1, *lst_2] 
# print(lst_3)

dict_1 = {
    "breakfast": "coffee",
    "lunch": "wings",
    "dinner": "pizza"
}

dict_2 = {**dict_1}
# print(dict_2)

# SETS

# EMPTY DICTIONARY
my_dict = {}

#EMPTY SET
# my_set = set()

# my_next_set = {1, "hello", None}
# print(my_next_set)

# ones = {1, 1, 1}
# print(ones)

# list_new = [1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7]
# print(list(set(list_new)))

# string = "hello"
# print(set(string))

# my_set = { 1, 2, 3, 4}
# print(my_set)
# my_set.add(5)
# print(my_set)
# my_set.remove(2)
# print(my_set)

# for item in my_set:
#     print(item)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# UNION
# print( a | b)
# print(a.union(b))

# INTERSECTION
# print( a & b)
# print(a.intersection(b))

# DIFFERENCE
# print(a - b)
# print(a.difference(b))
# print(b - a)

# SYMMETRIC DIFFERENCE
# print( a ^ b)
# print(a.symmetric_difference(b))


# BUILT IN FUNCTIONS
names = ["JAMES", "julie", "Ana", "Ria" ]
sorted_names = sorted(names, key=lambda x: x.lower(), reverse=True)
# print(sorted_names)

# ALL & ANY
# test = ['Hey', False, 0]
# test2 = {}

# print("all", all(test2))
# print("any", any(test2))


# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# only_as = filter(lambda grade: grade >= 90, scores)
# print(only_as)
# print(list(only_as))

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

# mapped_scores = map(get_grade, scores)
# print(mapped_scores)
# print(list(mapped_scores))

# ZIP
scores = [90, 86, 75, 91, 62, 99, 88, 90, 78, 50]
grades = ["A", "B", "C", "A", "D", "A", "B", "A"]

# combined = zip(scores, grades)
# print(combined)
# combined_list = list(combined)
# new_dict = dict(combined_list)
# print(new_dict)


# REMOVE DUPLICATES SOLUTION EXPLAINED

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


def get_unique_models(phone_list):
    seen = []
    return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)
    
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

def get_unique_models(phones):
    just_models = map(lambda phone: phone['model'], phones)
    print(list(set(just_models)))


# unique_models = list(get_unique_models(phones))
# print(unique_models)                # iPhone 13 Pro, Galaxy S22+, Pixel 6 (dictionaries)
# print(map_to_names(unique_models))  # iPhone 13 Pro, Galaxy S22+, Pixel 6
# get_unique_models(phones)

# LIST COMPREHENSION
# my_list = [1, "2", 'THREE', True, None]
# my_list_copy = [item for item in my_list]
# print(my_list_copy)

# for item in my_list:
#     my_list_copy.append(item)

# nums = [-5, 11, 10, 14]
# mapped_nums = map(lambda num: num * 2, nums)
# print(list(mapped_nums))

mapped_comp_nums = [num * 2 for num in nums]
print(mapped_comp_nums)

filter_comp_nums = [num for num in nums if num > 0]
print(filter_comp_nums)

map_and_filter_comp_nums = [num * 2 for num in nums if num > 0]
print(map_and_filter_comp_nums)

number_dict = { num: num**2 for num in range(5)}
print(number_dict)

breaks = {
    'lunch': 2,
    'afternoon': 6,
    'EOD': 7
}

daylight_saving = {k: v + 1 for k, v in breaks.items()}
print(daylight_saving)