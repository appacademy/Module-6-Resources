# XOR

# print(True or False)

# print(True ^ True)
# print(False ^ False)
# print(True ^ False)
# print(False ^ True)

# IF STATEMENTS

def breakfast(food):
    """accepts a breakfast food as a string an returns 
    how we feel about said food """
    if food == 'waffles':
        print(f'{food} are my favorite breakfast!')
    elif food == 'pancakes':
        print(f"{food} are a pretty good second to waffles")
    else:
        print(f'{food}!?!?  That is not a great breakfast!')


# breakfast("waffles")
# breakfast('pancakes')
# breakfast('potato chips')

# XOR PROBLEM

def xor(val1, val2):
    return val1 ^ val2


# print(xor(False, False))   #>  False
# print(xor(True, False))   #>  True
# print(xor(True, True)) #>  False
# print(xor(5, 3))  #> 6
# print(xor(8, 4))  #> 12
# print(xor(2, 2))  #> 0
# print(xor(1, 2))  #> 3
# print(xor(4, 4))  #> 0
# print(bin(True))
# print(bin(False))
# 0b1
# 0b1
# print(bin(5))
# print(bin(3))
# # 0b101
# # 0b011
# # 0b110
# print(bin(6))

# STRINGS

lunch = "tacos"
long_string = """ THis is going to be
a great
super fantastic 
multi line string"""

# print(f'I am hoping to have {lunch} for lunch today!')
# print("I am hoping to have {} for lunch today!".format(lunch))

a = 'a'
b = 'b'
an = 'an'

# print(b + an)
# print(b + a * 7)

breakfast = 'waffles'
# print(breakfast[-2])
# print(breakfast[::2])

# print(breakfast.index('af'))
# print(breakfast.count('q'))
# print(breakfast.split('a'))

instructors = ["Brad", "John", "Cesar", "David"]
join_str = ', '
# print(join_str.join(instructors))
# print(list(breakfast))

# print("waffles".upper())

# REVERSE BINARY
# print(bin(5)) # -> 0b101
# print(int('0b101', 2))


# Write your function, here.
def is_palindrome(str):
#   reverse = ''.join(reversed(str))
  reverse = str[::-1]

  return str == reverse



# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False


def recursive_string(string):  # input - "civic"
  if len(string) == 0:
    return string
    # if string == "waffles":
    #     # do our logic here
    #     pass

  return recursive_string(string[1:]) + string[0]
#                           "ivic"  "c"
#                             "vic" "i"  "c"
#                               "ic" "v"  "i"  "c"
#                               "c" "i"  "v" "i" "c"
#                               "" "c" "i"  "v" "i" "c"

# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) # noitacilppa



# NUMBERS
# print(int("123455"))

# print(4 / 2)
# print(4 // 2)

val = 5
# print(val)
# val += 1
# print(val)


my_int = 4
my_float = 4.0
 
# check if the values are the same
# print(my_int == my_float)  # True
 
# check if the values are the same and check type
# print(my_int == my_float and isinstance(my_int, float))
# print(my_int is my_float)

list_1 = [1,2,3]
list_2 = list_1

# print(list_1 == list_2) 
# print(list_1 is list_2) 
# print(id(list_1))
# print(id(list_2))

# STATEMENTS

# i = 0

# while i < 5:
#     if i == 3:
#         print(i, "We have a 3!" )
#     else:
#         print(i, "Nope not a 3")
#     i += 1


# i = 0
# while True:
#     print(f"{i}. Hello, world.")
#     if i < 4:
#         i += 1
#         continue
#     print("You've printed 5 times. Goodbye.")
#     break


foods = ['pizza', 'taco', 'waffle', 'salad']

# for food in foods:
#     print(food)

# print(user in post_likes)

# my_nums = range(4, -1, -1)
# # print(list(my_nums))

# for index in range(0, len(foods)):
#     print(index, foods[index])


# num = 0
# try:
#     print("In the try block")
#     print(4/num)

# except ZeroDivisionError:
#     print("Dividing by zero is bad!")

# except TypeError:
#     print("We can't do math with non numbers!")

# else: 
#     print("Our try block must have worked great if we see this")

# finally:
#     print("I am going to print stuff no matter what, you can't stop me!!!")


# SEQUENCE OF NUMBERS
# # Problem 6 - Sequence of Numbers
# # Write your function, here.

def seq_of_numbers(seq):
# iterate through the string
# counter variable
# result/response variable
# conditionals 
    seq += ' '
    count = 1
    results = ''
    index = 0

    while index < len(seq)-1:
        if seq[index] != seq[index + 1]:
            results= results + str(count) + seq[index] + ','
            count = 1
        else: 
            count += 1

        index += 1

    return results


# print(seq_of_numbers("1211"))
# # This is "one 1, one 2, two 1s"
# # Prints "11,12,21"
# # 111221

# print(seq_of_numbers("111221"))
# # This is "three 1s, two 2s, and one 1"
# # Prints "31,22,11"

# print(seq_of_numbers("31131211131221"))
# This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
#    one 3, one 1, two 2s, and one 1"
# Prints "13,21,13,11,12,31,13,11,22,11"


# FUNCTIONS
def is_even(num):
    """function that takes in a number and lets 
    us know if it is even or not """
    return num % 2 == 0

# print("regular results", is_even(6))

# even = lambda num: num % 2 == 0

# print("lambda result", even(6))

# times_two = lambda num: num * 2

# multiply = lambda num_1, num_2: num_1 * num_2

# print(multiply(10, 4))


# SCOPING
# y = 200
# print("Y global first time", y)

# def brads_func():
#     global y
#     print("First print", y)
#     y += 5
#     print("Second print", y)

# brads_func()
# print("Y in global second time", y)


# def my_funct(num_1, num_2, num_3 = 5, *args, **kwargs):
#     print(num_1, num_2, num_3)
#     print("args", args)
#     print("kwargs", kwargs)


# my_funct(4, 7, 6, 8, 9, 231, num_7 = 43, num_8 = -8743)

# Write a function string_multi_print that accepts 
# a string, str, and returns a lambda that prints 
# str i times.

# def string_multi_print(str):        # Prints 1 concatenated string
#     return lambda i : print(str * i)

# string_multi_print('hello ')(2)  # Prints "hello hello "
# string_multi_print('wahoo ')(3)  # Prints "wahoo wahoo wahoo "

# LISTS
foods = ["tacos", "wings", "salad", "steak", "bacon"]

# print(foods)
# # print(foods[:3])
# # print(len(foods))
# foods.append("steak")
# print(foods)
# foods.extend(["cheesesteak", "hamburger"])
# print(foods)
# foods.insert(0, "fries")
# print(foods)
# foods[2] = 'chicken'
# print(foods)
# foods.remove('steak')
# foods.remove('steak')
# print(foods)

vals = [2, 4, 56, 12, 7]

print(vals)
vals.sort()
print(vals)
print("sum:", sum(vals))
print("min:", min(vals))
print("max:", max(vals))