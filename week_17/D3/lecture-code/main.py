from pprint import pprint
empty_ls = []
str_ls = list("banana")


# print(str_ls)

num = [1,2,3,4,5]

# print(num[0])


# print(num[2:4])

# print(num)

# arr.length

# print(len(num))
# print(num.__len__())

num.append(6)

# print(num)

num.extend([7,8,9,10])
# print(num)

# num.append([7,8,9,10])

# print(num)

num.remove(1)


# print(num)
# num.remove(40)

random_nums = [0.1, 6,3,8,2,9,10,400,2,555]

# random_nums.sort()


# print(random_nums)

# random_nums.pop()
# print(random_nums)

# random_nums.pop(4)

# print(random_nums)


# num.insert(0, 1)

# print(num)

# print(random_nums)

sorted_nums = sorted(random_nums)

# print(sorted_nums)

# print(random_nums)

# print(sum(sorted_nums))
# print(min(sorted_nums))
# print(max(sorted_nums))

bare_tuple = 1,2,3,4,5

# print(type(bare_tuple))

singleton_tup = 1,


# print(type(singleton_tup))


# print(1,2,3,4,5) # five integers
# print((1,2,3,4,5)) # single tuple

tup_from_ls = tuple([1,2,3,4,5])

empty_tup = tuple()
# another_empty_tup = ()
# print(empty_tup)

# print(tup_from_ls)

new_tup = bare_tuple + tup_from_ls


# print(new_tup)

new_tup += 10,
# print(new_tup)

def sum_min_max(iter):
    return sum(iter), min(iter), max(iter)


# print(sum_min_max(new_tup))

# my_sum, my_min, my_max = sum_min_max(tup_from_ls)


fruits = "banana", "avocado", "apple", "orange"

sorted_fruits = tuple(sorted(fruits))

# print(fruits)
# print(sorted_fruits)

def recursive_add(tup): 
  if not tup:
    return 0
  return tup[0] + recursive_add(tup[1:])
  
# print(fruits[:3])

# print(recursive_add((2, )))               #> 2
# print(recursive_add((2, 4, 6, 8, 10)))    #> 30
# print(recursive_add((25, 50, 75, 100)))   #> 250

# print(list(range(0,10, 2)))

# for idx in range(len(fruits)): # range(4) = 0 , 1, 2, 3
#     print(fruits[idx])

# for idx in range(len(fruits)-1, -1, -1):
#     print(fruits[idx])

# for idx in range(-1, -len(fruits) - 1, -1):
#     print(fruits[idx])

squared_nums = []

for num in range(1, 11):
    squared_nums.append(num ** 2)

# print(squared_nums)

# print(list(range(0, -11, -1)))

# for idx, ele in enumerate(fruits):
    # print(idx, ele)
    # fruits[idx] = 5 # TypeError: tuples are immutable


def factorial(num):
  fact = 1
  for num in range(1, num+1):
    fact *= num
  return fact


# print(factorial(1))     #> 1
# print(factorial(8))     #> 40320
# print(factorial(12))    #> 479001600

crazy_dict = { None: "none", True: False, ("goat", 8): "tuple", 7: 0, "string": lambda x: x, factorial: "factorial", "factorial": "not factorial" } # dictionaries can take a whole bunch of differeny keyss
my_dict = { "name": "David", "age": 38, "role": "Supreme leader of mod 6"} # but strings are probably the most common keys


# print(crazy_dict[factorial]) # factorial in this case in the function factorial, which is a valid key

new_func = factorial # the function name is not important; the function itself is what matters, so now we can use the new_func variable as a key

# factorial = 5 # reassigning the factorial variable name will mean we can no longer use it to key into that key-value pair
# print(crazy_dict[factorial]) # KeyError

# print(crazy_dict[new_func]) # "factorial"


def factorial():
    return 9

# print(crazy_dict[factorial]) # KeyError

# print(crazy_dict[new_func]) # "factorial"

# crazy_dict.("goat", 8) # SyntaxError

con_dict = dict([("key", "value"),("key2", "value2")]) # creates dictionary: { "key": "value", "key2": "value2" }

# print(con_dict) # { "key": "value", "key2": "value2" }
age = "age"
# print(my_dict["name"]) # "David"

# print(my_dict[age]) # 38

# print(my_dict["height"]) # KeyError

# print(my_dict.get("height", "height does not exist on my_dict")) #  "height does not exist on my_dict"
# print(my_dict.get("role", None)) # "Supreme leader of mod 6"

# print(crazy_dict["goat", 8]) # "tuple"


del my_dict["age"] # removes the "age" key-value pair from dictionary

# print(my_dict)

my_dict["age"] = 25 # adds a new key "age" with a value of 25

# print(my_dict)

my_dict["age"] = 38 # updates "age" key with new value of 38
# print(my_dict)


# print(dir(dict)


# for key, val in my_dict.items(): # items with give us an iterable with each key-value pair as an element, and we store each in key and value
#     print(key, val)

# ARGS AND KWARGS

# *: single splat **: double splat

# print(my_dict)

