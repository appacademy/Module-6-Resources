# TUPLES
# string = "pizza"
# string += "pizza"
# print(string)

# tup = ("red", "blue")
# tup += "green", "orange"

# print(tup)

# # EMPTY TUPLES
# tup2 = ()
# tup3 = tuple()

# # SINGLE VALUE SINGLETON
# tup4 = 1,
# tup5 = (2,)

# print(tup[1:3])
# for color in tup:
#     print(color)


# DAYS = ("Mon", "Tues", "Wed", "Thurs", "Fri")

# def sum_and_average(lst):
#     list_sum = sum(lst)
#     average = list_sum / len(lst)
#     return (list_sum, average)

# list_sum, list_avg = sum_and_average([1,2,3,4,5])
# print(list_sum, list_avg)

# sorted_days = sorted(DAYS)
# print(tuple(sorted_days))

# def compare(val):
#     return val[1]

# def index_sort(tuple_list):
#     sorted_list = sorted(tuple_list, key=compare, reverse=True ) #lambda val: val[1]
#     return sorted_list


# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]

# def function(num1, num2, num3=30, *args):
#     total = num1 + num2 + num3
#     # print(num1, num2, num3)
#     print(args)
#     for arg in args:
#         total += arg

#     return total

# print("total:", function(10, 20, 40, 50, 60))

# RANGES
# values = range(start, stop, step)
# values = range(10)
# print(tuple(values))
# print(list(range(10, 0, -1)))

# lunch = ["wings", "pizza", "sandwich", "soup"]

# for index in range(len(lunch)):
#     print(lunch[index])

# print(list(enumerate(lunch)))

# for index, food in enumerate(lunch, 1):
#     print(f"{index}. {food}")

# def factorial(n):
#     total = 1
#     for integer in range(1, n + 1):
#         total *= integer

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
#     "second breakfast": "apple",
#     "elevensies": "cookie",
#     "luncheon": "turkey club",
#     4: "meals",
# }
# print(meals)

# print(meals["breakfast"])
# # print(meals["afternoon tea"])
# # print(meals.get("afternoon tea", "no tea for you!"))

# if meals.get("afternoon tea") is None:
#     meals["afternoon tea"] = "earl gray tea"
# else:
#     print("Key already exists!")

# print(meals)
# meals["afternoon tea"] = "peppermint tea"
# print(meals)
# del meals[4]
# print(meals)
# meals.update({"dinner": "roast beast", "supper": "taters"})
# print(meals)

# print("second breakfast" in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key in meals.keys():
#     print(key)


# for key, val in meals.items():
#     print(key, val)


# def function(num1, num2, num3=30, *args, **kwargs):
#     total = num1 + num2 + num3
#     # print(num1, num2, num3)
#     print(args)
#     for arg in args:
#         total += arg

#     print(kwargs)
#     for val in kwargs.values():
#         total += val

#     return total

# print("total:", function(10, 20, 40, 50, 60, num6=70, num7=80))


# lst1 = ['a', 'b', 'c']
# lst2 = [1, 2, 3 ]
# lst3 = [*lst1, *lst2]
# print(lst3)

# meals = {
#     "breakfast": "eggs",
#     "second breakfast": "apple",
#     "elevensies": "cookie",
#     "luncheon": "turkey club",
#     4: "meals",
# }

# meal_copy = {**meals}
# print(meal_copy)

# def merge_lists(lst1, lst2):
#     return_dict = {}

#     for index, value in enumerate(lst1):
#         return_dict[value] = lst2[index]

#     return return_dict


# def merge_lists2(lst1, lst2):
#     # merged_list = []
#     # for index in range(len(lst1)):
#     #     merged_tuple = (lst1[index], lst2[index])
#     #     merged_list.append(merged_tuple)
#     merged_list = zip(lst1, lst2)
#     print(merged_list)
#     return dict(merged_list)

#     # print(merged_list)
#     # return dict(merged_list)


# lst1 = ('a', 'b', 'c')
# lst2 = (1, 2, 3)
# merged_dict = merge_lists2(lst1, lst2)
# print(merged_dict)


