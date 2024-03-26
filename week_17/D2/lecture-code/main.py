true = True
false = False

# print(isinstance(false, bool))


# print(isinstance(1, bool))

# print(bool(0))
# print(bool(1))
#
# print(bool(-1))
#
# if bool(1):
#     print("one is truthy")
#
# if "":
#     print("empty strings are falsey")
#
# if []:
#     print("empty lists are falsey")

# List of falsey values:
# False
# 0 of any data type:
#   0
#   0.0
#   0j + 0
# empty collections
# None

# print(None == False) # False
# print(bool(None) == bool(False)) # True
# print(None == None) # True
# print(0 == 0.0) # True
# console.log("0" == 0);
# print(1 == 1.0) # True
# print(1 == 0j + 1) # True
# print(1 == 1j + 0) # False
# print("1" == 1) # False

# print(int("1") == 1) # True

# print("alpaca" > "ant")

# print("ant" > "anteater")

# print("A".casefold() == "a".casefold())

# print(False < True)

# print(False ^ False)
# print(True ^ False)
# print(False ^ True)
# print(True ^ True)

# print(15 ^ 5)
# print(bin(15))
# print(bin(5))

# print(True and True) # True
# print(True and False) # False
# print(1 or True)# 1
# print(10 or 0) # 10
# print(0 and 10) # 0

# print("hello" or True) # hello


# print(not "")

# print(True and not (True or False))

a = 6
b = 20

# if b < a:
#     print("b is less than a")
# elif b == a:
#     print("b is equal to a")
# else:
#     print("b is greater than a")
#     if b == 20:
#         print("twenty is a pretty good number")
#     elif a == 6:
#         print("6 is good too, but we'll never know, because this won't be printed out")

def xor(val1, val2):
    return val1 ^ val2

# print(xor(False, False))   #>  False
# print(xor(True, False))   #>  True
# print(xor(True, True)) #>  False
# print(bin(5))
# print(bin(3))
# print(bin(6))
# 101
# 011
# 110
# print(xor(5, 3))  #> 6
# 1000
# 0100
# 1100
# print(xor(8, 4))  #> 12
# print(xor(2, 2))  #> 0
# print(xor(1, 2))  #> 3
# print(xor(4, 4))  #> 0

def de_morgans_law(val1, val2):
    # return not (val1 and val2)
    # return not val1 or not val2
    # return not (val1 or val2)
    return not val1 and not val2


# print(de_morgans_law(True, True)) # False
# print(de_morgans_law(True, False)) # True
# print(de_morgans_law(False, False)) # True
# print(de_morgans_law("", [])) # True
# print(de_morgans_law(2, 2)) # False
# print(de_morgans_law(2, 0)) # True

def multiline_comment():
    """
    this is a docstring
    """
    return None

my_str = 'hello'
my_str_with_quotes = '"hello"'
my_str_double_quotes = "hello"
my_str_multiline = '''
hello
"





'''


# print(my_str)
# print(my_str_with_quotes)
# print(my_str_double_quotes)
# print(my_str_multiline)


teachers = ["Andrew", "David"]

# print(f"There are {len(teachers)} teachers in Module six!!!")

# print("There are {0} teachers in Mod 6!".format(len(teachers)))

a = "a"
b = "b"
an = "an"

# print(b + 9*an + a)

# print("$1" + ',000'*3)

food = "Spaghetti"

# print(food[0])
# print(food[-1])
# print(food[-10])
# print(food[9])

# print(food[0:5])
# print(food[0:-5])
# print(food[-5:-3])

# print(food[8:1:-1])

# print(food[-1::-1])

# print(help(str))

# print("aaaaabbbdjjjdbbdsbsdfgjjdsfsdaaa".count("aa")) # 8
# print("aaaaabbbdjjjdbbdsbsdfgjjdsfsdaaa".count("a")) # 3
# print("peanut peanut peanut peanut".count("peanut")) # 4

# print("the quick brown fox jumps over the lazy dog".index("fox"))
# print("the quick brown fox jumps over the lazy dog".index("k"))
# print("the quick brown fox jumps over the lazy dog".index("o"))


def look_for_words(search_str, str1, str2):
    return search_str.count(str1) + search_str.count(str2)

# print(look_for_words("the coyote is very very very hungry for a coyote", "coyote", "very"))

# print("the air is very dirty where i'm from".split(" "))
#
# print(" ".join(["i", "am", "very", "excited"]))
#
# print("hello there".upper())
#
# print("what's going on".title())
#
#
# print("the wild hogs are approaching...".capitalize())

# help(str.capwords)

# import string

# print(help(string))

# print(string.capwords("what's going on"))

# Write your function, here.
def recursive_string(word):
  if word == "":
    return word
  # return word[-1] + recursive_string(word[0:-1])
  return recursive_string(word[1:]) + word[0]

# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) # noitacilppa

# print(10 **2)

def long_division(num, div):
    return num // div, num % div


# print(long_division(100, 30))


# print(3/-1) # -3.0
# print(3//-1) # -3

x = 15

# x -= 15 # x = x - 15 # 0
# x **= 2 # x = x ** 2 # 225
# x %= 4 # x = x % 4 # 3
# x //= 3 # x = x // 3 # 1
# x *= 5 # x = x * 5 # 75
# print(x)

def recursive_countdown(num):
    print(num, end=' ')

    if num > 1:
        recursive_countdown(num - 1)

# recursive_countdown(10)

x = 0
y = 0

# print(x == y)
# print(x is y)

name = "David Nash"
full_name = "David Nash"

# print(name is full_name)

ls1 = [1,2,3,4,5]
ls2 = [1,2,3,5,4]

# print(ls1 == ls2)
# print(ls1 is ls2)

# print(id(ls1))
# print(id(ls2))

a = "hello world"
b = "hello world"

# print(a is b)

# print(id(a))
# print(id(b))

one = 1
one_point_zero = 1.0

# print(one is one_point_zero)

ls3 = ls1

ls3[0] = 500

# print(ls1)


# print(ls3 is ls1)

none = None
nothing = None

# print(none is nothing)

# print(0 is None) # False

ls4 = [ *ls1 ]

# print(ls1 is ls4)

# print(ls4)

hello = "hello "
world = "world"
hello_world = hello + world

# print(hello + world == hello_world)
# print(hello + world is hello_world)

def first_before_second(word, char1, char2):
    return word.rindex(char1) < word.index(char2)

# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#> True
# Every instance of "a" occurs before every instance of "j".

# print(first_before_second("knaves knew about waterfalls", "k", "w"))
#> True

# print(first_before_second("happy birthday", "a", "y"))
#> False
# The "a" in "birthday" occurs after the "y" in "happy".

# print(first_before_second("precarious kangaroos", "k", "a"))

def say_hello_n_times(n):
    i = 1
    while i <= n:
        print(f"{i}. Hello, world.")
        i += 1

# say_hello_n_times(10)


items = ["a", "b", "c", "c"]
# for item in items:
#     print(item)
#     print(items.index(item)) # won't give us every index

# for i in range(len(items)):
#     print(i, items[i])

# for idx, el in enumerate(items):
#     print(idx, el)
#     el = 5 # doesn't mutate list
    # items[idx] = 5 # mutates the list

# print(items)

# print("a" in items)

# print("a" in "almonds")

prompt = True
#
# while prompt is not None:
#     prompt = input("Give me a number!!!! ")
#     if prompt == "0":
#         break
#     try:
#         prompt = int(prompt)
#     except ValueError:
#         print("That's not a number!")
#         continue
#     if prompt > 10:
#         print("That number is too big!")
#         continue
#     print("That's a pretty good number!")

# try:
#     # print(bad)
#     bad = 5 / 0
# except ZeroDivisionError as e:
#     print("You can't divide by zero, you mad person.")

# while True:
#     try:
#         num = int(input("say a number "))
#         print(int(num))
#         break
#     except ValueError: # without a specific error, it can even prevent a KeyboardInterrupt
#         print("try again")

x = "1"

# try:
#     y = 5 // x
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print(y)
# finally:
#     print("that was fun")


def is_valid_hex_code(hex_str):
    valid_chars = "0123456789ABCDEF"
    if hex_str[0] != "#":
        return False
    for char in hex_str[1:]:
        if char.upper() in valid_chars:
            continue
        return False
    if len(hex_str) == 7:
        return True
    return False

# print(is_valid_hex_code("#CD5C5C")) #> True
# print(is_valid_hex_code("#EAECEE")) #> True
# print(is_valid_hex_code("#eaecee")) #> True
#
# print(is_valid_hex_code("#CD5C58C"))
# # Prints False
# # Length exceeds 6
#
# print(is_valid_hex_code("#CD5C5Z"))
# # Prints False
# # Not all alphabetic characters in A-F
#
# print(is_valid_hex_code("#CD5C&C"))
# # Prints false
# # Contains unacceptable character
#
# print(is_valid_hex_code("CD5C5C"))
# Prints False
# Missing #

bad_func = lambda x: "you should not define a function this way!!!!"

# print(bad_func(6))

def not_ready():
    pass

ls = [1,2,3,4,5]

squared_ls = list(map(lambda ele: ele ** 2, ls))

# print(squared_ls)

y = 0

def make_a_five():
    y = 5 # is not the same y
    return y

def make_a_six():
    global y
    y = 6 # this is the same y
    return y

# x = make_a_five()
# print(x)
# print(y)

x = make_a_six()
# print(x)
# print(y)

if True:
    x = 5

# print(x)




