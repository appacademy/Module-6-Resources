# BOOLEANS

# XOR
# print(True ^ True)
# print(True ^ False)
# print(False ^ True)
# print(False ^ False)

# def breakfast(food):
#     """takes in a food arguement and returns judgement on your food decsions"""
#     if food == "waffles":
#         print(f"{food} is an excellent choice!")

#     elif food == "pancakes":
#         print(f"{food} are my second fav breakfast, nice job!")

#     elif food == "cereal":
#         print(f"{food} eh?  We aren't even trying today?")

#     else:
#         print(f'{food} is an okay choice, but not as good as waffles...') 


# breakfast('waffles')
# breakfast("pancakes")
# breakfast("cereal")
# breakfast("toast")
# day = "Tuesday"
# todays_breakfast = "waffles" if day == "Wednesday" else "cereal"

# print(todays_breakfast)

# Problem 4 - XOR
# Write your function, here.
def xor(x, y):
    return x ^ y


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
# # 0b110
# print(bin(6))

# STRINGS
lunch = "wings"
# print(lunch)
# print(len(lunch))
# long_string = """

# 1

# """
# print(long_string)
# print(len(long_string))

# print(f"{lunch.upper()} is a great lunch!")

# a = "a"
# b = "b"
# an = "an"
 
# print(b + an)
# print(b + a*7)
# print(b + an*2 + a)

other_lunch = "Chicken Parm Sandwich"

# print(other_lunch[-2])
# # print(other_lunch[start:stop:step])
# print(other_lunch[::-1])

# print(other_lunch.index("ken"))
# print(other_lunch.index("c"))
# print(other_lunch.find("q"))

# print(other_lunch.count('q'))
# print(other_lunch.split("c"))
# print(list(other_lunch))

# foods = ["pizza", "wings", "chicken parm"]
# print(", ".join(foods))


# def is_palindrome(string):
#     # print(str(1))
#     # return string == string[::-1]
#     reverse = ''.join(reversed(string))
#     print(reverse)
#     return string == reverse


# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False



# Problem 7 - Recursive String
# Write your function, here.
# def recursive_string(string):
#     # BASE CASE
#     if len(string) == 0:
#         return string
#     # RECURSIVE STEP
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
# big_number = 1_000_000_000
# print(big_number)
# big_num = 1,0
# print(big_num)

# # Problem 3 - Perfect Square
# # Write your function, here.
# def perfect_square(num1, num2):
#     return num1 / num2 == num2 and num2 * num2 == num1


# print(perfect_square(15, 5)) #> False
# print(perfect_square(25, 5)) #> True
# print(perfect_square(81, 9)) #> True
# print(perfect_square(9, 2))  #> False


# def recursive_countdown(n):
#     if n <= 0:
#         return
#     else:
#         print(n)
#         recursive_countdown(n - 1)


# recursive_countdown(5) #> 5 4 3 2 1
# import os 
# import time 


# def recursive_xmas_countdown(n):
#     if n <= 0:
#         os.system("clear")
#         print('MERRY CHRISTMAS!!!')
#         return
#     else:
#         os.system("clear")
#         print(n)
#         time.sleep(0.5)
#         recursive_xmas_countdown(n - 1)


# recursive_xmas_countdown(26) #> 5 4 3 2 1

# Identity vs equality

# print(True == 1)
# print(False == 0)
# print(True is 1)
# print(False is 0)

# a = None
# print(id(a))
# b = None
# print(id(b))
# c = 'pizza'
# d = 1
# e = True


# Problem 1 - First Before Second
# Write your function, here.
# def first_before_second(string, letter1, letter2):
#    return string.rindex(letter1) < string.index(letter2)


# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# # > True  Every instance of "a" occurs before every instance of "j".
# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# #> True
# print(first_before_second("happy birthday", "a", "y"))
# #> False  The "a" in "birthday" occurs after the "y" in "happy".
# print(first_before_second("precarious kangaroos", "k", "a"))
#> False

# WHILE LOOP
index = 0

# while index < 5:
#     if index == 3:
#         print("We've got a three")

#     else:
#         print("Not a 3!")

#     index += 1

# while True:
#     if index < 5:
#         print(index)
#         index += 1
#         continue

#     break

# info = input("Gimme info please" )
# foods = ["pizza", "Chicken Parm", "Wings", "Chef Salad"]

# for food in foods:
#     print(food)

# print("pizza" in foods)

# for index in range(len(foods)):
#     print(f"{index}. {foods[index]}")


# dinner = "Chicken Parm"

# for letter in dinner:
#     print(letter)

# RANGE

# my_range = range(start, stop, step)
# print(list(range(1, 5, 2)))
# print(tuple(range(5, 1, -1)))


# import random
# from random import randint
# from time import sleep
# import os

# count = 99

# while count < 1000:
#     os.system("clear")
#     print(f"{count} little bugs in our code...")
#     sleep(2.5)
#     print(f"{count} pesky little bugs...")
#     sleep(2.5)
#     print("Take one down and patch it around...")
#     sleep(2.5)
#     new_bugs = randint(1, 100)
#     count += new_bugs
#     print(f"{count} little bugs in our code!")
#     sleep(2.5)

# TRY/EXCEPT
# def save_the_holiday_season():
#     print("Its saved, yay!")

# num = "wings"

# try: 
#     print(5/num)

# except ZeroDivisionError:
#     print("You can not divide by zero")
    
# except TypeError:
#     print("You can't divide by a string...")

# # except:
# #     print("You have gotten an error, bummer")

# else:
#     print("if you see me, you see math above me...")

# finally:
#     print("We will see this every time for reals")

# save_the_holiday_season()


# def seq_of_numbers(seq):
#     seq += " "
#     count = 1
#     index = 0
#     results = ''

#     while index < len(seq) - 1:  # for index in range(len(seq)-1)
#         if seq[index] != seq[index + 1]:
#             results = results + str(count) + seq[index] + ","
#             count = 1
#         else:
#             count += 1

#         index += 1 # remove if using a for loop

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
#     """tells us if the parameter is an even number"""
#     return num % 2 == 0

# print(is_even(4))

# even = lambda num: num % 2 == 0
# print(even(4))

# multiply = lambda num1, num2: num1 * num2

# print(multiply(2, 5))

# SCOPE

# z = 50
# PIE = 3.145

# print("global scope before function", z)

# def some_func():
#     #  z = 20
#      global z 
#      print("inside func scope", z)
#      print(PIE)
#      z += 10
#      print("inside func scope 2x", z)

# some_func()

# print("Back in global after func", z)

# LISTS

foods = ["tacos", "burgers", "wings", "steamed veggies"]

# print(foods[1])
# print(foods[-2])
# print(foods[1:])
# print(foods[::-1])
# print(len(foods))
# foods.append("cookies")
# print(foods)
# foods.extend(["pizza", "calzone"])
# print(foods)
# foods.remove("tacos")
# print(foods)
# foods.insert(1, "buritto")
# print(foods)
# foods.pop(2)
# print(foods)

vals = [1, 5, 78, 2, 56]
vals.sort()
print(vals)
print(sum(vals))
print(min(vals))
print(max(vals))