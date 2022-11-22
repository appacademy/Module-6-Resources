# XOR

# print(True or False)

# print(True ^ True)
# print(True ^ False)
# print(False ^ True)
# print(False ^ False)

# Logical Operators
# && || !
# and or not 

# IF STATEMENTS
def breakfast(food):
    if food == "waffles":
        print(f"{food} are my favorite! Yum!")
        print("Breakfast is fun")
    elif food == "pancakes":
          print(f"{food} are pretty good too!")
    else:
        print(f"{food} is okay but not as good as waffles")

# breakfast("waffles")
# breakfast("pancakes")


# Create a function that returns the xor result of two values.
# Write your function, here.
def xor(val1, val2):
    return val1 ^ val2


# print(xor(False, False))   #>  False 0 0 
# print(xor(True, False))   #>  True 1 0 
# print(xor(True, True)) #>  False 1 1 
# print(xor(5, 3))  #> 6
# print(xor(8, 4))  #> 12
# print(xor(2, 2))  #> 0
# print(xor(1, 2))  #> 3
# print(xor(4, 4))  #> 0
# print(bin(True))
# print(bin(False))
# print(bin(5))
# print(bin(3))
# # 0b101
# # 0b011
# #   110
# print(bin(6))
# 0b110

# STRINGS

meal = "breakfast"
food = "waffles"

# print(f"We are eating {food} for {meal}!")
# message = '''We can make
# multi line strings with three quotes
# and they can be double or single
# quotes'''
# print(message)

a = "a"
b = "b"
an = "an"
# print(b + an)
# print(b + a * 7)
# print(b + an * 2 + a)

meal = "breakfast"
food = "waffles"

# print(meal[::-1])
# print(food.count("o"))
# print(food.index('aff'))
# print(food[1:5].upper())
# food.index("a").upper().title()

# print(12 / 5)
# print(12 // 5)
# print(float(23))
# print(int("12345"))

# val =  25.567
# print(int(round(val, 2)))


# a = None
# print(id(a))
# b = "Turkey"
# print(id(b))
# c = None
# print(id(c))
# print(a is c)

a = 1
# print(a == True)  # don't do this, in Python 1 is equal in value to True
# print(a is True)


def first_before_second(string, first, second):
    last_first = string.rindex(first)
    first_second = string.index(second)   
    return last_first < first_second 



# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# #> True
# # Every instance of "a" occurs before every instance of "j".

# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# #> True

# print(first_before_second("happy birthday", "a", "y"))
# #> False
# # The "a" in "birthday" occurs after the "y" in "happy".

# print(first_before_second("precarious kangaroos", "k", "a"))


# WHILE LOOPS

i = 0

# while i < 5:
#     print(f'{i} Happy Thanksgiving')
#     i += 1

# print("Outside the while loop")


# while True:
#     print(f'{i} Happy Thanksgiving')
#     if i < 4:
#         i += 1
#         continue
#     print(f"Did we get here? {i}")
#     break

# FOR LOOPS

pies = ['apple', 'pumpkin', 'pecan', 'berry', 'key lime']

# for pie in pies:
#     if pie == 'berry':
#         break
#     print(f"{pie} is delicious!")

# print("cherry" in pies)
# vals[start:stop:step]
# vals = range(start, stop, step)
vals = range(11, 1, -1)
# print(list(vals))

# for i in range(len(pies)):
#     print(f"{i}. {pies[i]}")

# for i, pie in enumerate(pies, start=1):
#     print(i, pie)


# TRY/EXCEPT - similar try/catch
# num = "turkey"

# try:
#     print("In the try block")
#     print(10 / num)

# except ZeroDivisionError:
#     print('we can not divide by zero')

# except TypeError:
#     print('we can do division with strings')

# else:
#     print('we will see this only if our try block works')

# finally:
#     print('we will always see this')


# # raise Exception("You made an error. boooo!")

# print("really important stuff we need to see")



# SEQUENCE OF NUMBERS
# Write your function, here.
# There are hints after the print statements
def seq_of_numbers(seq):
    seq += ' '
    count = 1
    i = 0
    results = ''
    while i < len(seq) -1:
        if seq[i] != seq[i+1]:
            results = results + str(count) + seq[i] + ','
            count = 1
        else:
            count += 1
        i += 1

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

def is_even(num):
    """
    takes in a number and returns a boolean if the 
    number is even
    """
    return num % 2 == 0

# print(is_even(5))

# even = lambda num: num % 2 == 0

# print(even(4))

# multiply = lambda num_1, num_2: num_1 * num_2

# print(multiply(5,3))

# SCOPE

y = 20

# def add_5():
#     global y
#     print("y in function", y)
#     y += 5
#     print("y in fucntion after adding 5", y)
#     if True:
#         y = 99
#         print("in if block", y)
#     print("back in function", y)

# add_5()
# print("global y", y)

# def my_function(num_1, num_2, num_3=5, *args, **kwargs):
#     print(num_1, num_2, num_3)
#     print("args", args)
#     print("kwargs", kwargs)


# my_function(4, 6, 8, 10, 12, 14, num_4 = 16, num_5 = 18)


# LISTS


items = [1, None, True, [1, 2, 3], "Turkey"]

empty = []

foods = ["tacos", "burger", "pizza", "wings"]

# print(foods[1:3])
# print(foods[::-1])
# print(len(foods))
# foods.append("steak")
# print(foods)
# foods.extend(["salad", "sloppy joes"])
# print(foods)
# foods.pop(2)
# print(foods)
# foods.remove("burger")
# print(foods)
# foods.sort()
# print(foods)

vals = [2, 4, 6, 8, 10]
print(sum(vals))
print(min(vals))
print(max(vals))
