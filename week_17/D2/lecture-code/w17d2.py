# XOR
# print(True ^ False)
# print(True ^ True)
# print(False ^ False)
# print(False ^ True)


# print(False and True)
# print(True or True)


def breakfast(food):
    if food == 'waffles':
        print(f'{food} is the best breakfast!')
    
    elif food == 'pancakes':
        print(f"{food} is a pretty good breakfast!")
    
    elif food == 'french toast':
        print(f"Heck yeah!  French Toast!")

    else:
        print("Your breakfast choice is weak")


# breakfast("waffles")
# breakfast("pancakes")
# breakfast("cereals")
# breakfast("french toast")


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
# 0b1
# 0b0
# print(bin(5))
# print(bin(3))
# # 0b101
# # 0b011
# # 0b110
# print(bin(6))

# print("let's")
# print('let\'s')
# print("""This lets us 
# make a multi line string
# and preserve spaces  
# and     new lines
# """)

food = "tacos"

# print(food[1])
# print(food[-2])
# print(food[start:stop(non inclusive):step])
# print(food[:3])
# print(food[::-1])

# print(food.index('ac'))
# print(food.find('aw'))
# print(food.split("a"))
# print(list(food))


# Palindrome problem
def is_palindrome(string):
    return string == string[::-1]
 

# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False


# Problem 7 - Recursive String
# Write your function, here.
def recursive_string(string):
    # base case
    if len(string) == 0:
        return string
    # recursive case
    return recursive_string(string[1:]) + string[0]
#                           #ivic     + c
                            #vic + i
                            #ic + v
                            #c   + i
                            #     


# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) # noitacilppa

# # Problem 3 - Perfect Square
# # Write your function, here.
def perfect_square(num1, num2):
    return num2**2 == num1 and num1 / num2 == num2


# print(perfect_square(15, 5)) #> False
# print(perfect_square(25, 5)) #> True
# print(perfect_square(81, 9)) #> True
# print(perfect_square(9, 2))  #> False


# Operators (Equality vs Identity)
# val = "power"
# print(id(val))
# other_val = val
# print(id(other_val))
# yet_another_val = val
# print(id(yet_another_val))
# even_one_more_val = yet_another_val.lower()
# print(id(other_val.upper()))
# print(id(yet_another_val.lower()))


# print(val is even_one_more_val)
# print(val == even_one_more_val)




# Write your function, here.
def first_before_second(string, letter1, letter2):
    last_first_letter = string.rindex(letter1)
    print(last_first_letter)
    first_last_letter = string.index(letter2)
    print(first_last_letter)
    return last_first_letter < first_last_letter 

# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# #> True  # Every instance of "a" occurs before every instance of "j".
# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# #> True
# print(first_before_second("happy birthday", "a", "y"))
# #> False  # The "a" in "birthday" occurs after the "y" in "happy".
# print(first_before_second("precarious kangaroos", "k", "a"))
# #> False


# STATEMENTS

# While Loop
index = 0
# while index < 5:
#     print(f'{index}. Hey there!')
#     index += 1

# print("exited while loop, hopefully we printed 5 times")

# while True:
#     print(f"{index}. we printed!")
#     if index < 4:
#         index += 1
#         continue
#     print("we should have printed 5 times")
#     break


# import random
# import time
# import os

# count = 99

# while count < 1000:
#     os.system("clear")
#     print(f"{count} little bugs in our code...")
#     time.sleep(2)
#     print(f"{count} pesky little bugs...")
#     time.sleep(2)
#     print("Take one down and patch it around...")
#     time.sleep(2)
#     new_bugs = random.randint(1, 75)
#     count += new_bugs
#     print(f"{count} little bugs in our code!")
#     time.sleep(2)


foods = ["pizza", "tacos", "wings", "salad"]

# for food in foods:
#     print(food)

# print("pizza" in foods)
# print("burrito" in foods)

# range(start, stop, step)
# print(range(10))
# print(list(range(10)))

# for index in range(len(foods)):
#     print(f"{index}. {foods[index]}")



# TRY/EXCEPT

# num = 0
# # print(4/num)

# try:
#     print("In the try block")
#     print(4/num)


# except ZeroDivisionError:
#     print("You can not divide by zero!")

# except TypeError:
#     print("You can not do division with strings!")

# else:
#     print("You will only see me if the try succeeded")

# finally:
#     print("We will always see this")


# print("Super important info...")

# Sequence of numbers

def seq_of_numbers(seq):
    # iterate
    # conditional check value is the same as the next value
    # index for iteration
    # counter 
    count = 1
    index = 0
    results = ''
    seq += " "

    while index < len(seq)-1:
        if seq[index] != seq[index + 1]:
            results = results + str(count) + seq[index] + ","
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


# # FUNCTIONS
# def is_even(integer):   
#     """take in an integer and return a boolean if 
#     the integert is even or not"""
#     return integer % 2 == 0

# # print(is_even(5))

# # even = lambda integer: integer % 2 == 0
# # print(even(5))

# # multiply = lambda num1, num2: num1 * num2
# # print(multiply(2, 5))

# # SCOPE

# y = 100

# DAYS = ["Mon", "Tues", "Wed"]
# PI = 3.14

# def some_function():
#     """nonsensical function made only 
#     to demonstrate scope in python"""
#     # y = 50
#     global y
#     print("inside some function y = ", y)

#     def other_function():
#         global y
#         print("inside other function y = ", y)
#         y += 15
    
#     other_function()

#     print("inside some function 2nd time, y = ", y)
#     y += 20

#     print("inside some function 3rd time, y = ", y)
#     # if True:
#     #     print("inside the if block y =",y)

# some_function()

# print("y outside function y =", y)

# print(some_function.__doc__)


# LISTS

foods = [
        "Hamburger", 
        "Hot Dog", 
        "Ice Cream", 
        "Cake", 
        "Pure Sugar"
    ]

# print(foods)
# print(foods[1])
# print(foods[1:4])
# print(foods[::-1])
# print(len(foods))
# foods.append("Donuts")
# foods.append("Donuts")
# print(foods)
# foods.extend(["Deep Fried Butter", "Funnel Cake"])
# print(foods)
# foods.insert(1, "Fried Ice Cream")
# print(foods)
# foods.remove("Donuts")
# print(foods)
# val = foods.pop()
# print(foods)
# print(val)

vals = [2, 3, 6, 8, 56, 12, 7]

vals.sort()
print(vals)
print(sum(vals))
print(min(vals))
print(max(vals))