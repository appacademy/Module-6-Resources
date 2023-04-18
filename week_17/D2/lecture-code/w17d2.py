# XOR

# print(True ^ False)
# print(True ^ True)
# print(False ^ False)
# print(False ^ True)

# print(True or False)

# IF STATEMENTS

def breakfast(food):
    """Accept a food and offer commentary on 
    said breakfast choice"""

    if food == "waffles":
        print(f"{food} is my favorite breakfast!")

    elif food == "pancakes":
        print(f"{food} are pretty good too, but not waffles")

    elif food == "fruit cup":
        print(f"{food}!  Wow are we starting the day healthy!")

    else: 
        print(f"{food} is not my favorite, but enjoy!")
    
    return food

# something = breakfast("waffles")
# print(something)
# breakfast('pancakes')
# breakfast('fruit cup')
# breakfast('cereal')

# TERNARY SYNTAX
# hungry = False
# second_breakfast = "waffles" if hungry else "pancakes"
# print(second_breakfast)

# XOR PROBLEM
def xor(val1, val2):
    return val1 ^ val2


# print(xor(False, False))   #>  False
# print(xor(True, False))   #>  True
# print(xor(True, True)) #>  False
# print(xor(5, 3))  #> 6
# # print(xor(8, 4))  #> 12
# # print(xor(2, 2))  #> 0
# # print(xor(1, 2))  #> 3
# # print(xor(4, 4))  #> 0
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

# STRING

meal = "breakfast"
sentence = '''This is a 
lovely lovely
multi line
string'''
# print(sentence)
# print(f'I had {food} for {meal}!')

a = 'a'
b = 'b'
an = 'an'

# print(b + a)
# print(b + a * 7)
# print(b + an * 2 + a)

lunch = "tacos"
# print(lunch[2])
# print(lunch[-1])
# # print(lunch[start:stop:step])
# print(lunch[::-1])
food = 'waffles'


# print(food.index('a'))
# print(food.index('aff'))
# # print(food.index('q'))
# print(food.find('q'))
# print(food.count('f'))
# print(food.count('q'))
# print(food.upper())
# print(food.lower())
# print(food.title())
# print(food.split('f'))
# print(list(food))


# # Problem 7 - IS Palindrome
# # Write your function, here.

def is_palindrome(string):
    # return string == string[::-1]
    reverse_string = "".join(reversed(string))
    return string == reverse_string
    

# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False



# Problem 7 - Recursive String
# Write your function, here.
def recursive_string(string):
    if len(string) == 0:
        return string
    return recursive_string(string[1:]) + string[0]   
 #                   civi      + c
           
# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) # noitacilppa


# print(float(123))
# print(int("234"))
# print(4 / 2 )
# print(2 // 4) # ->  0.5 -> 0
# counter = 0
# counter += 1


# PERFECT SQUARE
# Write your function, here.
def perfect_square(num1, num2):
    return num1 / num2 == num2 and num2**2 == num1


# print(perfect_square(15, 5)) #> False
# print(perfect_square(25, 5)) #> True
# print(perfect_square(81, 9)) #> True
# print(perfect_square(9, 2))  #> False


# FIBONACCI
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Write your function, here.
def recursive_fib(integer):
    if integer <= 1:
        return integer
    
    else:
        return recursive_fib(integer - 1) + recursive_fib(integer - 2)



# print(recursive_fib(1))     #> 1
# print(recursive_fib(2))     #> 1
# print(recursive_fib(4))     #> 3
# print(recursive_fib(6))     #> 8
# print(recursive_fib(12))    #> 144


# IDENTITY vs EQUALITY
#    is         ==

# a = None
# print(id(a))
# b = None
# print(id(b))
# c = True 
# print(id(c))
# d = 1
# print(a is None)
# print( c == d)
# print( c is d)

# FIRST BEFORE SECOND
def f_b_s(string, letter1, letter2):
   first_letter2 = string.index(letter2)
   last_letter1 = string.rindex(letter1)
   return last_letter1 < first_letter2


