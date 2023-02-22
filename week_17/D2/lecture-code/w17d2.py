# XOR

# print(True ^ True)
# print(True ^ False)
# print(False ^ False)
# print(False ^ True)

# IF BLOCKS

def breakfast(food):
    if food == "waffles":
        print(f"{food} is my favorite breakfast")
    elif food == 'pancakes':
        print(f"{food} are a pretty good choice too")
    else:
        print("Thats a nice choice, but not waffles")


# breakfast("waffles")
# breakfast("pancakes")
# breakfast("cereal")

# XOR problem
# Create a function that returns the xor result of two values.
# Write your function, here.
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
# print(bin(5))
# print(bin(3))
# # 0b101
# # 0b011
# #   110
# print(bin(6))
# 0b110


# STRING
# greeting = "Let's say 'Hello!'"
# multi_line= '''This is a multi
# line string that will 
# preserve spaces and new lines'''

# # print(multi_line)

# meal = "lunch"
# food = "tacos"
# # print(f'We are having {food} for {meal}!')

# a = "a"
# b = 'b'
# an = 'an'

# print(b + an)
# print(b + a * 7)
# print(b + an * 2 + a)

# iterable[start:stop:step]
# iterable[0:-1:1]

# start = 1
# stop = 3

# food = "pizza is yum yum delicious!"
# print(food[start:stop])

# print(food.index('iz'))
# # print(food.index('w'))
# print(food.find('w'))
# print(food.count("z"))
# print(food.split("z"))
# print(list(food))

# foods = ["pizza", "wings", "tacos"]
# print(", ".join(foods))

# print(food.upper())
# print(len(food))
# print(len(foods))

# Is Palindrome
# Write your function, here.
def is_palindrome(string):
    return string == string[::-1]

#   reversed_lst = reversed(str)
#   print(list(reversed_lst))
#   reverse = ''.join(reversed_lst)
#   print(reverse)
#   return str == reverse

# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False


# Recursive String
def recursive_string(string):
    if len(string) == 0:
        return string
    
    return recursive_string(string[1:]) + string[0]     
    #                   "ivic"              "c"
    # 2nd               "vic"     +      "i"
    # 3rd               "ic"    +     "v"
    # 4th                "c"   +   "i"
    # 5th                ""    +   "c"
    # 6th "" 
 

# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) # noitacilppa

# NUMBERS
# print(10 / 2)
# print(10 // 2)

# num = 1
# num += 1 

# print(1 == 3)
# print("taco" != "wing")

# print(True == 1)
# print(True is 1)
# print(id(True))

num = 1
# print(id(num))
# another_num = 1
# print(id(another_num))
# yet_another_num = 2
# print(id(yet_another_num))


# First before Second 
# # You are given three inputs: a string, one letter, and a
# second letter.
# Write a function that returns True if every instance of the 
# first letter  occurs before every instance of the second 
# letter.
# Look at the String Methods to possibly help you find some 
# methods that can make this easier.
# Write your function, here.
def first_before_second(string, char_1, char_2):
    return string.rindex(char_1) < string.index(char_2)


# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# #> True  Every instance of "a" occurs before every instance of "j".
# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# #> True
# print(first_before_second("happy birthday", "a", "y"))
# #> False  The "a" in "birthday" occurs after the "y" in "happy".
# print(first_before_second("precarious kangaroos", "k", "a"))
# #> False


# WHILE LOOPS

# index = 0

# while index < 5:
#     if index == 3:
#         print(index, "We have got a 3!")
#     else:
#         print(index)
#     index += 1

# index = 0 

# while True:
#     if index < 4:
#         print(index, "How's it going?")
#         index += 1
#         continue
#     print("Our index is now more than 4")
#     break

import random 
import time
import os 

# count = 99

# while count < 1000:
#     os.system("clear")
#     print(f"{count} little bugs in our code...")
#     time.sleep(1)
#     print(f"{count} pesky little bugs...")
#     time.sleep(1)
#     print("Take one down and patch it around...")
#     time.sleep(1)
#     new_bugs = random.randint(1, 50)
#     count += new_bugs
#     print(f"{count} little bugs in our code!")
#     time.sleep(1)


# FOR LOOPS
dinner = ["Tacos", "Salad", "Wings", "Pizza", "Burger"]

# for food in dinner:
#     print(food)


# print("Pizza" in dinner)
# print("Pasta" in dinner)

# test_range = range(start,stop,step)
# test_range = range(0, 21, 2)
# print(list(test_range))

# for index in range(0, len(dinner)):
#     print(index, dinner[index])

# TRY / Except

# num = "waffles"

# try:
#     print("In the try block")
#     print(4/num)

# except ZeroDivisionError:
#     print("we can not divide numbers by zero!")

# except TypeError:
#     print("we can not do math with strings")

# else:
#     print("this should only print if our try succeeds")

# finally:
#     print("We will always see this print")


# raise Exception("This is an error, you were naughty")



# Sequence of Numbers
# def seq_of_numbers(seq):
#     count = 1
#     index = 0
#     results = ''
#     seq += " "

#     while index < len(seq)-1:
#         if seq[index] != seq[index + 1]:
#             results = results + str(count) + seq[index] + ","
#             count = 1
#         else:
#             count += 1
#         index += 1
    
#     return results


# print(seq_of_numbers("1211"))
# # This is "one 1, one 2, two 1s"
# # Prints "11,12,21"

# print(seq_of_numbers("111221"))
# # This is "three 1s, two 2s, and one 1"
# # Prints "31,22,11"

# print(seq_of_numbers("31131211131221"))
# # This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
# #    one 3, one 1, two 2s, and one 1"
# # Prints "13,21,13,11,12,31,13,11,22,11"

# FUNCTIONS
def is_even(num):
    """Take in a number and return if it is even or not"""
    return num % 2 == 0


# print(is_even(7))
# print(is_even(8))

# LAMBDAS
# even = lambda num: num % 2 == 0

# print(even(7))
# print(even(8))

# multiply = lambda num_1, num_2: num_1 * num_2

# print(multiply(5, 10))

# def sum(num_1, num_2, num_3=15, *args, **kwargs):
#     total = num_1 + num_2 + num_3
#     print(args)
#     print(kwargs)
#     return total

# print(sum(5, 10, 30, 45, 50, num_6=60, num_7=65))

# SCOPE

# y = 2300

# def make_a_five():
#     """Demo for function scope"""
#     # y = 10
#     global y
#     y += 10
#     print(y, "inside function")
#     # print(y, "inside function - second time")

# make_a_five()

# print(y, "in global scope")


# LISTS
foods = ["Tacos", "Salad", "Wings", "Pizza", "Burger"]

# print(foods[1])
# print(foods[0:4])
# print(foods[::2])
# print(foods[::-1])
# print(len(foods))
# foods.append("Pasta")
# print(foods)
# foods.extend(["Sloppy Joe", "Fried Chicken"])
# print(foods)
# foods.insert(1, "Cake")
# print(foods)
# foods.remove("Salad")
# print(foods)
print(foods)
foods.pop(2)
print(foods)

vals = [56, 4, 123, 34, 2]
vals.sort()
print(vals)
print(sum(vals))
print(min(vals))
print(max(vals))