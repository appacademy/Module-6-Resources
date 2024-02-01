### Tuples

my_tup = (1,2,3,4)
quick_tup = 1,2,3,4,        5

# print(type((1,2,3,4)))
# print(type(quick_tup))


my_tup += 5,6,7

# my_tup[0] = 5 # cannot alter an element in place

# my_tup += 8 # will not work
my_tup += 8,

my_tup = 1,2,3,4,5,6,7,8
my_tup = "i'm now a string"

# print(my_tup)


not_a_tup = (1) # this is an integer, the parenethesis serve only as grouping mechanisms

empty_tup = ()

# print(type(empty_tup))

another_empty_tup = tuple()

# print(another_empty_tup)


# ls = [3,4,62,4,823,4]
#
# ls.sort()

# tuple reassignment versus list appending
# my_tup = 1,2,3
# print("tuple address before reassigning:  ", id(my_tup))
# my_tup += 4, # note that we are using the assignment operator
# print("tuple address after reassigning:   ", id(my_tup))
# print()
#
# ls = []
# print("list address before appending:     ", id(ls))
# ls.append(1) # the append method mutates the list in place
# print("list address after appending:      ", id(ls))

sorted_obj = sorted((5,8,3,5,90,34,4,2,90,5))

# print(tuple(sorted_obj))

### RANGES

simple_range = range(10)

odds_backwards = range(21, 0, -2)

# for num in simple_range:
#     print(num)

# for num in odds_backwards:
#     print(num)

ls_for_range = [3,4,62,4,823,4]

ls_range = range(6)

# print(ls_range)

# for i in range(len(ls_for_range)):
#     print(i, ls_for_range[i])

counting_numbers = list(range(100))

# print(counting_numbers)

enumerate_obj = enumerate(ls_for_range)

# print(enumerate_obj)

enumerated_ls = list(enumerate_obj)

# print(enumerated_ls)
# print(ls_for_range)

for idx, ele in enumerate(ls_for_range):
    # print(idx, ele)
    # ele = 0
    ls_for_range[idx] = 0

# print(ls_for_range)

### DICTIONARIES

crazy_dict = { 1: 1, "string": "value", (1,2): "tuple", False: "boolean", None: None }

crazy_dict[9] = "new_value"

# crazy_dict.string # won't work with dicitonaries

# print(crazy_dict)

# print(crazy_dict[False])
# print(crazy_dict["not here"])

# print(crazy_dict.get("not here", "your key is not in the dictionary"))

# new_obj = { "new": "object" }

# newobj.new

# print(crazy_dict[1,2])

# del  crazy_dict[1,2]
crazy_dict[1,2] = "new tuple value"

# print(crazy_dict)

def concatenate_dictionaries(lst):
    new_dict = {}
    for dic in lst:
      for key in dic.keys():
        new_dict[key] = dic[key]
    return new_dict

def concatenate_dicationaries(ls):
    pass
    
### SETS

my_set = {1,1,2,2,3,4,5,6,7,6,6,5,4, "hello", "hello"}

# print(my_set)

empty_set = set()

redundant_ls = [1,1,1,1,1,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5,5,]

unique_elements = set(redundant_ls)

# print(unique_elements)

set1 = {1,3,5,7,9,11,13,15,17,19}

set2 = {1,2,3,4,5,6,7,8,9,10}


# print(set1 | set2)
# print(set1.union(set2))
#
# print(set1 & set2)
# print(set1.intersection(set2))

# print(set1 - set2)
# print(set2 - set1)
# print(set1.difference(set2))

# print(set1 ^ set2)

empty_set.add(1)

# print(empty_set)

def remove_repeats(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    return set1 - set2 | set2 - set1

str1 = 'aloha'
str2 = 'bonjour'


# print(remove_repeats(str1, str2)) 

### BUILT INS

ls = ["david", "andrew", "BRAD", "Keegan"]

sorted_names = sorted(ls, key=str.upper, reverse=True)
# print(sorted_names)

ls = [1,2,3,4,5]
# print(sorted(ls, key=lambda x: -x))

ls1 = [False, False, False, True]
ls2 = [True, True, True, True]
ls3 = [False, False, False, False]
ls4 = []

# print(any(ls1))
# print(any(ls2))
# print(any(ls3))

# print(all(ls1))
# print(all(ls2))
# print(all(ls3))

# print(any(ls4))
# print(all(ls4))

ls = ["david", "andrew", "BRAD", "Keegan"]

filtered_list = list(filter(lambda x: x.lower() < "f", ls))

# print(filtered_list)

# print(set(filtered_list))

# print(dict([ [1, "hello"], ["threee", 3]]))

# print(dict(enumerate(ls)))

# for x in filtered_list:
#     print(x)

nums = [1,2,3,4,5,6,7,8,9]

sq_nums = tuple(map(lambda x: x ** 2, nums))
# print(sq_nums)

scores = [90, 86, 75, 91, 62, 99, 88, 90]
grades = ["A", "B", "C", "A", "D", "A", "B", "A"]

combined_lists = zip(scores, grades)
# print(dict(combined_lists))

### COMPREHENSIONS

comp_ls = [ num for num in range(10) ]

for_ls = []
for num in range(10):
    for_ls.append(num)

# print(comp_ls)
# print(for_ls)

def square_num(num):
    return num ** 2

squares = [square_num(num) for num in range(1,10)]

zeroes = [0 for num in range(1,10)]

# print(squares)

# print(zeroes)

zeroes_n_odds = [0 if num % 2 == 0 else num for num in range(1,10)]

# print(zeroes_n_odds)

odds = [num for num in zeroes_n_odds if num != 0]

squared_odds = [num**2 for num in zeroes_n_odds if num != 0]

# print(squared_odds)
# print(odds)



scores = [90, 86, 75, 91, 62, 99, 88, 90]
grades = ["A", "B", "C", "A", "D", "A", "B", "A"]


grades_n_scores = { key: value for key, value in zip(scores, grades) }

# print(grades_n_scores)
#
nums_all = { num: num**2 for num in scores if num >= 90 }
# print(nums_all)

# [ expression for element in iterable (optional) if conditional]
