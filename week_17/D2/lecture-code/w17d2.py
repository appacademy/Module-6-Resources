# XOR
# print( True ^ False)
# print( True ^ True)
# print( False ^ False)
# print( False ^ True)


def breakfast(food):
    """Take in a food and judge if its a 
    good breakfast or not"""
    if food == "waffles":
        print(f"{food} is my favorite breakfast!")
    
    elif food == 'pancakes':
        print(f"{food} is pretty good, not waffles though")
    
    elif food == "bacon":
        print(f"Hey now! {food} is a delicious breakfast meat!")
    
    else:
        print(f"{food} is okay but not waffles!")


# breakfast('waffles')
# breakfast('pancakes')
# breakfast('bacon')
# breakfast('cereal')

# print("We will see this text")
# food = "bacon"
# print(f"{food} is so yummy!")


# XOR
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
# # 0b1
# # 0b0
# print(bin(5))
# print(bin(3))
# # 0b101
# # 0b011
# # 0b110
# print(bin(6))

# STRING
# meal = "breakfast"
# food = 'wings'

# print("""This
# is a multi
# line string
# """)

# print(f"We had {food} for {meal}!")

# print("b" + "an")
# print("b" + "an" * 2 + "a")

# day = 'Wing Wednesday'

# def super_import_function_that_saves_the_world(num):
#     print('World is saved, phew, that was a close one')
# # print(day[1])
# # print(day[-2])
# # print(day[start:stop:step])
# print(day[::-1])

# print(day.index("W"))
# print(day.find("x"))

# super_import_function_that_saves_the_world(3)

# print(day.count("x"))
# print(day.split("e"))
# print(list(day))
# print(day.upper())

# names = ['Brad', 'David', 'Andrew']
# print(", ".join(names))


# STRING PROBLEMS
# def is_palindrome(string):
#     # reversed_string = string[::-1]
#     # print("reversed", reversed_string)
#     # return string == reversed_string
#     return string == string[::-1]

# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False


# Problem 7 - Recursive String
# Write your function, here.
# str = "hello"
# print(str)
# word = str(123)


# def recursive_string(string):
#     # base case
#     if len(string) == 0:
#         return string

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


# NUMBERS

# num_1 = 250.0
# num_2 = int(num_1)
# string_1 =str(num_1)
# print(num_1, num_2, string_1)


# print(25 // 2)

# count = 0
# count += 1
# print(count)

# big_num = 1_000_000_000_000
# print(big_num)



# def recursive_countdown(n):
#     if n <= 0:
#         return 
#     else:
#         print(n)
#         recursive_countdown(n-1)


# recursive_countdown(5) #> 5 4 3 2 1
# recursive_countdown(15) #> 5 4 3 2 1

# import os
# import time

# def recursive_countdown_plus(n):
#     if n <= 0:
#         os.system("clear")
#         print("SURPRISE!!!")
#         return 
#     else:
#         os.system("clear")
#         print(n)
#         time.sleep(1)
#         recursive_countdown_plus(n-1)


# recursive_countdown_plus(5) #> 5 4 3 2 1


# def first_before_second(string, letter1, letter2):
#     return string.rindex(letter1) < string.index(letter2)



# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# #> True  Every instance of "a" occurs before every instance of "j".
# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# #> True
# print(first_before_second("happy birthday", "a", "y"))
# #> False  The "a" in "birthday" occurs after the "y" in "happy".
# print(first_before_second("precarious kangaroos", "k", "a"))
# #> False


# STATEMENTS

# index = 0

# while index < 5:
#     if index == 3:
#         print('We got a 3!')
#     else:
#         print(f"We got a {index}")

#     index += 1
# index = 0

# while True:
#     if index < 4:
#         print(index)
#         index += 1
#         continue

#     print("We hopefully got a index greater than 4")
#     break

# foods = ["pizza", "wings", "chicken cheesesteak", "salad"]

# for food in foods:
#     print(food)


# print("pizza" in foods)
# print("sandwich" in foods)

# RANGES
# first_range = range(5)
# print(first_range)
# print(list(first_range))
# second_range = range(1, 6, 2)
# print(list(second_range))

# # for index in range(5):
# #     print(index)

# for index in range(len(foods)):
#     print(index, foods[index])


# import random 
# import time
# import os

# count = 99

# while count < 1000:
#     os.system('clear')
#     print(f"{count} little bugs in our code...")
#     time.sleep(2)
#     print(f"{count} pesky little bugs...")
#     time.sleep(2)
#     print("Take one down and patch it around...")
#     time.sleep(2)
#     new_bugs = random.randint(1, 100)
#     count += new_bugs
#     print(f"{count} little bugs in our code!")
#     time.sleep(2)

# TRY EXCEPT

# num = 0

# try:
#     print("in the try block")
#     print(4 / num)

# except ZeroDivisionError:
#     print("You can not divide by zero!")


# except TypeError:
#     print("we can not divide strings!")

# # except:
# #     print("something went wrong!  oh no!")

# else:
#     print("only fires if the try is sucessful!")

# finally:
#     print('We will see this every time')


# def seq_of_numbers(seq):
#     seq += ' '
#     count = 1
#     index = 0
#     results = ''

#     while index < len(seq) - 1:
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
# # 111221

# print(seq_of_numbers("111221"))
# # This is "three 1s, two 2s, and one 1"
# # Prints "31,22,11"

# print(seq_of_numbers("31131211131221"))
# This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
#    one 3, one 1, two 2s, and one 1"
# Prints "13,21,13,11,12,31,13,11,22,11"


# FUNCTIONS
# def is_even(num):
#     """returns if the provided number is even or not"""
#     return num % 2 == 0


# # print(is_even(7))

# even = lambda num: num % 2 == 0
# print(even(7))

# multiply = lambda num1, num2: num1 * num2

# print(multiply(3,4))


# SCOPE
# y = 200
# PII = 3.145

# print("y in global scope", y)
# def some_function():
#     # y = 10
#     global y 
#     print("y inside the function", y)
#     print(PII)
#     if True:
#         print("in if block", y)
#         y += 10
#         print("in if block", y)
#     y += 10
#     print("y inside the function second time", y)


# some_function()

# print("y in global scope", y)


# LISTS
dinners = ["pizza", "wings", "steak", "cobb salad", "taco"]
# print(dinners)
# print(len(dinners))

# print(dinners[2])
# print(dinners[1::2])
# print(dinners[::-1])
# dinners.append("turkey")
# print(dinners)
# dinners.extend(["sloppy joe", "corn"])
# print(dinners)
# dinners.insert(1, "shrimp")
# print(dinners)
# dinners.remove("taco")
# print(dinners)
# dinners.pop(1)
print(dinners)
dinners.sort()
print(dinners)

vals = [2, 4, 45, 12, 234]
print(sum(vals))
print(min(vals))
print(max(vals))