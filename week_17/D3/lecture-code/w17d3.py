# TUPLES
# tup = ('red', 'blue')
# tup += "green", "orange"

# print(tup)
# print(tup[1:3])

# # EMPTY TUPLE
# tup_2 = ()

# # SINGLETON TUPLE
# tup_3 = (2,)
# tup_4 = 5, 


def sum_and_average(lst):
    list_sum = sum(lst)
    average = list_sum / len(lst)
    return (list_sum, average)


# print(sum_and_average([1, 2, 3, 4]))
# lst_sum, lst_avg = sum_and_average([1, 2, 3, 4])
# print(lst_sum, lst_avg)

# DAYS = ("Mon", "Tue", "Wed", "Thur", "Fri")
# sorted_days = sorted(DAYS)
# print(tuple(sorted_days))

# def function(num, *args):
#     total = num
#     print(num, args)
#     # for arg in args:
#     #     total += arg
#     total += sum(args)
#     return total

# print(function(1, 2, 3))

# BIG WORDS
def big_words(tup):
    big_word = []
    for word in tup:
        if len(word) >= 8:
            big_word.append(word)
    return tuple(big_word)
    # return tuple([x for x in tup if len(x) > 8])


# print(big_words(('earth', 'jupiter', 'mars', 'neptune'))) #> ()
# print(big_words(('wakanda', 'melbourne', 'london', 'france'))) #> ('melbourne',)
# print(big_words(('app', 'academy', 'app academy', 'xylophone'))) #> ('app academy', 'xylophone')

def compare(val):
    return val[1]
# INDEX SORT 
def index_sort(tuple_list):
    tuple_list.sort(key=compare, reverse=True) # lambda val: val[1]
    return tuple_list

# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
results = [2, 8, 5, 0]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]


# names = ["brad", "Marc", "David"]
# names.sort(key=lambda name: name.upper())
# print(names)

# RANGES & ENUMERATE
# values = range(start,stop,step)
# values = range(10, 0, -1)
# print(set(values))

lunch = ["pizza", "wings", "sandwich"]
# for food in lunch:
#     pass

# for index in range(len(lunch)):
#     print(index, f". {lunch[index]}")

# print(list(enumerate(lunch)))

# for index, value in enumerate(lunch, 1):
#     print(f"{index}. {value}")

# from math import factorial as sandwich
# FACTORIAL with a RANGE
# def factorial(num):
#     total = 1
#     for num in range(1, num + 1):
#         total *= num
#     return total


# print(factorial(1))     #> 1
# print(factorial(8))     #> 40320
# print(factorial(12))    #> 479001600




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


# BUILT IN FUNCTIONS
# SORTED
# names = {"JAMES", "julie", "Ana", "Ria"}
# sorted_names = sorted(names, key=lambda x: x.lower())
# print(tuple(sorted_names))

# ALL & ANY
# test = ['', True, None]
# test1 = []
# print(all(test))
# print(all(test1))
# test2 = ['', True, None]
# test3 = []
# print(any(test2))
# print(any(test3))
# all is happy if nothing inside is falsy, 
# any is happy if at least one thing is truthy

# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# # only_as = filter(lambda score: score >= 90, scores)
# # print(set(only_as))

# # MAP 
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
# print(tuple(mapped_grades))


# ZIP
# scores = [90, 86, 75, 91, 62, 99, 88, 90, 100, 100, 100]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
# combined = zip(grades, scores)
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
def get_unique_models(phone_list):
    just_models = map(lambda phone: phone["model"], phone_list)
    print(list(set(just_models)))

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


# COMPREHENSIONS

# my_list = [1, '2', 'three', True, 'bacon']
# my_list_copy = [item for item in my_list]
# print(my_list_copy)

# my_list_copy_2 = [*my_list]
# print(my_list_copy_2)

# MAPPING WITH LC
# nums = [-5, -2, 1, 3, 5, 8, 9]
# mapped_list = [num * 2 for num in nums]
# print(mapped_list)

# # FILTER WITH LC
# filter_nums = [num for num in nums if num > 0 ]
# print(filter_nums)

# # MAP & FILTER
# mapped_filtered_nums = [num * 2 for num in nums if num > 0]
# print(mapped_filtered_nums)

# DICTIONARY COMPREHENSION

# number_dict = { num: num**2 for num in range(15)}
# print(number_dict)

breaks = {
    "lunch": 2,
    "afternoon": 6,
    "EOD": 7,
}

daylight_saving = {key: value + 1 for key, value in breaks.items() if value >= 6 }
print(daylight_saving)





# THIS IS MY USUAL LECTURE CODE ON DICTIONARIES AND SETS
# DICTIONARIES

meals = {
    'breakfast': 'coffee',
    'lunch': 'wings',
    'dinner': 'pizza',
    'dessert': 'ice cream',
    4: 'meals',
    True: 'even more meals',
    'second breakfast': 'apple'
}


# print(meals)
# print(meals.get('second breakfast', "Key not in dictionary!"))

# if meals.get("second breakfast") is None:
#     meals["second breakfast"] = 'apple'
# else:
#     print("Key already exists")

# print(meals)

# meals['second breakfast'] = 'taters'

# print(meals)
# del meals[4]
# print(meals)
# meals[1] = 'apple'
# print(meals)
# meals[True] = 'cake'
# print(meals)
# meals.update(new_dict)  will concat dictionaries

# print("binner" in meals) 

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for k, v in meals.items():
#     print(f'{k}: {v}')

# for val in meals.values():
#     print(val)


# ARGS / KWARGS

def sum (num1, num2, *args, **kwargs):
    total = num1 + num2
    print("args", args)
    for val in args:
        total += val
    print("kwargs", kwargs)
    for more_vals in kwargs.values():
        total += more_vals
    return total

# print(sum(10, 15, 25, 30, num5=15, num6=20))

lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]
lst3 = [*lst1, *lst2]
# print(lst3)

dict1 = {
    "breakfast": 'eggs',
    "lunch": 'wings',
    "dinner": 'pizza'
}

dict2 = {**dict1}

# print(dict2)

# Write your code here.
def merge_lists(list_1, list_2):
  # return dict(zip(list_1, list_2))
  return_dict = {}
  for index, value in enumerate(list_1):
    return_dict[value] = list_2[index]

  return return_dict

lst1 = ['a', 'b']
lst2 = [1, 2]
merged_dict = merge_lists(lst1, lst2)
print(merged_dict)      # { 'a': 1, 'b': 2 }



# SETS
# new_set = set()
# another_set = {1, 2, 3}
# print(new_set)
# print((another_set))

# list1 = [1, 2, 2, 3, 3, 4, 5, 6, 6, 7]
# print(set(list1))

# string1 = "hello"
# print(set(string1))

my_set = {1, 2, 3, 4}
print(1 in my_set)
# print(my_set)
# # my_set.add(5)
# # print(my_set)
# my_set.update([5, 6])
# my_set.remove(2)
# print(my_set)


# UNION
# print(a | b)
# print(a.union(b))

# INTERSECTION
# print(a & b)
# print(a.intersection(b))

# DIFFERENCE
# print(a - b)
# print(a.difference(b))
# print(b - a)

a = {0, 1, 2, 3}
b = {0, 1, 5, 6}

# SYMMETRIC DIFFERENCE
# print(a ^ b)
# print(a.symmetric_difference(b))