# SETS
# EMPTY SET
# set1 = set()
# set2 = {1, 2, 3, 4, 5}

# list1 = [1, 2, 2, 2, 2, 3, 3, 3, 34, 4, 4, 4, 5, 5, 6]
# list_no_dups = set(list1)
# print(list_no_dups)

# print(3 in set2)
# print(8 in set2)

# set2.add(6)
# print(set2)
# set2.add(6)
# print(set2)
# # set12 = {1, 1, 1, 2, 2, 2, 3, 3 }
# # print(set12)
# set2.remove(3)
# print(set2)
# # print(set2[2])

# for val in set2:
#     print(val)

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# # UNION
# print( a | b)
# print(a.union(b))

# # INTERSECTION
# print( a & b )
# print(a.intersection(b))

# # DIFFERENCE
# print(a - b)
# print(a.difference(b))
# print(b - a)
# # SYMMETTRIC DIFFERENCE
# print(a ^ b)
# print(a.symmetric_difference(b))


def check_binary(num):
    return set(num).issubset({1, 0})


# BUILT-IN FUNCTIONS

teachers = "brad", "David", "Andrew"

nums = 1, 6, 4, 9, 210

# print(sorted(teachers, key=str.lower, reverse=True))
# print(sorted(nums, key=lambda x: -x))


word = "hello"

ls = [0, 5, 6]
empty_ls = []

# print(all(ls))
# print(any(ls))
# print(all(empty_ls))
# print(any(empty_ls))


def is_a(num):
    return num >= 90


scores = 89, 67, 100, 99, 84, 93, 70, 99
just_as = filter(is_a, scores)
# jst_as = filter(lambda x: X >= 90, scores)
# print(just_as)
# print(list(just_as))


def get_grade(num):
    if num >= 90:
        return "A"
    elif num < 90 and num >= 80:
        return "B"
    elif num < 80 and num >= 70:
        return "C"
    elif num < 70 and num >= 60:
        return "D"
    else:
        return "F"


# grades = map(get_grade, scores)
grades = "B", "D", "A", "A"

# print(grades)
# for el in grades:
#     print(el)
#     if el == "A":
#         break

# print(list(grades))
# print(scores)

# zipped_grades = zip(scores, grades)
# print(zipped_grades)
# print(dict(zipped_grades))
# print(list(zipped_grades))

# for idx, score in enumerate(scores):
#     print(f"index is {idx}")
#     print(f"score is {score}")

phones = [
    {"brand": "Apple", "model": "iPhone 13 Pro", "cost": 929, "color": "alpine green"},
    {"brand": "Samsung", "model": "Galaxy S22+", "cost": 999, "color": "black"},
    {"brand": "Google", "model": "Pixel 6", "cost": 599, "color": "kinda coral"},
    {"brand": "Apple", "model": "iPhone 13 Pro", "cost": 929, "color": "gold"},
    {"brand": "Google", "model": "Pixel 6", "cost": 599, "color": "stormy black"},
]


def get_unique_models(phones):
    previous_models = []
    unique_models = []
    for phone in phones:
        if phone["model"] in previous_models:
            continue
        else:
            previous_models.append(phone["model"])
            unique_models.append(phone)
    return unique_models


# print(get_unique_models(phones))
unique_phones = get_unique_models(phones)


def map_to_names(phones):
    return list(map(lambda phone: phone["model"], phones))


# print(map_to_names(unique_phones))

# COMPREHENSIONS

ls = [1, 2, 3, 4, 5]

my_first_comp = [el * 2 for el in ls]

boring_old_map = map(lambda x: x * 2, ls)

# print(list(boring_old_map))

filtered_and_mapped = [el**2 for el in ls if el % 2 != 0]

# print(filtered_and_mapped)

# print(my_first_comp)

# print([1 for el in ls if el % 2 == 0])

not_comp = []
for member in ls:
    not_comp.append(member)


mapped_ls = [num * 2 + 1 for num in ls]

# print(mapped_ls)

print({num + 1: num**2 for num in ls})
