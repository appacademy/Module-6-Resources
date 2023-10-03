# XOR

# print(True ^ False)
# print(True ^ True)
# print(False ^ False)
# print(False ^ True)

# IF Statements

def breakfast(food):
    """takes in a food string and judges your breakfastchoices"""
    if food == 'waffles':
        print(f"{food} are my favorite breakfast!")

    elif food == "pancakes":
        print(f"{food} are pretty delicious, but not waffles")
    
    else:
        print(f"{food} is okay, but not waffles")


# breakfast("waffles")
# breakfast("cereal")
# breakfast("pancakes")


# XOR
# def xor(x, y):
#     return x ^ y


# print(xor(False, False))   #>  False
# print(xor(True, False))   #>  True
# print(xor(True, True)) #>  False
# print(xor(5, 3))  #> 6
# # print(xor(8, 4))  #> 12
# # print(xor(2, 2))  #> 0
# # print(xor(1, 2))  #> 3
# # print(xor(4, 4))  #> 0
# # print(bin(True))
# # print(bin(False))

# # 0b1
# # 0b0
# print(bin(5))
# print(bin(3))
# # 0b101
# # 0b011
# #   110
# # 0b110
# print(bin(6))


# #STRINGS

# lunch = "tacos"
# dinner = 'more tacos'

# lots_of_meals = ''' waffles, bacon
# sandwich, pizza, motz sticks,
# tacos, burritos, ice cream
# '''
# a = "a"
# b = "b"
# an = "an"

# print(b + an)
# print(b + a * 7)
# print(b + an * 2 + a)
# print(100_000_000_000)

# breakfast = "waffles"

# print(breakfast[-2])
# # print(breakfast[start:stop:step])
# print(breakfast[-3:])
# print(breakfast[::-1])

# # print(breakfast.index("x"))
# print(breakfast.find("x"))
# print(breakfast.count("f"))
# print(breakfast.upper())
# print(breakfast.split())
# print(list(breakfast))

# def function_that_saves_the_world():
#     """this will save all humanity"""

# function_that_saves_the_world()

# more_foods = ["apple", "banana", "oramnge"]
# print(", ".join(more_foods))


# STRING Problems
# def is_palindrome(string):
#     # return string == string[::-1]
#     reverse = ''.join(reversed(string))
#     return string == reverse


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

    return recursive_string(string[1:]) + string[0]
            
#                 #ivic     + c
#                             #vic + i
#                             #ic + v
#                             #c   + i
#                             #c     

# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) # noitacilppa


# number_of_tacos = 10
# number_of_tacos += 1
# print(number_of_tacos)

# taco = "taco"
# taco += "s"
# print(taco)


# def perfect_square(square, num):
#     return num**2 == square


# print(perfect_square(15, 5))  # > False
# print(perfect_square(25, 5))  # > True
# print(perfect_square(81, 9))  # > True
# print(perfect_square(9, 2))  # > False


# def recursive_countdown(num):
#     if num == 0: # base case
#         return

#     else: # recursive step
#         print(num, end=" ") # end appends the value given to the string printed - the default is "\n" (newline)
#         recursive_countdown(num - 1)


# recursive_countdown(5)  # > 5 4 3 2 1


# list_1 = [1, 2, 3]
# list_2 = [1, 2, 3]

# print(list_1 == list_2) # True, the values in the lists are the same

# print(list_1 is list_2) # False, they are two different objects, the addresses are different

# list_3 = list_1

# list_1[0] = 10

# print(list_1 is list_3) # True

# print(list_3)

# print(id(list_1))
# print(id(list_2))
# print(id(list_3)) # same memory address as list_1 because they are the same object!

# a = 5
# b = 6

# print((a == b) is False) # True

# a = "5"
# b = "5"

# print(a is b) # True

# print(id(a)) # These two variables share the same memory
# print(id(b)) # address, due to a mechanism know as interning


# # Write your function, here.
# def first_before_second(str, letter1, letter2):
#     print(str(1))
#     return str.rindex(letter1) < str.index(letter2)



# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# #> True
# # Every instance of "a" occurs before every instance of "j".

# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# #> True

# print(first_before_second("happy birthday", "a", "y"))
# #> False
# # The "a" in "birthday" occurs after the "y" in "happy".
# print(first_before_second("precarious kangaroos", "k", "a"))
#> False

# STATEMENTS

index = 0

# while index < 5:
#     if index == 3:
#         print('We got a 3!!!')

#     else:
#         print(index, "Not a 3!!")

#     index += 1


# while True:
#     if index == 5:
#         break
#     elif index == 3:
#         print('We got a 3!!!')
#     else:
#         print(index, "Not a 3!!")

#     index += 1    

# i = 0
# while True:
#     print(f"{i}. Hello, world.")
#     if i < 4:
#         i += 1
#         continue
#     print("You've printed 5 times. Goodbye.")
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
#     new_bugs = random.randint(10, 100)
#     count += new_bugs
#     print(f"{count} little bugs in our code!")
#     time.sleep(2)



# for food in foods:
#     print(food)

# print("banana" in foods)
# print("tacos" in foods)

# range(start, stop, step)
# first_range = range(0, 7, 2)
# print(first_range)
# print(list(first_range))

# for integer in range(5):
#     print(integer)

# foods = ["tacos", "wings", "pizza", "tuna salad", "carrots"]


# for index in range(len(foods)):
#     print(index, foods[index])


# TRY/EXCEPT
# num = "pancakes"
# # print(5/num)

# try:
#     print("In the try block")
#     print(5 / num)



# except ZeroDivisionError:
#     print("We can't divide by zero!")

# except TypeError:
#     print("We can't do math with strings!!!")

# # except:
# #     print("an error has occurred!")

# else:
#     print("You only see me if the try block ran successfully")

# finally:
#     print("I am going to print this whether you like it or not")


# def seq_of_numbers(seq):
#     seq += " "
#     count = 1
#     # index = 0 
#     results = ''

#     # while index < len(seq) - 1:
#     for index in range(len(seq)-1):
#         if seq[index] != seq[index+1]:
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
#     """lets us know if a number is even"""
#     return num % 2 == 0

# print(is_even(7))

# even = lambda num: num % 2 == 0

# print(even(6))

# multiply = lambda num1, num2: num1 * num2
# print(multiply(2, 4))


# SCOPE
# PI = 3.145

# y = 200
# print("gobal scope", y)

# def some_function():
#     # y = 10
#     global y
#     print("in the function", y)
#     print(PI)
#     y += 10
#     print("in the function 2nd", y)

# some_function()

# print("global 2nd", y)

dinner = ["tacos", "pizza", "sloppy joes", "burgers", "cobb salad"]

# another_list = [1, True, "iphone", None, 5.25]
# print(dinner[0:])
# print(dinner[::-1])
# print(len(dinner))
# dinner.append("hot dogs")
# print(dinner)
# dinner.extend(["chicken pot pie", "ice cream"])
# print(dinner)
# dinner.insert(1, "burittos")
# print(dinner)
# dinner.remove("pizza")
# print(dinner)
# dinner.pop(1)
# print(dinner)
# dinner.sort()
# print(dinner)

vals = [1, 2, 3, 4, 5]
print(sum(vals))
print(max(vals))
print(min(vals))