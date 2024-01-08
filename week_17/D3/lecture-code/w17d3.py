# TUPLES

sandwiches = "hot dog", "grilled cheese", "quesadilla", "falafel sandwich", "gyro"

sandwich = ( "burrito", )

empty_tup = ()
empty_tup = tuple()

# print(type(sandwiches))
#
# print(sandwiches)
# print(sandwich)
# print(empty_tup)
#
# print(empty_ls)

# print(dir(sandwiches))
# print(dir(list))

sandwiches += sandwich

# print(sandwiches)

soups = ["lucky charms", "gazpacho", "warm ice cream", "chowder", "chili"]
soups.append("ice water")
soups.append("oatmeal")

soups = tuple(soups)
# print(type(soups))
# print(soups)

# print(dir(soups))

# sorted_soups = sorted(soups)

# print(soups)
# print(sorted_soups)

def fill_tuple(tups, val, length):
    ls = []
    for tup in tups:
        ls.append(tup + (val,) * (length - len(tup)))
    return tuple(ls)
  # return tuple([tuple([tup[idx] if idx < len(tup) else val for idx in range(length)]) for tup in tups])

# print(fill_tuple(((58, 1, 5), (0, 3), (45, ), (24, 23)), 2, 3))    #> ((58, 1, 5), (0, 3, 2), (45, 2, 2), (24, 23, 2))
# print(fill_tuple(((1, ), (5, 7), (55, 22), (80, 52, 20)), 5, 4))   #> ((1, 5, 5, 5), (5, 7, 5, 5), (55, 22, 5, 5), (80, 52, 20, 5))
# print(fill_tuple(((), (0, 14), (5, 2, 8), (2, 4, 2, 3)), 0, 5))    #> ((0, 0, 0, 0, 0), (0, 14, 0, 0, 0), (5, 2, 8, 0, 0), (2, 4, 2, 3, 0))

test_tup = 1,2,3

new_tup = test_tup + (1,)
# print(new_tup)

def second_ele(tup):
    return tup[1]

def index_sort(tups):
    return sorted(tups, key=lambda x: x[1])

# print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
# print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
# print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]

# RANGES

new_range = range(10)
# print(type(new_range))
# print(list(new_range))

# for i in range(0, len(sandwiches), 2):
#     print(sandwiches[i])

# ls = [1,2,3,4,5]
# print(ls[1:4:2])


# for i in range(11, 6, -2):
#     print(i)


# for i in range(len(sandwiches)-1, -1, -1):
#     print(i, sandwiches[i])
#
# for sandwich in sandwiches:
#     print(sandwich)


# print(list(enumerate(sandwiches)))

# for idx, ele in enumerate(sandwiches):
    # print(idx, ele)

# print(dir(enumerate(sandwiches)))

def difference(ls):
    mini = ls[0]
    maxi = ls[0]
    for i in range(len(ls)):
        if ls[i] < mini:
            mini = ls[i]
        if ls[i] > maxi:
            maxi = ls[i]
    return maxi - mini

# print(difference([10, 15, 20, 2, 10, 6]))
# # 20 - 2 = 18
#
# print(difference([-3, 4, -9, -1, -2, 15]))
# # 15 - (-9) = 24
#
# print(difference([4, 17, 12, 2, 10, 2]))
# # 17 - 2 = 15

def factorial(n):
    prod = 1
    for i in range(1, n+1, 1):
        prod *= i
    return prod

# print(factorial(1))     #> 1
# print(factorial(8))     #> 40320
# print(factorial(12))    #> 479001600

# Dictionaries

# let obj = { hello: "world", 4: "four" };
# console.log(obj.4);

hello = "hello"

my_dict = { "hello": "world" }
# print(my_dict[hello])
# print(my_dict.hello)

# print(dir(my_dict))
# print(my_dict.keys())

crazy_dict = {
    "hello": "world",
    5: "five",
    None: "none",
    True: "wow!",
    (1,2,3,4): [1,2,3,4],
    factorial: 4
}

# print(crazy_dict[factorial])

weird_dict = dict([(5, "ive"),(None, None)])

# print(weird_dict)

# print(crazy_dict[False])
# print(crazy_dict.get(False))


crazy_dict["new key"] = "new value"
# print(crazy_dict)

crazy_dict["new key"] = factorial

# del crazy_dict["new key"]
# print(crazy_dict)

def show_some_values(*args, a, **kwargs):
    print(a)
    print(args)
    print(kwargs)

# show_some_values(1,2,3,4,5,6,7,8,9,10,(1,2,2,2), a=10, gorp="gorp", mark=6)
#

def new_function(x,y,z):
    print(x)
    print(y)
    print(z)


new_dict = { "x": 1, "y": 2}
# new_function(**new_dict)
# new_function(1,2,3)

# new_function(5, z=100, y=6)

