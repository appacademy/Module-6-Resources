# XOR

# print(True ^ True)
# print(True ^ False)
# print(False ^ True)
# print(False ^ False)

# IF STATEMENTS

def breakfast(food):
    # function scope
    solid_breakfasts = ["pancakes", "waffles", "eggs", "oatmael", "cereal"]
    if food == "waffles":  
        print(f"{food} is my favorite breakfast!")
    elif food == "pancakes":
        print(f'{food} is great, hope they had blueberries!')
    elif food in solid_breakfasts:
        print(f'{food} is a solid breakfast!')
    else:
        # not a new scope
        print("Do you know what breakfast even is???")


# breakfast("waffles")
# breakfast("pancakes")
# breakfast("cereal")
# breakfast("ice cream")

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
# # 0b0
# # 0b1
# print(bin(5))
# print(bin(3))
# #0b101
# #0b011
# #  110
# print(bin(6))

# STRINGS

meal = "breakfast"
food = 'waffles'
long_string = """ THis is a multi
line string
cause it spans
multiple lines
"""

# print(meal, food)
# print(long_string)

# print(f"Brad had {food} for {meal} today!")

# a = "a"
# b = 'b'
# an = 'an'
# print(b + an)
# print(b + (7 * a))
# print(b + an*2 + a)

# print(food[start:stop:step])
# print(food[1:3])
# print(food[::-1])

# print(food.index("aff"))
# print(food.count("q"))
# print(food.split('f'))
# print(list(food))

# letters = ['a', 'b', 'c', 'd']
# print(','.join(letters))


# Write your function, here.
# def is_palindrome(str):
#     # reverse = ''.join(reversed(str))
#     # return str == reverse
#     return str == str[::-1]

# is_palindrome = lambda str: str == str[::-1]

# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False



# Write your function, here.
def recursive_string(string):
    if len(string) == 0:
        return string
    return recursive_string(string[1:] + string[0])
    

# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) # noitacilppa


# Write your function, here.
# def long_burp(n):
#     # r = 'r' * n
#     return f"{'r' * n}rp"

# print(long_burp(3))  #> "Burrrp"
# print(long_burp(5))  #> "Burrrrrp"
# print(long_burp(9))  #> "Burrrrrrrrrp"



# RECURSIVE COUNTDOWN
# def recursive_countdown(n):
#     if n <= 0:
#         return
#     else:
#         print(n)
#         recursive_countdown(n - 1)


# recursive_countdown(900) #> 5 4 3 2 1

# RECURIVE FIBONACCI
# def recursive_fib(num):
#     if num <= 1:
#         return num
#     else:
#         return recursive_fib(num -1) + recursive_fib(num -2)
        


# print(recursive_fib(1))     #> 1
# print(recursive_fib(2))     #> 1
# print(recursive_fib(4))     #> 3
# print(recursive_fib(6))     #> 8
# print(recursive_fib(12))    #> 144



# variable_1 = 1
# print(id(variable_1))
# variable_2 = 1
# print(id(variable_2))

# print(variable_1 == True)
# print(variable_1 is True)


# Write your function, here.
def first_before_second(s, first, second):
    first = s.rindex(first)
    second = s.index(second)
    return first < second



# Write your function, here.
def first_before_second(s, first, second):
    return s.rindex(first) < s.index(second)

## Here's another variant, with the while loop
def first_before_second_while(s, first, second):
    first_last_index = 0
    second_first_index = 0
    i = 0
    while i < len(s):
        if s[i] == first:
            first_last_index = i
        i += 1
    i = 0
    while i < len(s):
        if s[i] == second:
            second_first_index = i
            break
        i += 1
    return first_last_index < second_first_index


# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# print(first_before_second("happy birthday", "a", "y"))
# print(first_before_second("precarious kangaroos", "k", "a"))


# WHILE LOOPS
# index = 0
# while index < 5:
#     print(f"{index}.  Hello Programmers!")
#     index += 1

# print("while loop done!")

# index = 0
# while True:
#     if index < 5:
#         print(f"{index}.  Hello Programmers!")
#         index += 1
#         continue

#     print("index is now >= 5")
#     break

# print("while loop done!")

import random
import time
import os

count = 99

# while count < 1000:
#     os.system("clear")
#     print(f"{count} little bugs in our code...")
#     time.sleep(1)
#     print(f"{count} pesky little bugs...")
#     time.sleep(1)
#     print("Take one down and patch it around...")
#     time.sleep(1)
#     new_bugs = random.randint(1, 100)
#     count += new_bugs
#     print(f"{count} little bugs in our code!")
#     time.sleep(1.5)




# FOR LOOPS

foods = ["pizza", "tacos", "wings", "waffles", "salad"]

# for food in foods:
#     print(food)


# print("tacos" in foods)
# print("burger" in foods)


# range(start, stop, step)

# new_range = range(11)
# print(list(new_range))

# for index in range(len(foods)):
#     print(index, foods[index])


# TRY/EXCEPT


# try:
#     num = int(input("Enter something to divide by 4: "))
#     print("In try in try block")
#     value = 4/num

# except ZeroDivisionError:
#     print("We can not divide by zero!")

# except TypeError:
#     print("We can't divide numbers by words!")

# except ValueError:
#     print("We need number values please")

# else:
#     print("If our try block was successful, we will see this!")
#     value += value + 25
#     print(value)

# finally:
#     print("You are going to see this every time, promise!")



# SEQUENCE OF NUMBERS
# Write your function, here.
def seq_of_numbers(seq):
    seq += " "
    count = 1
    index = 0
    results = ''

    while index < len(seq) - 1:
        if seq[index] != seq[index + 1]:
            results = results + str(count) + seq[index] + ","
            count = 1
        else:
            count += 1
        index += 1
    return results

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


# FUNCTIONS
def is_even(num):
    """returns a bolean if the given number is even or not"""
    return num % 2 == 0

# print(is_even(5))

# even = lambda num: num % 2 == 0

# print(even(5))

# multiply = lambda num_1, num_2: num_1 * num_2

# print(multiply(5, 10))

# SCOPE
PI = 3.14
# y = 200
# y += 10
# print("outside function", y)

# def some_function():
#     global y
#     print("inside the function", y)
#     # print(PI)
#     if True:
#         print("inside if block", y)
#         y += 10
#     y += 50
#     print("second time in function", y)

# some_function()

# print("second outside function", y)

# def my_func(num_1, num_2, num_3 = 5, *args, **kwargs):
#     print(num_1, num_2, num_3, args, kwargs)



# my_func(10, 15, 25, 30, 35, 40, num_7=45, num_8=50)


# LISTS
dinners = ["tacos", "salad", "pasta", "pizza", "fajitas"]

# print(dinners[0:4])
# print(dinners[::-1])
# print(len(dinners))
# dinners.append("steak")
# print(dinners)
# dinners.extend(["wings", "sloppy joes"])
# print(dinners)
# dinners.insert(1, "chicken cordon blue")
# print(dinners)
# dinners.remove("wings")
# print(dinners)

vals = [2, 6, 1, 7, 9, 4]
vals.sort()
print(vals)
print(sum(vals))
print(min(vals))
print(max(vals))