# TUPLES

# tup_1 = ("red", "blue")
# print(tup_1) 
# tup_1 += ("green", "orange")
# print(tup_1) 


# # EMPTHY
# tup_2 = ()
# tup_x = tuple()
# # SINGLETON TUPLSE
# tup_3 = 1,
# tup_4 = (1,)


# print(tup_1[2])
# print(tup_1[1:3])

# for color in tup_1:
#     print(color)



# def sum_and_average(lst):
#     list_sum = sum(lst)
#     average = list_sum / len(lst)
#     return (list_sum, average)

# results = sum_and_average([1, 2, 3, 4, 5])
# print(results)
# ret_sum, ret_avg = results
# print(ret_avg, ret_sum)


# DAYS = ("MON", "TUE", "WED", "THUR", "FRI")
# vals = [5, 4, 3, 2, 1]

# sorted_days = sorted(DAYS)
# print(tuple(sorted_days))
# sorted_vals = sorted(vals) 
# print(sorted_vals)

# def compare(val):
#     return val[1]

# def index_sort(tuple_list):
#     # tuple_list.sort( key=compare)
#     sorted_list = sorted(tuple_list, key=compare, reverse=True)  # lambda val: val[1]

#     return sorted_list



# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]


# RANGES
# values = range(10, 0, -1)
# print(values)
# print(tuple(values))


# lunch = ["wings", "pizza", "sandwich", "chef salad"]

# for index in range(len(lunch)):
#     print(index, lunch[index])

# vals = enumerate(lunch)
# print(list(vals))

# for index, value in enumerate(lunch, 1):
#     print(f"{index}. {value}")


# def factorial(number):
#     total = 1
#     for index in range(1, number + 1):
#         total *= index

#     return total


# def recur_factorial(number):
#     if number == 1:
#         return number

#     else:
#         return number * recur_factorial(number - 1)


# # print(factorial(1))     #> 1
# # print(factorial(8))     #> 40320
# # print(factorial(12))    #> 479001600
# # print(recur_factorial(1))     #> 1
# # print(recur_factorial(8))     #> 40320
# # print(recur_factorial(12))    #> 479001600


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
    "lunch": "pizza",
    "dinner": "wings",
    "dessert": "pie",
    4: "meals",    
}

# print(meals)
# print(meals[4])
# print(meals["breakfast"])

# # print(meals["second breakfast"])

# print(meals.get("second breakfast", 'NO KEY FOR YOU!!!'))

# if meals.get("second breakfast") is None:
#     meals["second breakfast"] = "apple"
# else:
#     print("Key already exists!")

# print(meals)

# meals["second breakfast"] = "taters"

# print(meals)

# del meals["lunch"]
# print(meals)
# meals.update({"elevensies": "waffle", "supper": "whole turkey"})
# print(meals)

# print("dinner" in meals)
# print("brinner" in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key in meals.keys():
#     print(key)

# for key, val in meals.items():
#     print(key, val)


# ARGS/KWARGS

# def sum_num(num1, num2, num3=30, *args, **kwargs):
#     print(num1, num2, num3)
#     total = num1 + num2 + num3
#     print(args)
#     for arg in args:
#         total += arg 
#     print(kwargs)
#     for kwarg_val in kwargs.values():
#         total += kwarg_val
#     return total


# print(sum_num(10, 20, 40, 50, 60, 70, 80, num8=90, num9=100))

# lst1 = ["a", "b", "c"]
# lst2 = [1, 2, 3]
# lst3 = [*lst1, *lst2]
# print(lst3)

# dict1 = {
#     "breakfast": "eggs",
#     "lunch": "wings",
#     "dinner": "pizza",
# }

# dict2 = {**dict1}
# print(dict2)


# def merge_lists(list_1, list_2):
#     return_dict = {}
#     for index, val in enumerate(list_1):
#         return_dict[val] = list_2[index]

#     return return_dict

# def merge_lists2(list_1, list_2):
#     merged_list = []
#     for index in range(len(list_1)):
#         merge_tuple = (list_1[index], list_2[index])
#         merged_list.append(merge_tuple)
#     print(merged_list)
#     return dict(merged_list)


# merge_lists3 = lambda list_1, list_2: dict(zip(list_1, list_2))


# lst1 = ('a', 'b', 'c')
# lst2 = (1, 2, 3)
# merged_dict = merge_lists3(lst1, lst2)
# print(merged_dict)  


 # SETS
# new_set = set()
# another_set = {1, 2, 3}
# print(new_set)
# print(another_set)

# nums = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 7, 7]
# print(list(set(nums))) 

# string1 = "hello"
# print(set(string1))

# my_set = {1, 2, 3, 3, 3, 4, 5}
# print(my_set)
# print(1 in my_set)
# # print(my_set[2])
# my_set.add(6)
# print(my_set)
# my_set.update([7, 8])
# print(my_set)
# my_set.remove(3)
# print(my_set)

a = {0, 1, 2, 3}
b = {2, 3, 4, 5}


#UNION
# print( a | b )
# print(a.union(b))


# INTERSECTION
# print(a & b)
# print(a.intersection(b))

#DIFFERENCE
# print(a - b)
# print(a.difference(b))
# print(b - a)

# SYMMETRIC DIFFERENCE
print(a ^ b)
print(a.symmetric_difference(b))