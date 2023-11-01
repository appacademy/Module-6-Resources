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