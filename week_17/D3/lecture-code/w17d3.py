king = ("Brad",)
minions = "david", "andrew"

teachers = king + minions

# print(teachers)
empty_tuple = ()

# print(dir(teachers))

# elements are converted to lower case before comparison, and
# the final result is returned in reverse order
sorted_teachers = sorted(teachers, key=str.lower, reverse=True)

# print(sorted_teachers)

ls_1 = [(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)]
ls_2 = [(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)]

[2, 8, 5, 0]

def index_sort(tups):
  return sorted(tups, key=lambda x: x[1])

# print(index_sort(ls_1))
# print(index_sort(ls_2))

tup_1 = ((58, 1, 5), (0, 3), (45, ), (24, 23))

def fill_tuple(tups, val, length):
  ls = []
  for tup in tups:
    ls.append(tup + (val,) * (length - len(tup)))
  return tuple(ls)

# print(fill_tuple(tup_1, 2, 3))

ls = [1,2,3,4]

# for el in ls:
#   print(el)


# print(list(range(20, 5, -2)))

# # print(list(range(10)))

# for idx in range(len(ls)):
#   print("index:   ", idx)
#   print("element: ", ls[idx])

# for idx, element in enumerate(teachers):
#   print(f"teacher at {idx} is {element}")

# print(list(enumerate(teachers)))

meals = {
  "breakfast": "eggs",
  "lunch": "ice cream",
  "dinner": "tamales"
}

random = {
  (1,2,4): ["spork", "grand"],
  5: "five",
  False: True,
  "False": "this is a different kv pair",
  "nested": { 5: 5}
}

random[False] = False
# print(random)

del random[False]

# print(random)

# random[False]
# random["False"]
# random[5]

new_dict = dict(this="is", a="valid", dictionary="!")

# print(new_dict["this"])

# print(dir(new_dict))

# print(list(new_dict.keys()))
# print(list(new_dict.values()))

# def give_me_anything(*nums, **kwargs):
#   # print(nums)
#   print(hello="there", whats="up")
#   for num in nums:
#     print(num)
  
my_dict = {
  "hello": "there",
  "whats": "up"
}

# give_me_anything(1,3,4,5, **my_dict)

tups = "b", "c", "A", "D"

values = {
  "key": str.lower,
  "reverse": True,
  9: "nine"
}

# for xx in values:
#   print(xx)

# print(sorted(tups, **values))

my_set = set()

# print(my_set)

# print(set(values))

ls = [1,1,1,1,2,2,2,3,3,3,4,4,4,4,4,5,5,5,5]

# print(set(ls))

word = "mississippi"

# print(set(word))

# set_1 = {2, 3, 5, 7, 11, 13, 17, 19}
# set_2 = { 2, 4, 6, 8, 10, 12, 14, 16, 18}

# print(set_1 | set_2)

# print(set_1 & set_2)

set_1 = {1, 2, 3, 4, 5, 7}
set_2 = {3, 4, 7, 9, 10}

# print(set_2 - set_1)
# print(set_1 - set_2)
# print(set_1 ^ set_2)

# print((set_2 - set_1) | (set_1 - set_2))
str1 = '1010001010010100101'
str2 = '1010010015010101010'
def check_binary(bin_str):
  converted_bin = set(bin_str)
  valid_bins = [{'1', '0'}, {'1'}, {'0'}, {''}]
  return converted_bin in valid_bins
  # return converted_bin.issubset({"0", "1"})

# print(check_binary(str1))
# print(check_binary(str2))

# print(help())

empty_ls = []
ls = [True, True, False, True]

# print(any(ls))
# print(all(ls))

first_ten = {1,2,3,4,5,6}
first_ten_letters = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# print(list(filter(lambda x: x % 2 == 0, first_ten)))
# print(list(map(lambda x: x ** 2, first_ten)))

combined = zip(first_ten_letters, first_ten)
# print(dict(combined))

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

def get_unique_models(phones):
  unique_phones = []
  models = set()
  # unique = True
  for phone in phones:
    # for unique_phone in unique_phones:
    #   if unique_phone["model"] == phone["model"]:
    #     unique = False
    # if unique:
    #   unique_phones.append(phone)
    if phone["model"] not in models:
      unique_phones.append(phone)
    models.add(phone["model"])
  return unique_phones
  # return models

# Don't code like this:
# def get_unique_models(phone_list):
#     seen = []
#     return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)
  
# print(list(get_unique_models(phones)))
    
pre_comp_ls = [1,2,3,4,5,6,7,8,9]
# comp_ls = [ element for element in pre_comp_ls ]
# comp_ls = [element * 2 if element > 5 else None for element in pre_comp_ls if element % 2 != 0]
comp_ls =[element for element in pre_comp_ls if element % 2 == 0]

# print(comp_ls)

for_ls = []
for element in pre_comp_ls:
  if element % 2 == 0:
    for_ls.append(element * 2)

nums = [-5, 11, 10, 14]
    
# print([num * 2 + 1 for num in nums])

# print([num > 0 for num in nums])

# print([num for num in nums if num > 0])

keys =  [1,2,3,4]
values= ["one", "two", "three", "four"]

print({key: value for key, value in zip(keys, values)})
