# TUPLES

# tup = ("red", "blue")
# tup = ("yellow", "green")  # no error, this works
# print(tup)                 # ("yellow", "green")
# tup += ("red", "blue")    # no error, this works
# print(tup)    


# tup2 = (1, 2, 4)
# tup3 = 2, 4, 6

# tup4 = ()

# single_tuple = 3,
# single_tuple2 = (3,)

# tup1 = ('turn', 'on')
# tup2 = ('the', 'red', 'light', '!')
# tup3 = tup1 + tup2
# print(tup3)
# print(' '.join(tup3))
# # for val in tup3:
# #     print(val)
# print(tuple(sorted(tup3)))

# RANGES & ENUMERATE

# values = range(20,0,-5)
# print(values)

# drinks = ["coffee", "tea", "soda"]
# for i in range(len(drinks)):
#     print(i, drinks[i])
# print(list(enumerate(drinks)))
# for i, value in enumerate(drinks, 1):
#     print(f"{i}. {value}")


# DICTIONARIES
# meals = {
#     "breakfast": "coffee",
#     "lunch": "sandwich",
#     "dinner": "hamburger",
#     "dessert": "ice cream",
#     4: "meals"
# }

# # print(meals.get("second breakfast"))
# if meals.get("second breakfast") is None:
#     meals["second breakfast"] = "banana"
# else:
#     print("Key already exists")

# print(meals)
# meals["dinner"] = "pizza"
# print(meals)
# del meals["second breakfast"]
# print(meals)


# SETS
# not_an_empty_set = {}
# print(type(not_an_empty_set))
 
# empty_set = set()
# print(type(empty_set))
 
# set_with_elements = {1, "hello", None}
# print(set_with_elements)
 
# ones = {1, 1, 1}
# print(ones)


# lst1 = [1, 1, 3, 3, 4, 5, 6, 6]
# unique_list = set(lst1)
# print(list(unique_list))


# # union of two sets
# a = {0, 1}
# b = {0, 1, 5}
# print(a | b)       # {1, 2, 3, 4, 5}
# print(a.union(b))  # {1, 2, 3, 4, 5}

# # # intersection of two sets
# print(a & b)       # {2, 3}
# print(a.intersection(b))  # {2, 3}

# # # difference of two sets
# print(a - b) # {1}
# print(b.difference(a)) # {4, 5}

# # # symmetric difference
# print(a ^ b) # {1, 4, 5}
# print(b.symmetric_difference(a)) # {1, 4, 5}

# BUILT INS
# SORTED
# names = ["JAMES", "julie", "Ana", "Ria"]
# # sorted_names = sorted(names)
# # print(sorted_names)
 
# # ensure a case-insensitive sort with the `.lower` string method 
# # and sort in reverse order
# sorted_names = sorted(names, key= lambda x: x.lower(), reverse=True)
# print(sorted_names)
# ALL & ANY
# test = ["item", [], []]
# print(all(test)) # True
# print(any(test)) # False
# FILTER
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# only_as = filter(lambda num: num >= 90, scores)
# print(only_as)        # <filter object at 0x10546ad30>
# print(list(only_as))  # [90, 91, 99, 90]
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
# # print(map(get_grade, scores))  # <map object at 0x106faffa0>
# # grades = list(map(get_grade, scores))
# # print(grades)                  # ['A', 'B', 'C', 'A', 'D', 'A', 'B', 'A']
# curve = map(lambda x: x + 5, scores)
# print(list(curve))


# ZIP
# scores = [90, 86, 75, 91, 62, 99, 88, 90]
# grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
# more_info = ["Pizza", "Sandwich", "Coffee"]
# combined = zip(scores, grades, more_info)
# combined_list = list(combined)
# # combined_dict = dict(combined_list)
# print(combined)       # <zip object at 0x1023a9600>
# print(combined_list)  # [(90, 'A'), (86, 'B'), (75, 'C'), (91, 'A'), (62, 'D'), (99, 'A'), (88, 'B'), (90, 'A')]
# # print(combined_dict)  # {90: 'A', 86: 'B', 75: 'C', 91: 'A', 62: 'D', 99: 'A', 88: 'B'}


# COMPREHENSIONS
# my_list = [1, "2", "three", True, None]
# my_list_copy = [ item for item in my_list]
#     for loop
#    ----------
# /               \
# for item in my_list:
#     my_list_copy.append(item)
# #                        |
# #                       var
# print(my_list_copy)  # [1, '2', 'three', True, None]
# print(my_list)
nums = [-5, 11, 10, 14]
# # mapped_nums = map(lambda num: num * 2 + 1, nums)
# mapped_nums = [num * 2 + 1 for num in nums ]
# print(list(mapped_nums))  # [-9, 23, 21, 29]
# filtered_nums = filter(lambda num: num > 0, nums)
filtered_nums = [ num for num in nums if num > 0 ] 

# new_list = []
# for num in nums:
#     if num > 0:
#         new_list.append(num)

# print(filtered_nums)  # [11, 10, 14]

# a dictionary that maps numbers to the square of the number
number_dict = { num: num**2 for num in range(5) }
print(number_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

breaks = {
    "lunch": 3,
    "afternoon": 5,
    "EOD": 7,
}

daylight_savings = { k: v + 1 for k, v in breaks.items() }
print(daylight_savings)