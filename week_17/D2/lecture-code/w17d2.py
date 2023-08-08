# boolean_1 = True
# boolean_2 = False


# print(True ^ True)
# print(True ^ False)
# print(False ^ True)
# print(False ^ False)

# && || !
# and or not 


# print(1 != 2)
# print(not True)


# def breakfast(food):
#     """Accepts a food as an arguement and then judges your decisions"""

#     if food == "waffles":
#         print(f"{food} is my favorite breakfast!  Yum!")

#     elif food == "panckes":
#         print(f"{food} is okay, but not as good as waffles")

#     else: 
#         print(f"{food} is not waffles, yuck")


# q
# breakfast("waffles")
# breakfast("pancakes")
# breakfast("eggs")
# breakfast("shrimp n grits")


# Create a function that returns the xor result of two values.
# Write your function, here.
# def xor(val1, val2):
#     return val1 ^ val2

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
# 0b0
# print(bin(5))
# print(bin(3))
# # 0b101
# # 0b011
# #   110
# print(bin(6))

# DON'T DO THIS REAL BAD
# str = "jello"
# print(str)
# print(str(1))

# STRINGS
# meal = "Breakfast"
# long_string = """This is a really,
# really, really
# reakly,
# long string

# """
# print(long_string)
# print(f"{long_string} is a long string")


# food = "tacos"
# other_food = "banana"
# print(food[1])
# # food[start:stop:step]
# print(food[-2])
# print(food[:3])
# print(food[::-1])

# print(food.index('ac'))
# print(other_food.index("a"))
# # print(food.index('q'))
# print(food.find('q'))
# print(other_food.count('q'))
# print(other_food.split("a"))

# foods = ["tacos", "wings", "sandwich"]

# print(", ".join(foods))


# STRING PROBLEMS

# def is_palindrome(string):
#     # return string == string[::-1]
#     rev_string = reversed(string)
#     return string == "".join(rev_string)



# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False


def recursive_string(string):
    # base case
    if len(string) == 0:
        return string

    # recursive step
    return recursive_string(string[1:]) + string[0]
                            #ivic     + c
                            #vic + i
                            #ic + v
                            #c   + i
                            #     

# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) # noitacilppa


# print(10 / 2)
# print(10 // 2)
# print(9 // 2)
# print(9 / 2)

# big_num = 1_000_000_000
# big_num_2 = 1,000,000,000


# Write your function, here.
# Problem 5 - Recursive Countdown
# import os
# import time


# def recursive_countdown(number):
#     if number <= 0:
#         os.system("clear")
#         print("BOOM!")
#         return
#     else:
#         os.system("clear")
#         print(number)
#         time.sleep(1)
#         recursive_countdown(number - 1)


# timer_length = int(input("How many seconds for the timer?"))
# recursive_countdown(timer_length) #> 5 4 3 2 1



# # Problem 4 - Recursive Fibonacci


# The Fibonacci Sequence is the series of numbers:

# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# The next number is found by adding up the two numbers before it:

# the 2 is found by adding the two numbers before it (1+1),
# the 3 is found by adding the two numbers before it (1+2),
# the 5 is (2+3),
# and so on!
# Example: the next number in the sequence above is 21+34 = 55
# # Write your function, here.
# def recursive_fib(number):
#     if number <= 1:
#         return number
    
#     return (recursive_fib(number - 1) + recursive_fib(number - 2))
    

# print(recursive_fib(1))     #> 1
# print(recursive_fib(2))     #> 1
# print(recursive_fib(4))     #> 3
# print(recursive_fib(6))     #> 8
# print(recursive_fib(12))    #> 144

# def first_before_second(string, letter1, letter2):
#     return string.rindex(letter1) < string.index(letter2)

# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# #> True
# # Every instance of "a" occurs before every instance of "j".
# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# #> True
# print(first_before_second("happy birthday", "a", "y"))
# #> False
# # The "a" in "birthday" occurs after the "y" in "happy".
# print(first_before_second("precarious kangaroos", "k", "a"))
#> False

# STATEMENTS

index = 0

# while index < 5:
#     print(f"{index}. Hello World!")
#     index += 1

