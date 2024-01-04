# XOR
# print(True ^ True)
# print(True ^ False)
# print(False ^ False)
# print(False ^ True)


# IF STATEMENTS

# def breakfast(food):
#     """take in a food as a string, and heavily judge 
#     your breakfast decisions"""
#     if food == "waffles":
#         print(f"{food.title()} is an excellent breakfast choice!")

#     elif food == 'pancakes':
#         print(f"{food.capitalize()} is a good choice for breakfast")

#     elif food == 'bacon':
#         print(f"{food.upper()} you win at breakfast!")

#     else:
#         print(f"{food} is an okay choice")
    

# breakfast('waffles')
# breakfast('pancakes')
# breakfast("bacon")
# breakfast("oatmeal")


# XOR 
# Write your function, here.
# def xor(val1, val2):
#     return val1 ^ val2


# print(xor(False, False))   #>  False
# print(xor(True, False))   #>  True
# print(xor(True, True)) #>  False
# # print(xor(5, 3))  #> 6
# # print(xor(8, 4))  #> 12
# # print(xor(2, 2))  #> 0
# # print(xor(1, 2))  #> 3
# # print(xor(4, 4))  #> 0
# print(bin(True))
# print(bin(False))
# # 0b1
# # 0b0
# print(bin(5))
# print(bin(3))
# #0b101
# #0b011
# #  110
# print(bin(6))

# STRINGs
# multi_line = '''this string
# can span 
# many many lines
# and preserves spaces

# '''

# print(len(multi_line))
# print(f"{multi_line.upper()} is a multi line string...")

# a = "a"
# b = "b"
# an = "an"
 
# print(b + an)
# print(b + a*7)
# print(b + an*2 + a)
 
# print("$1" + ",000"*3)


# food = "waffle"
# # print(food[-1])
# # print(food[start:stop:step])
# # print(food[:3])
# # print(food[2:])
# # print(food[::-1])

# def save_the_world_from_evil():
#     print('world is saved!')

# # print(food.index("af"))
# # print(food.find("q"))

# # # save_the_world_from_evil()
# # print(food.count('f'))
# print(food.split("f"))

# print(', '.join(["Brad", "David", "Andrew"]))

# # Problem 7 - IS Palindrome
# # Write your function, here.

def is_palindrome(string):
    reversed_string = string[::-1]
    print(reversed_string)
    return string == reversed_string

  

# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False



# Problem 7 - Recursive String
# Write your function, here.
# def recursive_string(string):
#     # base case
#     if len(string) == 0:
#         return string

#     # recursive case
#     return recursive_string(string[1:]) + string[0]

#                             #ivic     + c
#                             #vic + i
#                             #ic + v
#                             #c   + i
#                             #     



# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) # noitacilppa


# string = "pizza"


# NUMBERS
# result = 2 * (4 + 12)
# print(result)



# # Problem 3 - Perfect Square
# # Write your function, here.
# A perfect square is a positive integer that can be expressed 
# as the product of an integer by itself or as that integer squared.  
# For example, 25 is a perfect square of 5 as 5 x 5 = 25 and 5**2 = 25.
# def perfect_square(num1, num2):
#     return num2**2 == num1 and num1 / num2 == num2


# print(perfect_square(15, 5)) #> False
# print(perfect_square(25, 5)) #> True
# print(perfect_square(81, 9)) #> True
# print(perfect_square(9, 2))  #> False


# Problem 5 - Recursive Countdown
# Write your function, here

# import os
# import time


# def recursive_countdown(num):
#     if num <= 0:
#         os.system("clear")
#         print("Happy New Year!!!")
#         return
#     else:
#         os.system("clear")
#         print(num)
#         time.sleep(1)
#         recursive_countdown(num - 1)


# recursive_countdown(5) #> 5 4 3 2 1


# print(4.0 == 4)
# print(True == 1)
# print(True is 1)

# print(None == None)


# Write your function, here.
# def first_before_second(string, first, second):
#     return string.rindex(first) < string.index(second)


# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# #> True
# # Every instance of "a" occurs before every instance of "j".

# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# #> True

# print(first_before_second("happy birthday", "a", "y"))
# #> False
# # The "a" in "birthday" occurs after the "y" in "happy".

# print(first_before_second("precarious kangaroos", "k", "a"))
# #> False

# index = 0

# while index < 5:
#     if index == 3:
#         print('We found a three!')

#     else:
#         print("Not a 3!")

#     index += 1

# while True:
#     print(index)

#     if index < 4:
#         index += 1
#         continue
#     print("This will be the end...")
#     break

# foods = ["wings", "pizza", "mac n cheese", "sandwich"]


# for food in foods:
#     print(food)

# for letter in "waffle":
#     print(letter)
# print("wings" in foods)
    

# range(start, stop, step)
# print(list(range(1, 10, 2)))

# for index in range(len(foods)):
#     print(foods[index])

# import random
# from random import randint, choice, choices, sample
# import os
# # import time
# from time import sleep

# count = 99

# while count < 1000:
#     os.system("clear")
#     print(f"♫ {count} little bugs in our code... ♬")
#     sleep(2.5)
#     print(f"♫ {count} pesky little bugs... ♬")
#     sleep(2.5)
#     print("♫ take one down and patch it around... ♬")
#     sleep(2.5)
#     new_bugs = randint(1, 100)
#     count += new_bugs
#     print(f"♫ {count} little bugs in our code! ♬")
#     sleep(2.5)


# TRY/EXCEPT

# num = "peanut"
# # print(5/num)
# # raise Exception("We done made an error, oopsies!")

# try:
#     print("In the try block...")
#     print(5/num)

# except ZeroDivisionError:
#     print("We can't divide by zero!")

# except TypeError:
#     print("We can't do math with strings!")
# # except: 
# #     print("We have made an error!")

# else:
#     print("we only see this if the try was successful")

# finally:
#     print("We will see this every time.")


# def seq_of_numbers(seq):
#     count = 1
#     results = ''
#     # index = 0
#     seq += " "

#     for index in range(len(seq)-1): # while index < len(seq)-1:
#         if seq[index] != seq[index + 1]:
#             results = results + str(count) + seq[index] + ","
#             count = 1
#         else:
#             count += 1

#         index += 1

#     return results



# print(seq_of_numbers("1211"))
# This is "one 1, one 2, two 1s"
# Prints "11,12,21"
# 111221

# print(seq_of_numbers("111221"))
# # This is "three 1s, two 2s, and one 1"
# # Prints "31,22,11"

# print(seq_of_numbers("31131211131221"))
# This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
#    one 3, one 1, two 2s, and one 1"
# Prints "13,21,13,11,12,31,13,11,22,11"


# FUNCTIONS

# def is_even(integer):
#     """will tell us if the passed in integer is even or not"""
#     return integer % 2 == 0

# print(is_even(7))
# print(is_even(8))


# even = lambda integer: integer % 2 == 0

# print(even(8))

# multiply = lambda num1, num2: num1 * num2

# print(multiply(2, 6))


# y = 1000
# print("1st time in global", y)
# PI = 3.14

# def some_function():
#     # y = 50
#     global y
#     print("1st print in function", y)
#     print(PI)
#     y += 50
#     print("2nd print in function", y)
#     # if True:
#     #     y += 50
#     # print("3rd print in function", y)


# some_function()

# print("2nd global print", y)

# LISTS
foods = ['tacos', 'wings', 'pizza', 'burgers']
# other_list = [1, 4, True, "tacos", None, [1, 2]]
# print(other_list)

# print(foods[-1])
# print(foods[1:3])
# print(foods[::-1])
# print(len(foods))

# foods.append("steak")
# print(foods)
# foods.extend(["salad", "hot dog"])
# print(foods)
# foods.insert(1, "burritos")
# print(foods)
# foods.remove("tacos")
# print(foods)
# foods.pop(3)
# print(foods)

# foods.sort()
# print(foods)

vals = [1, 2, 3, 4, 5]
print(sum(vals))
print(min(vals))
print(max(vals))