# my_obj = { ...old_obj } javascript spread
new_dict = { **my_dict }

ls = [1,2,3,4,5]
new_ls = [*ls]

# print(new_ls)
# print(new_dict)


def print_some_data_types(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# print_some_data_types(1,2,3,4,5,6,7, key="value", random="sdfjhsaoiuudhv bng22t80bnvsdflkdfgh", test=6)


def print_tuple(*tup, key):
    print(tup)
    print(key)

# print_tuple(1,2,3,4,5, key=6, key_two=5)


def print_objs(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)


# print_objs(1, 2, 3, 4, key="value")

# Sets

set1 = {1, 2, 1, 2, 1, 2, 3, 4, 3, 5, 7, 6, 8, 6, 9, 7, 9, 0}

# print(set1)

set2 = set()
# print(set2)

ls1 = [1, 2, 1, 2, 1, 2, 3, 4, 3, 5, 7, 6, 8, 6, 9, 7, 9, 0]

set3 = set(ls1)
# print(set3)

# print(set("hello"))

odds = {1,3,5,7,9,11,13,15,17,19}
nums = {1,2,3,4,5,6,7,8,9,10}

# print(odds | nums)
# print(odds.union(nums))

# print(odds & nums)
# print(odds.intersection(nums))

# print(odds - nums) # odds.difference(nums)
# print(nums - odds) # nums.difference(odds)
# print(nums ^ odds) # nums.symmetric_difference(odds)


def remove_repeats(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    return (str1 - str2) | (str2 - str1) # return str1 ^ str2

str1 = 'aloha'
str2 = 'bonjour'

my_set = (remove_repeats(str1, str2))    # {'r', 'a', 'l', 'h', 'n', 'b', 'j', 'u'}

# sorted_set_ls = sorted(my_set)
sorted_set_ls = sorted(my_set, reverse=True)

teachers = ["David", "keagan", "andrew", "Brad"]

# print(sorted(teachers, key=str.lower))

# print(sorted_set_ls)

ls1 = [True, False, True, False, True, False]
ls2 = [True, True, True, True, True]
ls3 = [False, False, False, False]
ls4 = []

# print(all(ls1))
# print(all(ls2))
# print(all(ls3))
# print(all(ls4))
#
# print(any(ls1))
# print(any(ls2))
# print(any(ls3))
# print(any(ls4))


# print(help(any))

important_teachers = list(filter(lambda x: x == x.lower(), teachers))


# print(important_teachers)

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
# print(map(get_grade, scores))  # <map object at 0x106faffa0>
grades = list(map(get_grade, scores))
# print(grades)                  # ['A', 'B', 'C', 'A', 'D', 'A', 'B', 'A']
 

scores = [90, 86, 75, 91, 62, 99, 88, 90, 100] # extra element in scores is not included in zip
grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
combined = zip(scores, grades)
combined_list = list(combined)
combined_dict = dict(combined_list)
# print(combined)       # <zip object at 0x1023a9600>
# print(combined_list)  # [(90, 'A'), (86, 'B'), (75, 'C'), (91, 'A'), (62, 'D'), (99, 'A'), (88, 'B'), (90, 'A')]
# print(combined_dict)  # {90: 'A', 86: 'B', 75: 'C', 91: 'A', 62: 'D', 99: 'A', 88: 'B'}

def get_unique_models(phone_list):
    seen = []
    unique_models = []
    for phone in phone_list:
        if phone["brand"] in seen:
            continue
        seen.append(phone["brand"])
        unique_models.append(phone)
    return unique_models

def map_to_names(phone_list):
    names = []
    for phone in phone_list:
        names.append(phone["model"])
    return names

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




unique_models = list(get_unique_models(phones))
# pprint(unique_models)                # iPhone 13 Pro, Galaxy S22+, Pixel 6 (dictionaries)
# pprint(map_to_names(unique_models))  # iPhone 13 Pro, Galaxy S22+, Pixel 6


ls = [1,2,3,4,5,6,7,8,9]

# new_ls = [el % 3 if el <= 2 else el % 2 for el in ls if el < 7]
new_ls = [el for el in ls]
# new_ls = [el for el in ls if el < 7]
# new_ls = list(filter(lambda x: x < 7, ls))
# new_ls = [el % 2 for el in ls]
# new_ls = list(map(lambda x: x % 2, ls))
# new_ls = [el % 2 for el in ls if el < 7]

# zeroes = [0 for member in new_ls]

# print(ls is new_ls)
# print(ls == new_ls)

# print(new_ls)
# print(zeroes)

ones = []

# for item in zeroes:
    # ones.append(item + 1)

# print(ones)
# ones = [item + 1 for item in zeroes]
# print(ones)


nums = [item for item in range(100)]

# print(nums)
nums = [-5, 11, 10, 14]
chars = ["f", "g", "h", "y", "l"]

# print([num > 0 for num in nums])

# print([num for num in nums if num > 0])

# pprint({ num: num **2 for num in nums})

# pprint({key: val for key, val in zip(nums, chars)})

# pprint({key: val for key, val in enumerate(nums)})