# while True:
#     print(index)
#     if index < 3:
#         index += 1
#         continue
#     print("index should be greater than 3")
#     break


# FOR LOOPS

# foods = ["pizza", "tacos", "waffles", "steak"]
# dessert = "ice cream"

# for index in range(len(foods)):
#     print(index, foods[index])

# for food in foods:
#     print(food)

# for letter in dessert:
#     print(letter)

# print("waffles" in foods)
# print("potato" in foods)

# # range(start,stop,step)
# first_range = range(2, 7, 2)
# print(first_range)
# print(list(first_range))


# TRY / EXCEPT
# try:
#     "connect to the db"

# except: 
#     "did not connect, bad times, but we excepted/caught our error"

# else:
#     "do DB stuff, add, delete, query"

# finally:
#     "close out DB connection"

# number = 0

# try:
#     print("In the try block")
#     print(4/number)

# except ZeroDivisionError:
#     print("you can not divide by zero")

# except TypeError:
#     print("you can't divide with strings")

# # except:
# #     print("something bad happened, it got messy...")

# else:
#     print("only if try worked, do we see this code")

# finally:
#     print("we will always see this")

# # random_code_that_somehow_save_the_entire_planet()

# raise Exception("You done made an error")


# def seq_of_numbers(seq):
#     count = 1
#     index = 0
#     results = ""
#     seq += ' '

#     # for index in range(len(seq)-1):
#     while index < len(seq) -1:
#         if seq[index] != seq[index+1]:
#             results = results + str(count) + seq[index] + ","
#             count = 1
#         else:
#             count += 1

#         index += 1

#     return results    

# str = "pizza"


# print(seq_of_numbers("1211"))
# # This is "one 1, one 2, two 1s"
# # Prints "11,12,21"
# # 111221

# print(seq_of_numbers("111221"))
# # This is "three 1s, two 2s, and one 1"
# # Prints "31,22,11"

# print(seq_of_numbers("31131211131221"))
# # This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
# #    one 3, one 1, two 2s, and one 1"
# # Prints "13,21,13,11,12,31,13,11,22,11"

# SONG TIME!
# import random
# import time
# import os

# count = 99

# while count < 1000:
#     os.system("clear")
#     print(f'{count} little bugs in our code...')
#     time.sleep(2)
#     print(f"{count} pesky little bugs...")
#     time.sleep(2)
#     print("Take one down and patch it around...")
#     time.sleep(2)
#     new_bugs = random.randint(25, 100)
#     count += new_bugs
#     print(f"{count} little bugs in our code!")
#     time.sleep(2)


# FUNCTIONS
# def is_even(number):
#     """accepts a number and returns a boolean on if the number is even"""
#     return number % 2 == 0

# print(is_even(0))

# even = lambda number: number % 2 == 0 

# print(even(7))
# print(even(10))

# multiply = lambda num_1, num_2: num_1 * num_2
# print(multiply(3, 4))

# y = 50
# print(y, "global scope before function")
# PI = 3.14

# def some_function():
#     # y = 20
#     global y
#     print(y, "inside the function")
#     # print(PI)
#     y += 20
#     print(y, "in function second time")

# some_function()

# print(y, "global scope aftern function")

# def sum_nums(num1, num2, num3=30, *args, **kwargs):
#     print(num1, num2, num3)
#     print(args)
#     print(kwargs)

# sum_nums(10, 20, 40, 50, 60, num6=70, num8=80)
empy_list = []
dinner = ["tacos", "wings", "hamburger", "chef salad", "ice cream"]
# print(dinner)
# print(len(dinner))
# print(dinner[start:stop:step])
# print(dinner[1:4])
# print(dinner[::-1])
# dinner.append("pizza")
# print(dinner)
# dinner.extend(["steak", "gnocchi"])
# print(dinner)
# dinner.insert(1, "sloppy joe")
# print(dinner)
# dinner.remove("steak")
# print(dinner)
# dinner.pop(2)
# print(dinner)
# # dinner.sort()
# # print(dinner)
# sorted_dinner = sorted(dinner)
# print(sorted_dinner)

vals = [1, 2, 3, 4, 5]
print(sum(vals))
print(min(vals))
print(max(vals))
