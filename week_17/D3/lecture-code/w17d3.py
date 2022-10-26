# TUPLES

tup = ('red', 'blue')
# print(tup)
tup += ('green', 'orange')
tup = tup + ('green', 'orange')

num = 1
num += 1
# print(tup)
# print(tup[1])

tup2 = "Brad", "John", "David"
# print(tup2)

# EMPTY TUPLE
tup3 = ()
# SINGLETON TUPLE
tup4 = 1,
tup5 = (1,)


def sum_and_average(lst):
    list_sum = sum(lst)
    average = list_sum / len(lst)
    return (list_sum, average)

# print(sum_and_average([1, 2, 3, 4]))

# tup_sum, tup_avg = sum_and_average([1, 2, 3, 4])
# print(tup_sum, tup_avg)


DAYS = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri')

sorted_days = sorted(DAYS)
# print(tuple(sorted_days))
# print(DAYS[2:4])

# for day in DAYS:
#     print(day)


# INDEX SORT PROBLEM
def compare(val):
    return val[1]

# def index_sort(tup_list):
#     tup_list.sort(key= compare) # can use lambda x: x[1]
#     return tup_list


# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]


# Write your function, here.
# def big_words(tup):
#   return tuple([  x for x in tup if len(x) > 8])


# print(big_words(('earth', 'jupiter', 'mars', 'neptune'))) #> ()
# print(big_words(('wakanda', 'melbourne', 'london', 'france'))) #> ('melbourne',)
# print(big_words(('app', 'academy', 'app academy', 'xylophone'))) #> ('app academy', 'xylophone')


# RANGES & ENUMERATE

values = range(1, 11)
# print(values)
# print(list(values))

lunch = ['wings', 'pizza', 'sandwich']

# for i in range(len(lunch)): # [0, 1, 2]
#     print(lunch[i])


# print(list(enumerate(lunch, 1)))

# for i, v in enumerate(lunch, 1):
#     print(f'{i}. {v}')


# Problem 4 - Check Nested Arrays
# Your code, here.

# def can_nest(list1, list2):

#     if True:
#         print('True')

#     if False:
#         print("False")
#         if num == 1:
#             pass
#         if num == 2:
#             pass

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
    'breakfast': 'coffee',
    'lunch': 'ramen',
    'dinner': 'pizza',
    'dessert': 'ice cream',
    4: 'meals',
    True: "even more meals",
}

# print(meals)
# print(meals['lunch'])
# print(meals.get('second breakfast'))

# if meals.get('dessert') is None:
#     meals['dessert'] = 'apple'
# else:
#     print("Key already exists")

# print(meals)
# meals['dinner'] = 'wings'
# print(meals)

# # print("dinner" in meals)
# del meals['dinner']
# print(meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key, val in meals.items():
#     print(key, val)


def sum_all(num1, num2, num3=7, *args, **kwargs):
    print(num1, num2, num3)
    total = num1 + num2 + num3
    print("args", args)
    for val in args:
        total += val
    print("kwargs", kwargs)
    for more_vals in kwargs.values():
        total += more_vals
    return total


# print(sum_all(2, 4, 6, 8, 10, num6 = 12, num7=14))

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = [*list1, *list2]
# print(list3)

dict1 = {
    'breakfast': 'coffee',
    'lunch': 'ramen',
    'dinner': 'pizza',
}

dict2 = {**dict1}
# print(dict2)

# SETS

new_set = set()
new_dict = {} # not a set, dictionary
new_set2 = {1, 2, 3, 4, 5}

list1 = [1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7]
# print(list(set(list1)))

# string1 = "hello"
# print(set(string1))

# print(2 in new_set2)

my_set = {1, 2, 3, 4}
# my_set.add(5)
# print(my_set)
# my_set.remove(2)
# print(my_set)

a = {1, 2, 3}
b = {3, 4, 5}

# UNIONS
# print(a | b)
# print(a.union(b))

# # INTERSECTION
# print(a & b)
# print(a.intersection(b))

# DIFFERENCE
# print(a - b)
# print(a.difference(b))
# print(b - a)

# SYMMETRIC DIFFERENCE
# print(a ^ b)
# print(a.symmetric_difference(b))


# BUILT IN FUNCTIONS

# SORTED
def compare(x):
    return x.lower()

names = ("JAMES", "julie", "Ana", "Ria")
sorted_names = sorted(names, key= lambda x: x.lower(), reverse=True)
# print(tuple(sorted_names))


# ALL / ANY
test = [0, False, ""]
test2 = {}
# print('all - test', all(test))
# print('all - test2', all(test2))
# print('any - test', any(test))
# print('any - test2', any(test2))

# all is happy if nothing inside is falsy, 
# any is happy if at least one thing is truthy

# FILTER

# only_as = filter(lambda score: score >= 90, scores)
# print(list(only_as))


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

# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# mapped_grades = map(get_grade, scores)
# print(list(mapped_grades))

# ZIP
scores = [90, 86, 75, 91, 62, 99, 88, 90 ]
grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
combined = zip(scores, grades)
# combined_list = list(combined)
combined_dict = dict(combined)
# print(combined_list)
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
#     just_models = map(lambda phone: phone['model'], phone_list)
#     print(list(set(just_models)))

# get_unique_models(phones)

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


# COMPREHENSIONS
# my_list = [1, '2', "THREE", True, None]
# my_list_copy = [item for item in my_list]
# print(my_list)
# print(my_list_copy)


# my_list_copy2 = []
# for item in my_list:
#     my_list_copy2.append(item)

nums = [-5, 11, 10, 14, -10, 23]
# mapped_nums = map(lambda num: num * 2, nums)
# print(list(mapped_nums))
# comprehension_nums = [ num * 2 for num in nums]
# print(comprehension_nums)
# filter_comp_nums = [ num for num in nums if num > 0]
# print(filter_comp_nums)
def times_2(num):
    return num * 2

map_and_filter_comp = [times_2(num) for num in nums if num > 0]
# print(map_and_filter_comp)

# DICTIONARY COMPREHENSIONS
numbers_dict = { num: num**2 for num in range(5) }
# print(numbers_dict)

breaks = {
    'lunch': 2,
    'afternoon': 6,
    'EOD': 7
}

print(breaks)
daylight_savings = { k: v + 1 for k, v in breaks.items() }
print(daylight_savings)