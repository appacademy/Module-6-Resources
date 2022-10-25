#XOR

# print(True ^ False)
# print(True ^ True)
# print(False ^ False)
# print(False ^ True)

# 0 for any number type
# '' [] set() {}
# False None

num = 0

if num:
    pass # do stuff here

# print(True or False)

# IF STATEMENTS
def breakfast(food):
    if food == "waffle":
        print(f'{food} is my favorite breakfast!')
    elif food == "bacon":
        print(f'{food} is the most delicious thing on earth, yummy!')
    else:
        print(f'{food} is okay breakfast!')

# breakfast("bacon")

# XOR

def xor(x, y):
    """ takes 2 values and compares them with xor """
    return x ^ y


# print(xor(False, False))   #>  False
# print(xor(True, False))   #>  True
# print(xor(True, True)) #>  False
# print(xor(5, 3))  #> 6
# print(xor(8, 4))  #> 12
# print(xor(2, 2))  #> 0
# print(xor(1, 2))  #> 3
# print(xor(4, 4))  #> 0
# print(bin(5))
# print(bin(3))
# 0b101
# 0b011
# 0b110
# print(bin(6)) 

# STRINGS
meal = "breakfast"
food= 'pancakes'

# print(f"we are eating {food} for {meal}")
# print("we are eating {thing1} for {thing2}".format(thing2=meal, thing1=food))

multi = """ This is going
to allow us 
to make as many
lines
as we
would like
"""

# print(multi)

a = "a"
b = 'b'
an = 'an'

# print(b + an)
# print(b + an * 2 + a)

lunch = 'pizza'

# print(lunch[2])
# print(lunch[-1])
# print(lunch[::-1])

# print("index", lunch.index('q'))
# print("count", lunch.count('q'))
# print("split", lunch.split())

instructor = ["Brad", 'David', "John", 'Ryan']
# print(", ".join(instructor))
# print(lunch.upper())


# Write your function, here.
def is_palindrome(string):
    # reverse_string = string[::-1]
    # print("rev", reverse_string, "OG", string)
    reverse = ''.join(reversed(string))
    print(reverse)
    return string == reverse


# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False


# NUMBERS

# print(10 // 4)
# print(10 % 4)

# num = 10
# print(num)
# num += 1
# print(num)

# print( True is 1)



# First Before Second
# You are given three inputs: a string, one letter, 
# and a second letter. Write a function that returns 
# True if every instance of the first letter occurs 
# before every instance of the second letter.

def first_before_second(string, first, second):
    return string.rindex(first) < string.index(second)
    

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


# STATEMENTS
i = 0

# while i < 5:
#     if i == 3:
#         print(i, "We have a 3!!!")
#     else: 
#         print(i, "Nope not a 3 here")
#     i += 1

# while True:
#     print(f'{i}. Hello World!')
#     if i < 4:
#         i += 1
#         continue
#     print("You printed 5 times, We are done!")
#     break
#     print("Never gonna see this")


foods = ['pizza', 'tacos', 'waffles', 'wings', 'salad']

# for food in foods:
#     print(food)

# print("pizza" in foods)
# print("sandwich" in foods)

# RANGES 
# print(list(range(10,0,-1)))

# for i in range(len(foods)):
#     print(i, foods[i])

# TRY/EXCEPT


# num = "pizza"

# try:
#     print("In the try block")
#     print(4/num)

# except ZeroDivisionError:
#     print("We can not divide by zero")


# except TypeError:
#     print("we can't do math with non numbers")

# else:
#     print("We should see this only if our try block works")

# finally:
#     print("This is going to print no matter what")



# SEQUENCE OF NUMBERS
# Write your function, here.
# There are hints after the print statements
def seq_of_numbers(seq):
    seq += ' '
    count = 1
    # i = 0
    results = ''

    # while i < len(seq) - 1:
    for i in range(len(seq) - 1):
        if seq[i] != seq[i+1]:
            results = results + str(count) + seq[i] + ","
            count = 1
        else:
            count += 1
        # i += 1

    return results



# print(seq_of_numbers("1211 "))
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

def is_even(num):
    """takes in a number and returns a boolean 
    if that number is even or not"""
    if True:
        print("new indent for new block")
    return num % 2 == 0

# print(is_even(9))

# even = lambda num: num % 2 == 0

# print(even(6))

# multiply = lambda num1, num2: num1 * num2

# print(multiply(4, 4))

# SCOPING

y = 'pizza'
y = "burrito"

LUNCH = 'soup'

def make_a_five():
    """return the integer value of 5"""
    # y = 5
    # global y
    print("inside func", y)
    y = "taco"
    return y

# make_a_five()
# print("global scope", y)
# y = 'banana'
# print("global scope", y)


# def my_function(num, num2, num3=5, *args, **kwargs):
#     print(num, num2, num3)
#     print(args)
#     print(kwargs)

# my_function(2, 3, 6, 8, 9, num8=10, num9=239)


# LISTS

foods = ["tacos", "burgers", "pizza", "wings"]

# print(foods)
# # print(foods[::-1])
# # print(len(foods))
# foods.append("steak")
# print(foods)
# foods.extend(["salad", 'sloppy joe'])
# print(foods)
# foods.insert(1, 'mac n chees')
# print(foods)
# foods.remove('steak')
# print(foods)

vals = [2, 4, 56, 23, 7, 19]

vals.sort()
print(vals)
print(sum(vals))
print(min(vals))
print(max(vals))