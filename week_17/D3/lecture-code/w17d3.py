# TUPLES

# tuple_1 = ("red", "blue")
# print(tuple_1)
# tuple_1 += ("green", "orange")
# print(tuple_1)
# print(tuple_1[1:3])

# tup3 = "Brad", "Cesar", "David", "Drew"
# print(tup3)

# EMPTY TUPLE
tup4 = ()
# SINGLETON TUPLE
tup5 = 1,
tup6 = (1,)
# print(isinstance(tup6, tuple()))

list_1 = [1, 2, 3]
# print(tuple(list_1))

DAYS = ("Mon", "Tue", "Wed", "Thur", "Fri")
sorted_days = sorted(DAYS)
# print(sorted_days)

def sum_and_average(lst):
    list_sum = sum(lst)
    average = list_sum / len(lst)
    return (list_sum, average)


list_sum, list_average = sum_and_average([1, 2, 3, 4])
# print(list_sum, list_average)

def func(num, *args):
    sum_vals = num
    print(args)
    for arg in args:
        sum_vals += arg
    return sum_vals

# print(func(2, 4, 6, 8))


# names = ["Brad", "Drew", "david", "cesar"]
# names.sort(key=lambda x: x.upper())
# print(names)


# # Problem 4 - Big Words
# # Write your function, here.
# Write your function, here.
def big_words(tup):
    return_list = []
    for item in tup:
        if len(item) > 8:
            return_list.append(item)
    return tuple(return_list)

#   return tuple([x for x in tup if len(x) > 8])

# Problem 6 - Index Sort
# Write your function, here.

def compare(val):  
    return val[1]

def index_sort(tuple_list):
    tuple_list.sort(key=compare) # alternate lambda x: x[1]
    return tuple_list

# RANGES & ENUMERATE
# range(start, stop, step)
# int_range = range(1, 11, 1)
# print(int_range)
# print(list(int_range))
int_range = range(10, 0, -1)
# print(int_range)
# print(list(int_range))

lunch = ["pizza", "sandwich", "soup"]

# for index in range(len(lunch)-1,-1,-1):
#     print(f'{index}. {lunch[index]}')

# print(enumerate(lunch))
# print(list(enumerate(lunch, 1)))

# for index, val in enumerate(lunch, 1):
#     print(f'{index}. {val}')


# DICTIONARIES

meals = {
    'breakfast': "coffee",
    'lunch': 'wings',
    'dinner': 'pizza',
    'dessert': 'ice cream',
    4: 'meals',
    True: 'even more meals',
    "second breakfast": 'apple'
}

# print(meals)
# print(meals["lunch"]) 
# print(meals.get("second breakfast", "Key not in dictionary"))
# print("before trying to add", meals)

# if meals.get('second breakfast') is None:
#     meals["second breakfast"] = 'apple'
# else:
#     print("key already exists")

# print("before",meals)

# meals["second breakfast"] = 'taters'
# del meals[True]

# print('after', meals)

# print("brinner" in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for k, v in meals.items():
#     print(k, v)


# for value in meals.values():
#     print(value)

# meals2= dict(breakfast="coffee", lunch="wings", dinner="pizza")
# print(meals2)

# ARGS/KWARGS

def sum(num1, num2, *args, **kwargs):
    total = num1 + num2
    print('args', args)
    for val in args:
        total += val
    print(kwargs)
    for more_vals in kwargs.values():
        total += more_vals
    return total

# print(sum(2, 3, 4, 5, num5=10, num6=15))

# lst1 = ['a', 'b', 'c']
# lst2 = [1, 2, 3]
# lst3 = [*lst1, *lst2]
# print(lst3)

dic1 = {
    "breakfast": 'eggs',
    "lunch": 'wings',
    "dinner": 'pizza',
    "meals": {
        1: "coffee",
        2: "sandwich"
    }
}

dic2 = {**dic1}

# print(dic2)


# SETS
# new_set = set()

# new_set_maybe = {} # not good, makes a dictionary
# print(type(new_set_maybe))
# new_set_2 = {1, 2, 3}
# print(new_set, new_set_2)

# list_1 = [1, 2, 2, 2, 3, 3, 4, 5, 6, 6, 7]
# print(list(set(list_1)))

# string = "hello"
# print(set(string))

# my_set = {1, 2, 3, 4}
# print(my_set)
# my_set.add(5)
# print(my_set)
# my_set.remove(2)
# print(my_set)


# UNIONS
# print(a | b)
# print(a.union(b))

# INTERSECTION
# print(a & b)
# print(a.intersection(b))

a = {1, 2, 3}
b = {3, 4, 5}

# DIFFERENCE
# print(a - b)
# print(a.difference(b))
# print(b - a)

# SYMMETRIC DIFFERENCE
# print(a ^ b)
# print(a.symmetric_difference(b))



# BUILT INS
# SORTED
# names = ["JAMES", "julie", "Ana", "Ria"]
# sorted_names = sorted(names, key=lambda x: x.lower())
# print(sorted_names)

# ALL & ANY
# tests = ['pickle', False, 0, '']
# print("All", all(tests))
# print("Any", any(tests))

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


# grades = map(get_grade, scores)
# print(grades)
# print(list(grades))


# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]

# combined = zip(scores, grades)
# print(combined)
# combined_list = list(combined)
# combined_dict = dict(combined_list)
# print(combined_dict)

# Remove Dubplicates
def get_unique_models(phone_list):
    seen = []
    return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)
    
    # so what is going on here in the filter method???
    # think of the lambda statement being written like this...
    if phone['model'] not in seen:
        return seen.append(phone['model']) is None
    else:
        return False
    
    # Because this is a callback in a filter, it needs to return True or False
    # to determine if the value gets added to our filtered list
    
    # In the else, we return False, makes sense...
    # The append method does not have a return, but we know that if a
    # function does not have a set return value, it returns None!
    # So we check if the return value is None, which will evaluate to true!


# COMPREHENSIONS
my_list = [1, "2", 'THREE', True, None]
my_list_copy = [item for item in my_list]
# print(my_list_copy)

# my_list_copy = []
# for item in my_list:
#     my_list_copy.append(item)

# nums = [-5, 11, 10, 14]
# mapped_nums = [ num * 2 for num in nums]
# print(mapped_nums)

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

scores = [90, 86, 75, 91, 62, 99, 88, 90]
# mapped_scores = [get_grade(score) for score in scores]
# print(mapped_scores)
filtered_scores = [ score for score in scores if score >= 90 ]
# print(filtered_scores)

# DICTIONARY COMPREHENSION
number_dict = { num: num**2 for num in range(5)}
# print(number_dict)

breaks = {
    'lunch': 2,
    'afternoon': 6,
    'EOD': 7
}
print(breaks)

daylight_saving = { key: val + 1 for key, val in breaks.items() }
print(breaks.items())
print(daylight_saving)