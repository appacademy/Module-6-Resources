# print( True ^ True)
# print( True ^ False)
# print( False ^ True)
# print( False ^ False)

# && || !
def breakfast(food):
    val = 5
    if food == "waffles":
        val = 6
        print(f'{food} are my favorite breakfast')
    elif food == "pancakes":
        print(f"{food} are pretty good")
    elif food == "french toast":
        print(f"{food} yummy!  I hope you have syrup")
    else:
        print('That does not sound like a great breakfast')


# breakfast("waffles")
# breakfast("french toast")
# breakfast("eggs")

# if True:
#     print("this code will evaluate")



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
# 0b1
# 0b0
# 0b1
# print(bin(5))
# print(bin(3))
#0b101 - bin(5)
#0b011 - bin(3)
#0b110
# print(bin(6))
#0b110


# STRINGs
meal = "breakfast"
food = 'bagels'
multiline =""" this is 
a multiple line 
string """

# print(f"We are eating {food} for {meal}")

a = 'A'
b = 'B'
an = "an"

# print(b + an) 
# print(b + an * 7)
# print(b + an * 2 + a)

food = "waffles"
foods = ["pancakes", "eggs", "bacon"]

# print(food[0:4:2])
# print(food[-2:])
# print(food.index("ff"))
# print(food.count("f"))
# print(food.split("f"))
# print(food.upper())
# print(", ".join(foods))


# NUMBERS
a = 2
a += 1

# EQUALITY vs IDENTITY

my_int = 4
my_float = 4.0
 
# check if the values are the same
# print(my_int == my_float)  # True
 
# check if the values are the same and check type
# print(isinstance(my_int, str)) 

# python version
a = 5
b = 5
# print(a is b) # True
 
c = "hey"
d = "hey"
# print(c is d) # True


# STATEMENTS
# index = 0
# while index < 5:
#     if index == 3:
#         print("hey we got a 3!")
#     else:
#         print("nope, not a 3")
#     index += 1


# i = 0
# while True:
#     print(f"{i}. Hello, world.")
#     if i < 4:
#         i += 1
#         continue
#     print("You've printed 5 times. Goodbye.")
#     break

# for i in range(0,5):
#     print(f"{i}. Hello, world.")
#     if i < 4:
#         i += 1
#         continue
#     print("You've printed 5 times. Goodbye.")
#     break


instructors = ['Brad', 'Drew', 'Cesar', 'David']

# for instructor in instructors:
#     print(f"{instructor} is a cool dude")
     

# for index in range(len(instructors)):
#     print(f"{index}. {instructors[index]}")

# print("Brad" in instructors)
# print("John" in instructors)

# my_range = range(0,10,1)
# print(list(my_range))


# TRY/EXCEPT

try:
    # code we hope runs correctly
    pass
except TypeError:
    # code that will inform us of an error
    pass
except ZeroDivisionError:
    # code that will inform us of an error
    pass
else:     
    # code that runs if the try is successful
    pass
finally:
    # this will run no matter what
    pass

# num = "potato"
# print(4/num)
def math(num):
    try:
        print("In the try block")
        print(4/num)
        # try to connec to a DB here
        try:
            print('Hey there')
        except:
            pass
        finally:
            print("nested try/except oh my")
    except TypeError:
        print("we can't do with math with non numbers")
    except ZeroDivisionError:
        print('we can not divide by zero!')
        # catostrophic connect error, we are all gonna die
        return 4
    else:     
        print("YAY we successfully did math!")
    finally:
        print("Hopefully you see this every time")
        # end the connection to the db

# val = math(2)

# while True:
#     try:
#         num = int(input("say a number "))
#         print(num)
#         break
#     except:
#         print("try again")



# FUNCTIONS
def is_even(num):
    return num % 2 == 0

# print(is_even(5))

even = lambda num: num % 2 == 0
# print(even(4))

multiply = lambda num1, num2: num1 * num2
# print(multiply(2, 10))
PI = 3.14

if True:
    num2 = 10

def make_a_five():
    """ will return a five """
    num3 = num2
    # global num2
    num = 5
    print(num3)
    # num2 +=1
    return num
 
# make_a_five() 
 
# print(num) #10
# # `x` was created in the global scope
# print(num2) # NameError: name 'y' is not defined


# def my_func(num, num2, num3 = 5, *args, **kwargs):
#     print(num, num3, num2)
#     print(args)
#     print(kwargs)

# my_func(3, 4, 4, 6, num5 = 78, num6 = 102)

# LISTS

dinner = [ "tacos", "burger", "pizza", "wings"]

# print(dinner)
# # print(dinner[0:3:2])
# # print(len(dinner))
# dinner.append("salad")
# print(dinner)
# dinner.extend(["mac & cheese", "steak"])
# print(dinner)
# dinner.insert(1, "fajitas")
# print(dinner)
# dinner.remove("wings")
# print(dinner)
# dinner[1] = "burritos"
# print(dinner)

vals = [2, 4, 56, 12, 7]

vals.sort()
print(vals)

print("sum", sum(vals))
print("min", min(vals))
print("max", max(vals))


# Problem 3 - # Write your code here.
def string_multi_print(string):
    return lambda i: print(string * i) 


string_multi_print('hello ')(2)  # Prints "hello hello "
# string_multi_print('wahoo ')(3)  # Prints "wahoo wahoo wahoo "

# Problem 1 - First Before Second
# Write your function, here.
def first_before_second(string, letter1, letter2):
   return string.rindex(letter1) < string.index(letter2)

print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#> True
# Every instance of "a" occurs before every instance of "j".

print(first_before_second("knaves knew about waterfalls", "k", "w"))
#> True

print(first_before_second("happy birthday", "a", "y"))
#> False
# The "a" in "birthday" occurs after the "y" in "happy".

print(first_before_second("precarious kangaroos", "k", "a"))
#> False

def seq_of_numbers(seq):
    # counter
    # iterate - check the whole sequence
    # result variable
    # conditional - check if numbers next to each other are the same
    seq += " "
    count = 1
    index = 0
    results = ''

    while index < len(seq) - 1:
        if seq[index] != seq[index + 1]:
            results = results + str(count) + seq[index] + ','
            count = 1
        else:
            count += 1
        index += 1


    return results



print(seq_of_numbers("1211"))
# This is "one 1, one 2, two 1s"
# Prints "11,12,21"
# 111221

print(seq_of_numbers("111221"))
# This is "three 1s, two 2s, and one 1"
# Prints "31,22,11"

print(seq_of_numbers("31131211131221"))
# This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
#    one 3, one 1, two 2s, and one 1"
# Prints "13,21,13,11,12,31,13,11,22,11"

