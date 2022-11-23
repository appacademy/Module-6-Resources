# # TUPLES

# tup = ('red', 'blue')
# tup += 'green', 'orange'

# # print(tup)
# # print(tup[1:3])

# # tup_2 = 'Brad', 'John', 'David', 'Andrew'
# # print(tup_2)

# # EMPTY TUPLE
# tup_3 = ()
# # SINGLETON TUPLE
# tup_4 = 1,
# tup_5 = (2,)

# def sum_and_average(lst):
#     list_sum = sum(lst)
#     average = list_sum / len(lst)
#     return (list_sum, average)

# average, list_sum = sum_and_average([1, 2, 3, 4])
# # print(average, list_sum)

# DAYS = ("Mon", "Tue", "Wed", "Thurs", "Fri")

# sorted_days = sorted(DAYS)
# # print(tuple(sorted_days))

# for day in DAYS:
#     print(day)


# TUPLE Problem # 6 - Index Sort

# def compare(val):
#     return val[1]

# def index_sort(tuple_list):
#     tuple_list.sort(key=compare) # lambda x: x[1]
#     return tuple_list


# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]


# instructors = ["Brad", 'andrew', 'David', "John"]
# instructors.sort(key=lambda x: x.lower())
# print(instructors)

# RANGES

# values = range(start,stop,step)
values = range(1,11)
# print(values)
# print(list(values))

# new_range = range(2, 51, 2)
# print(list(new_range))

# for i in range(10, 1, -1):
#     print(i)


# sides = ['stuffing', 'potatoes', 'salad', "cranberry relish"]

# print(list(enumerate(sides)))

# for i, val in enumerate(sides, start=1):
#     print(f'{i}. {val}')


# Check Nested LISTS
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
    'breakfast': 'coffee',
    'lunch': 'pizza',
    'dinner': 'wings',
    'dessert': 'ice cream',
    4: 'meals',
    True: 'even more meals',
}

# print(meals)
# print(meals['lunch'])
# print(meals[4])

# print(meals.get("dessert"))
# print(meals.get("second breakfast", "Key not in dictionary!"))

# if meals.get('second breakfast') is None:
#     meals['second breakfast'] = 'apple'
# else:
#     print('Key already exists')

# meals['dinner'] = "tacos"
# print(meals)
# del meals[True]
# print(meals)

# print("dinner" in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key in meals.keys():
#     print(key)

# for k, v in meals.items():
#     print(k, ': ', v)


# ARGS / KWARGS

def sum(num_1, num_2, *args, **kwargs):
    total = num_1 + num_2
    print('args', args)
    for val in args:
        total += val
    print('kwargs', kwargs)
    for more_vals in kwargs.values():
        total += more_vals
    return total


# print(sum(10, 15, 20, 25, num_5 = 30, num_6 = 35))


# lst_1 = ['a', 'b', 'c']
# lst_2 = [1, 2, 3]
# lst_3 = [*lst_1, *lst_2]
# lst_4 = [*lst_2]
# print(lst_3)
# print(lst_4)

# dict_1 = {
#     'breakfast': 'coffee',
#     'lunch': 'pizza',
#     'dinner': 'wings',
# }

# dict_2 = {**dict_1}

# print(dict_2)

# SETS

new_set = set()
new_dictionary = {}

another_set = {1, 2, 3}
# print(another_set)

# list_23 = [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7, 8, 8, 9]
# print(list(set(list_23)))

# string_1 = "hello"
# print(set(string_1))

my_set = {1, 2, 3, 4}
# print(1 in my_set)

# my_set.add(8)
# print(my_set)
# my_set.remove(2)
# print(my_set)

set_1 = {0, 2, 4, 6, 8}
set_2 = {1, 2, 3, 4, 5, 9}

set_2.pop()
set_2.pop()
# print(set_2)
# set_1.pop()
# set_1.add(10)
# set_1.pop()
# print(set_1)

# UNION
# print(set_1 | set_2)
# print( set_1.union(set_2))

# # INTERSECTION 
# print(set_1 & set_2)
# print( set_1.intersection(set_2))

# DIFFERENCE
# print(set_1 - set_2)
# print(set_1.difference(set_2))
# print(set_2.difference(set_1))

# # SYMMETRIC DIFFERENCE
# print(set_1 ^ set_2)
# print(set_1.symmetric_difference(set_2))



# CHECK BINARY
def check_binary(string):
    set_string = set(string)
    print(set_string)
    return set_string.issubset({'0', '1'})

# {'1'}
# {'0'}
# {'1', '0'}

str1 = '1010001010010100101'
str2 = '1010010015010101010'

# print(check_binary(str1))       # True
# print(check_binary(str2))       # False

# BUILT IN FUNCTIONS
# names = ["JAMES", "julie", 'Ana', 'Ria']
# sorted_names = sorted(names, key=lambda x: x.lower(), reverse=True)
# print(sorted_names)



# ALL vs ANY

# test = ['Turkey', True, 1]

# test_2 = {}
# print('all', all(test))
# # all is happy if nothing inside is falsy
# print('any', any(test))
# any is happy if at least one thing is truthy

# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# only_as = filter(lambda num: num >= 90 , scores)
# print(set(only_as))

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
# print(list(mapped_grades))

# ZIP
scores = [90, 86, 75, 91, 62, 99, 88, 90, 70, 45]
grades = ["A", "B", "C", "A", "D", "A", "B", "A"]

combined = zip(scores, grades)
# print(list(combined))
combined_dict = dict(list(combined))
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

my_list = [1, '2', "THREE", True, None]
my_list_copy = [item for item in my_list]
# print(my_list_copy)

# Copying the above list without a comprehension
my_list_copy = []
for item in my_list:
    my_list_copy.append(item)

nums = [-5, 11, 10, 14]
mapped_nums = map(lambda num: num *2, nums)
mapped_nums_comp = [num * 2 for num in nums]
# print(mapped_nums_comp)
# filter_nums_comp = [num for num in nums if num > 0]
# print(filter_nums_comp)
# map_and_filter = [num * 2 for num in nums if num > 0]
# print(map_and_filter)

# DICTIONARY COMPREHENSIONS

number_dict = { num: num**2 for num in range(5)}
# print(number_dict)

breaks = {
    'lunch': 2,
    'afternoon': 6,
    'eod': 7,
}

daylight_saving = {k: v + 1 for k, v in breaks.items()}
print(daylight_saving)