# print(f_b_s("a rabbit jumps joyfully", "a", "j"))
# # True  Every instance of "a" occurs before every instance of "j".
# print(f_b_s("knaves knew about waterfalls", "k", "w"))
# # True
# print(f_b_s("happy birthday after", "a", "y"))
# # False The "a" in "birthday" occurs after the "y" in "happy".
# print(f_b_s("precarious kangaroos", "k", "a"))
# False

# WHILE LOOPS
# index = 0

# while index < 5:
#     print(f"{index}. Howdy Programmers!")
#     index += 1

# print("while loop exited")
# index = 0

# while True:
#     print(f"{index}. Howdy Programmers!")
#     if index < 4:
#         index += 1
#         continue
#     print("done with continue")
#     break

# import random
# import time
# import os

# count = 99

# while count < 1000:
#     os.system('clear')
#     print(f'{count} little bugs in our code...')
#     time.sleep(2)
#     print(f"{count} pesky little bugs...")
#     time.sleep(2)
#     print("Take one down and patch it around...")
#     time.sleep(2)
#     new_bugs = random.randint(1, 200)
#     count += new_bugs
#     print(f"{count} little bugs in our code!")
#     time.sleep(2)


# FOR LOOP
dinners = ['tacos', 'pizza', 'wings', 'burger & fries', 'salad']

# for meal in dinners:
#     print(meal)

# print("tacos" in dinners)
# print("potato" in dinners)

# range(start, stop, step)

# print(list(range(10)))
# print(list(range(1,11)))
# print(list(range(11,0,-1)))

# for index in range(5):
#     print(f"{index}. Hello!")

# for index in range(len(dinners)):
#     print(f"{index}. our food is {dinners[index]}")


# TRY/EXCEPT
# num = "hi"

# try:
#     print("in the try block")
#     print(4/num)

# except ZeroDivisionError:
#     print("Can't divide by zero!")

# except TypeError:
#     print("Can't do math with strings")


# else:
#     print("will only run if try block suceeds")
#     print(num * 40)

# finally:
#     print("We will see this every time, it always runs")



# SEQUENCE OF NUMBERS
def seq_of_numbers(sequence):
    # "1211 "
    sequence += " "
    count = 1
    index = 0
    results = ''

    while index < len(sequence)-1:
        if sequence[index] != sequence[index+1]:
            results = results + str(count) + sequence[index] + ","
            count = 1
        
        else:
            count += 1

        index += 1
    
    return results


# print(seq_of_numbers("1211"))
# # This is "one 1, one 2, two 1s"
# # Prints "11,12,21"
# print(seq_of_numbers("111221"))
# # This is "three 1s, two 2s, and one 1"
# # Prints "31,22,11"
# print(seq_of_numbers("31131211131221"))
# This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
#    one 3, one 1, two 2s, and one 1"
# Prints "13,21,13,11,12,31,13,11,22,11"

# FUNCTIONS
# def is_even(number):
#     """takes in a number and returns a boolean 
#     if the number is even"""
#     return number % 2 == 0


# print(is_even(5))

# even = lambda num: num % 2 == 0
# print(even(5))

# multiply = lambda num1, num2: num1 * num2
# print(multiply(3, 10))


# SCOPE

# y = 100
# PI = 3.14

# def some_function():
#     """this is gonna do functionie stuff"""
#     global y
#     print("inside our function", y)
#     if y:
#         y += 30
#         print("not new scope")
#     print(PI)
#     y += 10
#     print("inside our function, again", y)

# some_function()

# print("outside after function ran", y)


# def math(num1, num2, num3=30, *args, **kwargs):
#     print(num1, num2, num3)


# math(10, 20, 40)

# LISTS

foods = ['tacos', 'wings', 'pasta', 'carrot', 'apple']

# print(foods)
# print(len(foods))

# print(foods[-2])
# print(foods[0:4:2])
# print(foods[::-1])
# foods.append('steak')
# print(foods)
# foods.extend(["salad", "sloppy joe"])
# print(foods)
# foods.insert(2, "pizza")
# print(foods)
# foods.remove("carrot")
# print(foods)
# foods.pop(4)
print(foods)

vals = [2, 4, 8, 14, 23, 5, 11, 234]
vals.sort()
print(vals)
print(sum(vals))
print(min(vals))
print(max(vals))

