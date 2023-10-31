# XOR

# print(True ^ False)
# print(True ^ True)
# print(False ^ True)
# print(False ^ False)

def candy(piece_of_candy):
    """take in a candy piece and then judge 
    your candy choices"""

    if piece_of_candy == "milky way bar":
        print(f"{piece_of_candy} is a delicious choice!")

    elif piece_of_candy == "peanut butter cup":
        print(f"{piece_of_candy}!!! Just throw as many as you can directly into my mouth space!")

    elif piece_of_candy == "candy corn" or piece_of_candy == "smartie":
        print(f"{piece_of_candy}!?!?!?!  You do not know what candy is...")

    else:
        print(f"{piece_of_candy} is an okayish choice...")


# candy("milky way bar")
# candy("mild duds")
# candy("peanut butter cup")
# candy('candy corn')
# candy("smartie")

#XOR
# def xor(x, y):
#     return x ^ y


# print(xor(False, False))   #>  False
# print(xor(True, False))   #>  True
# print(xor(True, True)) #>  False
# print(xor(5, 3))  #> 6
# print(xor(8, 4))  #> 12
# print(xor(2, 2))  #> 0
# print(xor(1, 2))  #> 3
# print(xor(4, 4))  #> 0
# # print(bin(True))
# # print(bin(False))
# #  0b1
# #  0b1
# #  0b0
# print(bin(5))
# print(bin(3))
# #  0b101
# #  0b011
# #    110
# print(bin(6))

# STRINGS

# multi_string = """Happy Halloween to everyone!
# hope you      have fun trick or treatings 
# and 
# don't eat yellow candy"""
# print(multi_string)


# big_number = 1_000_000_000
# big_number = 1000000000
# print(big_number)

# a = "a"
# b = "b"
# an = "an"
 
# print(b + an)
# print(b + a * 7)
# print(b + an * 2 + a)

halloween_char = "Jack Skellington"

def function_to_save_halloween_from_disaster():
    return "awesomeness"

# print(halloween_char[-5])
# print(halloween_char[start:stop:step])
# print(halloween_char[::-1])
# copy_hc = halloween_char[::]

# print(halloween_char.index("c"))
# print(halloween_char.index("k"))
# print(halloween_char.index("ell"))
# print(halloween_char.find("w"))

# print(function_to_save_halloween_from_disaster())
# print(halloween_char.count('l'))
# print(halloween_char.split('n'))
# print(list(halloween_char))

# print(" -  ".join(["milky way", "snickers", "almond joy"]))
# print(halloween_char.upper())

# # Problem 7 - IS Palindrome
# # Write your function, here.

# def is_palindrome(string):
#     return string[::-1] == string   
#     # reverse = " ".join(reversed(string))
 
# is_palindrome(1)


# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False



# Problem 7 - Recursive String
# # Write your function, here.
# def recursive_string(string):
#     # base case
#     if len(string) == 0:
#         return string

#     # recursive step
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

# print()

# print(int('120'))
# print(float(120))
# print(str(3))
# # print(int(3.145))

# import os
# import time

# def more_fun_recursive_countdown(num):
#     if num <= 0:
#         os.system("clear")
#         print("its lunchtime!  enjoy your lunch!")
#         return

#     else:
#         os.system("clear")
#         print(num)
#         time.sleep(1)
#         more_fun_recursive_countdown(num -1)


# more_fun_recursive_countdown(10) 
# print(int("3") == 3)
# print(True == 1)
# print(False == 0)
# print(True is 1)
# print(False is 0)
# print(None == None)
# print(None is None)


# First Before Second
# def first_before_second(string, letter1, letter2):
#     return string.rindex(letter1) < string.index(letter2)



# print(first_before_second("a rabbit jumps joyfully", "a", "j")) #> True
# # Every instance of "a" occurs before every instance of "j".
# print(first_before_second("knaves knew about waterfalls", "k", "w")) #> True
# print(first_before_second("happy birthday", "a", "y")) #> False
# # The "a" in "birthday" occurs after the "y" in "happy".
# print(first_before_second("precarious kangaroos", "k", "a")) #> False


