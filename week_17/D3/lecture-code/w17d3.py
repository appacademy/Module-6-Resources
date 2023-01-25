# TUPLES

tup = ('red', 'blue')
tup += 'green', 'orange'
# print(tup)
# print(tup[1])

# EMPTY TUPLE
tup_2 = ()

# SINGLETON TUPLE
tup_3 = 1,
tup_4 = (1,)

def sum_and_average(lst):
    list_sum = sum(lst)
    average = list_sum / len(lst)
    return (list_sum, average)


# list_sum, avg = sum_and_average([1, 2, 3, 4])
# print(list_sum, avg)


DAYS = ("Mon", "Tue", "Wed", "Thurs", "Fri")

# sorted_days = sorted(DAYS)
# print(set(sorted_days))

def function(num, num_2=3, *args, **kwargs):
    print(num, num_2)
    # print(args)
    # for arg in args:
    #     print(arg)

# function(1, 6, 45, 56, 78)


# Tuple Problem Index Sort
def compare(val):
    return val[1]


def index_sort(tup_list):
    # tup_list.sort(key=compare, reverse=True ) # lambda tup: tup[1]
    sorted_list = sorted(tup_list,key=lambda tup: tup[1])
    return sorted_list


# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]

# RANGES & ENUMERATE

# values = range(5)
# print(values)
# print(tuple(values))

# for index in range(5, 0, -1):
#     print(index)


# lunch = ['wings', 'pizza', 'sandwich', 'salad']
# print(list(enumerate(lunch)))

# for index, value in enumerate(lunch, start=1):
#     print(f'{index}.', value)


# Problem 4 - Check Nested Arrays
# Your code, here.
def can_nest(list_1, list_2):
    list1_min = min(list_1)
    list1_max = max(list_1)
    list2_min = min(list_2)
    list2_max = max(list_2)
    return list1_min > list2_min and list1_max < list2_max


# def list_min(lst):
#   min = lst[0]
#   for i in range(1, len(lst)):
#     l = lst[i]
#     if l < min:
#       min = l
#   return min

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
    4: 'meals',
    True: "even more meals",
}

empty_dict = {}

# print(meals)
# print(len(meals))
# print(meals['lunch'])
# print(meals["second breakfast"])
# print(meals.get("second breakfast", "Key not in dictionary!"))

if meals.get("second breakfast") is None:
    meals["second breakfast"] = "apple"
else:
    print('Key already exists')

# print(meals)
# meals["dinner"] = "creamed spinach"
# print(meals)
# del meals[True]
# print(meals)
    

# print("dinner" in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key in meals.keys():
#     print("keys", key)


# for val in meals.values():
#     print("vals", val)


# for k, v in meals.items():
#     print(k, v)


# ARGS / KWARGS

def sum(num_1, num_2, num_3 = 5, *args, **kwargs):
    total = num_1 + num_2 + num_3
    print(total)
    print("args", args)

    cb(*args, **kwargs)
    for arg in args:
        total += arg

    print("kwargs", kwargs)
    for val in kwargs.values():
        total += val

    return total

# print("total when done", sum(10, 20, 25, 30 , 35,num_6 = 40, num_7 = 45))


lst_1 = ['a', 'b', 'c']
lst_2 = [1, 2, 3]
lst_3 = [*lst_1, *lst_2]
lst_4 = [*lst_3]
# print(lst_3)

dict_1 = {
    "breakfast": "eggs",
    "lunch": "wings",
    "dinner": "pizza",
}

# dict_2 = {**dict_1}
# print(dict_2)


# SETS

# new_set = set()
# new_set2 = {} # <- this is a empty dictionary, not a set

# new_set3 = {1, 2, 3, 4, 5, 5, 5, 6}
# print(new_set3)
# list_1 = [1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]
# print(list(set(list_1)))


# string_1 = "hello"
# print(set(string_1))

# set_2 = {1, 2, 3, 4}
# print(2 in set_2)
# print(5 in set_2)
# # print(set_2[2])
# set_2.add(5)
# print(set_2)
# set_2.update({6, 7})
# print(set_2)
# set_2.remove(6)
# print(set_2)

# list_dic = [
#     [1, 2, 3, 4],
#     [1, 2, 3, 4]
# ]

# print(set(list_dic))

# SET OPERATIONS

a = {1, 2, 3, 4 }
b = {2, 4, 6, 8 }

# UNION
# print(a | b)
# print(a.union(b))

# INTERSECTIONS
# print(a & b)
# print(a.intersection(b))

# DIFFERENCE
# print(a - b)
# print(b - a)
# print(a.difference(b))

# SYMETRIC DIFFERENCE
# print(a ^ b)
# print(a.symmetric_difference(b))


# BUILT In FUNCTIONS
# SORTED
# names = ["JAMES", "julie", 'Ana', "Ria"]
# sorted_names = sorted(names, key=lambda x: x.lower(), reverse=True)
# # print(sorted_names)

# ALL ANY
# all is happy if nothing inside is falsy
# any is happy if at least one thing is truthy
test_1 = ['', 4, True]
test_2 = {}

# print(all(test_1))
# print(all(test_2))
# print(any(test_1))
# print(any(test_2))


# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
# only_as = filter(lambda score: score >= 90, scores)
# print(tuple(only_as))
# print(list(only_as))

# MAP
def get_grade(num):
    if (num >= 90):
        return "A"
    elif (num < 90 and num >= 80):
        return "B"
    elif (num < 80 and num >= 70):
        return "C"
    elif (num < 70 and num >= 60):
        return "D"
    else:
        return "F"

# mapped_scores = map(get_grade, scores)
# print(list(mapped_scores))


# ZIP
# scores = [90, 86, 75, 91, 62, 99, 88, 90, 99, 86, 30]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
# combined = zip(grades, scores)
# print(combined)
# print(dict(combined))



# REMOVE DUPLICATES SOLUTION EXPLAINED

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

def get_unique_models(phone_list):
    just_models = map(lambda phone: phone["model"], phone_list)
    print(list(set(just_models)))

# get_unique_models(phones)


# COMPREHENSIONS
# my_list = [1, '2', 'THREE', True, None]
# my_list_copy = [ item for item in my_list]
# my_list_copy = [*my_list]
# print(my_list_copy)

# my_list_copy = []
# for item in my_list:
#     my_list_copy.append(item)

scores = [90, 86, 75, 91, 62, 99, 88, 90, 99, 86, 30]
# mapped_scores = [get_grade(score) for score in scores]
# print(mapped_scores)
curved_scores = [score + 5 for score in scores]
# print(curved_scores)

# only_a_grades = [score + 5 for score in scores if score >= 90]
# print(only_a_grades)

# only_a_grades_mapped = [get_grade(score) if score > 80 else score for score in scores ]
# print(only_a_grades_mapped)


# DICTIONARY COMPREHENSHIONS
number_dict = { num: num**2 for num in range(15)}
print(number_dict)

breaks = {
    'lunch': 2,
    'afternoon': 6,
    'EOD': 7,
}

daylight_savings = { k: v + 1 for k, v in breaks.items()}
print(daylight_savings)