def merge_lists(ls1, ls2):
    new_dict = {}
    for idx in range(len(ls1)):
        new_dict[ls1[idx]] = ls2[idx]
    return new_dict

lst1 = ['a', 'b']
lst2 = [1, 2]
merged_dict = merge_lists(lst1, lst2)
# print(merged_dict)      # { 'a': 1, 'b': 2 }

def majority_char(chars):
    total_chars = len(chars)
    char_count = {}
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        if char_count[char] > (total_chars / 2):
            return char
    return None


str1 = 'all'
str2 = 'welcome to the jungle'

# print(majority_char(str1))           # 'l'
# print(majority_char(str2))          # None


# SETS

my_set = set([1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,6])
# print(my_set)

my_set.add(7)

# print(my_set)

# print(my_set[0])

simple_set = { 1,2,3,4,5,6,6,6,6,6,6 }
# print(simple_set)

empty_set = set()
# print(type(empty_set))

# list_set = {[1,2,3], 5, 3, 3,4}
# print(list_set)

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {2,4,6,8,10,12,14,16,18,20}

# print(set1 & set2)
# print(set1.intersection(set2))

# print(set1 | set2)
# print(set2.union(set1))

# print(set1 ^ set2)
# print((set1 - set2) | (set2 - set1))

# print(set1 - set2)
# print(set2 - set1)

def check_binary(chars):
    valid_bins = { "1", "0" }
    # return set(chars).issubset(valid_bins)
    return set(chars) == {"1", "0"} or set(chars) == {"1"} or set(chars) == {"0"} or set(chars) == set()


str1 = '1010001010010100101'
str2 = '1010010015010101010'

# print(check_binary(str1))       # True
# print(check_binary(str2))       # False

# BUILT-INS

ls = [1,2,3,4]
# print(dir(ls))
# print(len(ls))
# print(dir(5))
# print(len(5))

# print(ls.__len__())

# new_tup = ("brad", "David", "Andrew")
# sorted_ls = sorted(new_tup, key=str.upper, reverse=True)
# print(sorted_ls)


ls_bools = [ False, True, False, False, False]
ls_again = [0, None, tuple(), False]
more_ls = [True, 5, -9, (1,2,3), "extra"]

# print(all(more_ls))


# print(tuple(filter(lambda x: True, sandwiches)))

# print(list(map(lambda x: x + "wubbbba", sandwiches)))

# print(dict(zip(ls_again, more_ls)))
# print(dict(zip(ls_bools, more_ls)))

my_dict = {}
my_dict[False] = True
my_dict[False] = "extra"

# COMPREHENSIONS

normal_ls = []

for i in range(10):
    normal_ls.append(i)

# print(normal_ls)

ls_comp = [i for i in normal_ls]
# print(ls_comp is normal_ls)

evens = [i for i in normal_ls if i % 2 == 0]
# print(evens)

squared_odds = [ i ** 2 if i < 6 else None for i in normal_ls if i % 2 != 0]
# print(squared_odds)
#
# print([9 for i in normal_ls])

nums = [-5, 11, 10, 14]
def map_func(x):
    return x * 2 + 1

# print([map_func(num) for num in nums])

nums = [-5, 11, 10, 14]

# print([num for num in nums if num > 0])

# [expression for ele in iterable if expression]

my_first_dict_comp = { ele: ele * 2 for ele in normal_ls }
# print(my_first_dict_comp)

# print({idx: val for idx, val in enumerate(normal_ls)})

# DECORATORS

from datetime import datetime
from time import sleep

def timer(cb):
    def wrapper(*args, **kwargs):
        if kwargs.get("skip"):
            return cb(*args, **kwargs)
        print(kwargs)
        start_time = datetime.now()
        val = cb(*args, **kwargs)
        end_time = datetime.now()
        total_time = end_time - start_time
        print(f"{cb.__name__}{*args, kwargs} finished in {total_time} seconds!")
        return val
    return wrapper


# this decorator does not work well with recursive functions
# because the decorator fires every time the function calls itself
@timer
def recursive_fib(n, memo = {}, skip=0):
    print(memo)
    if n <= 2:
        return 1
    else:
        if n-1 not in memo:
            memo[n-1] = recursive_fib(n-1, skip=True)
        if n-2 not in memo:
            memo[n-2] = recursive_fib(n-2, skip=True)
        print(memo)
        return memo[n-1] + memo[n-2]

@timer
def print_list(ls, time):
    for i in range(time * 90909090):
        continue
    return ls


# timed_fib = timer(recursive_fib)

# print(timed_fib(30))

start_time = datetime.now()
# print(recursive_fib(34))
# print(recursive_fib(35))
print(recursive_fib(36))
end_time = datetime.now()
print(end_time - start_time)

# print(print_list([1,2,3,4,5], 5))