# STATEMENTS
# WHILE LOOPS

# pumpkins = 1

# while pumpkins < 6:
#     print(f'We have {pumpkins} pumpkins 🎃')

    # pumpkins += 1

# while True:
#     if pumpkins < 6:
#         print(f'We have {pumpkins} pumpkins 🎃')
#         pumpkins += 1
#         continue

#     break

# FOR LOOPS

# candies = ["Reeses' Pieces", "3 Musketeers", "heath bar", "Twix"]

# for candy in candies:
#     print(candy)

# print("heath bar" in candies)
# print("milky way" in candies)
# print('s' in "snickers")

# RANGES
# print(range(start, stop, step))
# print(range(10))
# print(list(range(10)))
# print(list(range(10, -1, -1)))
# print(tuple(range(10, 0, -1)))

# # for integer in range(11):
# #     print(integer) 

# for index in range(len(candies)):
#     print(f"{index}. {candies[index]}")


# import random
# import time
# import os

# count = 99


# while count < 1000:
#     os.system("clear")
#     print(f"{count} little bugs in our code...")
#     time.sleep(2.5)
#     print(f"{count} pesky little bugs...")
#     time.sleep(2.5)
#     print("Take one down and patch it around...")
#     time.sleep(2.5)
#     new_bugs = random.randint(50, 100)
#     count += new_bugs
#     print(f"{count} little bugs in our code!")
#     time.sleep(2.5)


# TRY / EXCEPT


# raise Exception("we done made a boo boo")

# try:
#     num = int(input("provide you number here: "))
#     print("In the try block")
#     print(4/num)

# except ZeroDivisionError:
#     print("we can not divide by zero")

# except TypeError:
#     print("we can't do math with strings!")

# except ValueError:
#     print("we need to provide number digit values")


# else:
#     print("we will only see this if the try is successful")

# finally:
#     print("We will always see this finally block")
#     print("its like an old friend ")

# def seq_of_numbers(seq):
#     count = 1
#     index = 0
#     results = ''
#     seq += " "

#     while index < len(seq) -1:   # for index in range(len(seq) -1)
#         if seq[index] != seq[index + 1]:  
#             results = results + str(count) + seq[index] + ','
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
# # This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
# #    one 3, one 1, two 2s, and one 1"
# # Prints "13,21,13,11,12,31,13,11,22,11"

# FUNCTIONS

# def is_even(num):
#     """takes in a number and tells us if its even"""
#     return num % 2 == 0

# print(is_even(7))


# even = lambda num: num % 2 == 0

# print(even(7))
# print(even(8))

# multiply = lambda num1, num2: num1 * num2
# print(multiply(2, 5))

# SCOPE

# PIE = 3.145

# candies = 50
# print("candies global 1st time", candies)

# def trick_or_treat():
#     """silly fucntion to demonstrate scope"""
#     print(PIE)
#     # candies = 10
#     global candies
#     print("candies in the func", candies)
#     candies += 20
#     print("candies in the func 2nd time", candies)
#     if True:
#         candies = 1_000_000_000

# trick_or_treat()

# print("global after function call", candies)
candies = ["Snickers", "Milky Way", "Twix", "Kitkats", "Health Bar"]
# mish_mosh = [1, True, None, "pumpkin", "5"]
print(candies)
# print(len(candies))
# print(candies[1:4])
# print(candies[::-1])
# candies.append("Dots")
# print(candies)
# candies.extend(["Payday", "3 Musketeers"])
# print(candies)
# candies.insert(1, "1,000,000 Bar")
# print(candies)
# candies.remove("Twix")
# print(candies)
# candies.pop(2)
# print(candies)
# candies.sort()
# print(candies)
vals = [1, 3, 4, 6, 8, 20]
print(sum(vals))
print(max(vals))
print(min(vals))