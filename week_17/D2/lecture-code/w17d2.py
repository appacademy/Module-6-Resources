# XOR

# print(True or False)

# print(True ^ False)
# print(True ^ True)
# print(False ^ False)
# print(False ^ True)

# IF STATEMENTS

def breakfast():
    food = input("What are you having for breakfast?: ").lower()
    if food == "waffles":
        print(f"{food} is my favorite!  Yum Yum!")
    
    elif food == "pancakes":
        print(f"{food} is a great breakfast too!")
    
    else:
        print("you need to learn what breakfast is...")


# breakfast()
# breakfast("pancakes")
# breakfast("Skittles")


# XOR 

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
# # 0b1
# # 0b0
# print(bin(5))
# print(bin(3))
# # 0b101
# # 0b011
# # 0b110
# print(bin(6))
# 0b110

# STRINGS

long_string = '''This is a long
multi line string, its
so many lines!  
wow this is dark magic compared to boring ole JS '''


# a = 'a'
# b = 'b'
# an = 'an'

# print(b + a)
# print(b + a * 9)
# print(b + an * 2 + a)
meal = 'breakfast'
food = "waffles"
# print(f'We are eating {food} for {meal}!')

# print(food[2])
# print(food[-1])
# print(food[start:stop:step])
# print(food[:4:])
# print(food[::-1])

# print(food.index("aff"))
# # print(food.index("q"))
# # print(food.find("q"))
# print(food.count('q'))
# print(food.split('f'))
# print(list(food))
# print(food.upper())


# NUMBERS

# print( int(9) / int(3.1))
# print( int(9 / 3.1))


# a = 5
# a += 1
# print(a)
# a -= 1
# print(a)
# a *= 2
# print(a)


# FIBONACCI
def recursive_fib(num):
    """Recursively solve for the provided fibonacci number"""
    # base case
    if num <= 1:
        return num
    else:
        # recursive step
        return (recursive_fib(num - 1) + recursive_fib(num - 2))


# print(recursive_fib(1))     #> 1
# print(recursive_fib(2))     #> 1
# print(recursive_fib(4))     #> 3
# print(recursive_fib(6))     #> 8
# print(recursive_fib(12))    #> 144


# TOTAL DIGITS


def find_digit_amount(integer):
    # new_var = 500
    if integer < 0:
        # print(new_var)
        # new_var += 100
        return len(str(integer)) - 1
    
    return len(str(integer))


# "1110000111"
# 1110000111
# print(find_digit_amount(123))           #> 3
# print(find_digit_amount(-56))           #> 2
# print(find_digit_amount(7154))          #> 4
# print(find_digit_amount(61217311514))   #> 11
# print(find_digit_amount(0))             #> 1


# OPERATORS 

# my_int = 5
# print("After 5", id(my_int))
# my_float = 5.0
# my_int = 6
# print("After 6", id(my_int))

# print(my_int == my_float)
# print(my_int is my_float)
 

# print(id(my_float))
# print(id(my_int))
my_second_int = 5
# print("My second int", id(my_second_int))

# print(True == 1)
# print(True is 1)

# FIRST BEFORE SECOND
# Write your function, here.
# def first_before_second(string, char_1, char_2):
#     return string.rindex(char_1) < (string.index(char_2))


# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# #> True
# # Every instance of "a" occurs before every instance of "j".

# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# #> True

# print(first_before_second("happy birthday", "a", "y"))
# #> False
# # The "a" in "birthday" occurs after the "y" in "happy".

# print(first_before_second("precarious kangaroos", "k", "a"))

# i = 0

# while i <= 5:
#     if i == 3:
#         print(i, "We have a 3!")
#     else:
#         print(i, "Not a 3")

#     i += 1
# i = 5

# while True:
#     print(i)
#     if i > 1:
#         i -= 1
#         continue

#     print("This will only happen when i == 1")
#     break

# count = 99
# import random
# import time
# import os

# while count < 1000:
#     os.system("clear")
#     print(f"{count} little bugs in our code")
#     time.sleep(1.5)
#     print(f"{count} pesky little bugs...")
#     time.sleep(1.5)
#     print("Take on down and patch it around...")
#     time.sleep(1.5)
#     new_bugs = random.randint(1, 50)
#     count += new_bugs
#     print(f"{count} little bugs on the wall")
#     time.sleep(1.5)
#     print("")
    # count += 100


# FOR LOOP

lunch = ['tacos', 'wings', 'pizza', 'sandwich']

# for food in lunch:
#     print(food)

# print("tacos" in lunch)
# print("burger" in lunch)

# RANGES
nums = list(range(2, 21, 2))
# print(nums)

# for i in range(0,5):
#     print(f"{i}. Happy taco tuesday!")

# for index in range(0,len(lunch)):
#     print(lunch[index])


# TRY / EXCEPT
# num = "waffle"

# try:
#     print("In the try block")
#     print(4/num)
# except ZeroDivisionError:
#     print("You can't divide by zero there buddy!")
# except TypeError:
#     print("You can't divide integers by strings")
# else: 
#     print("we only see this if our try block works")
# finally:
#     print("We will alway see this every time")



# for val in something:
#     print("Hello")

# # Problem 6 - Sequence of Numbers
# # Write your function, here.
# # There are hints after the print statements
# def seq_of_numbers(seq):
#     pass
#     # iterate
#     # counter
#     # index variable
#     # compare values next to each other (indexing)  
#     # results variable, that we build as we go, return at the end
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
# # This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
# #    one 3, one 1, two 2s, and one 1"
# # Prints "13,21,13,11,12,31,13,11,22,11"



# FUNCTIONS
# def is_even(num):
#     """takes in a number and returns a boolean 
#     on if the number is even or not"""
#     return num % 2 == 0

# print(is_even(5))

# even = lambda num: num % 2 == 0
# print(even(8))

# multiply = lambda num_1, num_2: num_1 * num_2

# print(multiply(3, 75))

# SCOPE
# PII = 3.14

# num = 20

# def add_five():
#     """this function is going to be 
#     used to test scope"""
#     global num
#     print("inside function",num)
#     print("PII", PII)
#     num += 5
#     print("inside function after adding 5",num)

# add_five()

# print("Outside function",num)
# print(add_five.__doc__)

# LISTS
foods = ["tacos", "wings", "pizza", "burgers"]

# print(foods)
# print(foods[1])
# print(foods[-2])
# print(foods[1:3])
# print(foods[::-1])
# print(len(foods))
# more_foods = ["tacos", "burritos"]
# foods.append("steak")
# print(foods)
# foods.extend(more_foods)
# print(foods)
# foods.insert(1, "salad")
# print(foods)
# foods.remove("tacos")
# print("remove", remove_val)
# print(foods)
# pop_val = foods.pop(2)
# print(pop_val)
# print(foods)
# foods.sort()
# print(foods)

vals = [2, 4, 5, 7, 8, 9]
print(sum(vals))
print(min(vals))
print(max(vals))