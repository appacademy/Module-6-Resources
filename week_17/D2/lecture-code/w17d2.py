# BOOLEANS

a = True
b = False

# XOR

# print(True ^ False)
# print(True ^ True)
# print(False ^ False)
# print(False ^ True)




# IF STATEMENTS

def breakfast(food):
    """accepts a food and judges your meal choices"""
    if food == "waffles":
        print(f"{food.title()} is my favorite breakfast!")

    elif food == 'pancakes':
        print(f"{food.upper()} is okay, but not waffles")

    else:
        print("Meh thats an okay choice but not waffles") 


# breakfast("waffles")
# breakfast('pancakes')
# breakfast("eggs")


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
# # 0b0
# # 0b0
# print(bin(5))
# print(bin(3))
# # 0b101
# # 0b011
# #   110
# print(bin(6))
# # 0b110
# print(int(0b011))


#STRING
# meal = "tacos"
# food = 'pizza'
# multi = '''This is a multi
# line string where new lines and also spaces
# are preserved'''
# print(multi)
# print(len(multi))
# print(f"We are eating {meal} for lunch today!")

# a = "a"
# b = "b"
# an = "an"

# print(b + an)
# print(b + 7 * a)
# print(b + an * 2 + a)
# num = 1_000_000_000_000
# print(num)

# # Indexing
# # print(food[start:stop:step])
# # print(food[0:End:1])
# print(food[2:4:])
# print(food[::-1])

# lunch = "meatball sub"
# print(lunch.index("x"))
# print(lunch.find("x"))
# print(lunch.count("x"))
# print(lunch.split())
# print(list(lunch))


# Write your function, here.
# def is_palindrome(string):
#     return string == string[::-1]


# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False


# Write your function, here.
# def recursive_string(string):
#     if len(string) == 0:
#         return string

#     return recursive_string(string[1:]) + string[0]

# #ivic     + c
# #vic + i
# #ic + v
# #c + i
# #     

# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) # noitacilppa

# # Problem 3 - Perfect Square
# # Write your function, here.
# def perfect_square(num_1, num_2):
#     return num_2**2 == num_1 and num_1 / num_2 == num_2

# print(perfect_square(15, 5)) #> False
# print(perfect_square(25, 5)) #> True
# print(perfect_square(81, 9)) #> True
# print(perfect_square(9, 2))  #> False


# Problem 5 - Recursive Countdown
# Write your function, here.
# def recursive_countdown(integer):
#     if integer <= 0:
#         return
#     else:
#         print(integer)
#         recursive_countdown(integer - 1)


# recursive_countdown(5) #> 5 4 3 2 1



# STATEMENTS

# index = 1

# while index <= 5:
#     print(f"{index}. Hello world!")
#     index += 1

# print("You've printed 5 times. Goodbye.")


# index = 0

# while True:
#     print(f"{index}. Hello world!")
#     if index < 4:
#         index += 1
#         continue

#     break


foods = ["tacos", 'wings', 'pizza', 'sandwich']

# for food in foods:
#     print(food)


# print("tacos" in foods)

# range(start,stop,step)
# range(10) # stop/end
# range(1, 10) # start, stop/end
# range(1, 10, 2) # start, stop/end, step

# print(tuple(range(1,10)))

# for index in range(len(foods)):
#     print(foods[index])


# num = "tacos"

# try:
#     print("in the try block")
#     print(4 / num)

# except ZeroDivisionError:
#     print("we can't divide by zero!") 


# except TypeError as error:
#     print("we can't do math with strings!")
#     print(error)

# # except:
# #     print("we had an error")

# else:
#     print("This will only run if the try was successful")


# finally:
#     print("we will see this every time")


# link to docs on exceptions  https://docs.python.org/3.9/library/exceptions.html?highlight=typeerror#TypeError

# def seq_of_numbers(seq):
#     seq += " "
#     index = 0
#     count = 1
#     results = ''

#     while index < len(seq) -1:
#         if seq[index] != seq[index +1]:
#             results = results + str(count) + seq[index] + ","
#             count = 1
#         else:
#             count += 1

#         index += 1

#     return results


# print(seq_of_numbers("1211 "))
# # This is "one 1, one 2, two 1s"
# # Prints "11,12,21"
# print(seq_of_numbers("111221"))
# # This is "three 1s, two 2s, and one 1"
# # Prints "31,22,11"
# print(seq_of_numbers("31131211131221"))
# # This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
# #    one 3, one 1, two 2s, and one 1"
# # Prints "13,21,13,11,12,31,13,11,22,11"

import os
import random
import time 

# bugs = 99

# while bugs < 1000:
#     os.system("clear")
#     print(f"{bugs} little bugs in our code")
#     time.sleep(2)
#     print(f"{bugs} pesky little bugs...")
#     time.sleep(2)
#     print("Take one down and patch it around...")
#     time.sleep(2)
#     bugs += random.randint(10, 100)
#     print(f"{bugs} little bugs in our code!")
#     time.sleep(2)

# Identity vs Equality
# my_int = 4
# my_float = 4.0

# print(my_float == my_int)
# print(my_float is my_int)

# print(1 == True)
# print(1 is True)
# print(1 == None)

# Write your function, here.
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

# FUNCTIONS

def is_even(num):
    """a function that will tell if a number is even"""
    return num % 2 == 0

# # print(is_even(7))

# even = lambda num: num % 2 == 0
# # print(even(9))

# multiply = lambda num_1, num_2: num_1 * num_2
# print(multiply(10,2))

# SCOPE
# PI = 3.14
# y = 100
# print(y, "global scope y, print 1")
# def function():
#     # y = 10
#     global y
#     print(y, "inside our function")
#     print(PI)
#     y += 10
#     print(y, "inside our function")

# function()


# print(y, "global scope y, print 2")
# y += 35
# print(y, "global scope y, print 2")

# LISTS
dinner = ["tacos", "meatloaf", "pizza", "salad", "steak"]

# print(dinner[2])
# print(dinner[:4])
# print(dinner[::-1])
# print(len(dinner))
# dinner.append("fried onions")
# print(dinner)
# dinner.extend(['pasta', 'chicken fingers'])
# print(dinner)
# dinner.remove("salad")
# print(dinner)
# dinner.insert(1, "apples")
# print(dinner)
# dinner.pop(0)
# print(dinner)

# dinner.sort()
# print(dinner)


vals = [1, 2, 3, 4, 5]
print(sum(vals))
print(min(vals))
print(max(vals))
