def lunch(food):
    if food == 'wings':
        print(f"{food} is my favorite food")
    elif food == 'pizza':
        print(f"{food} is a pretty good lunch")
    else:
        print(f"{food} is just okay")

# lunch('wings')

# XOR
# print( True ^ False)
# print( False ^ False)
# print( True ^ True)
# print( False ^ True)


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
#   1 = T

# print(bin(5))
# print(bin(3))
# 0b101
# 0b011
#   110
# 0b110
# print(bin(6))


# print(f"{word} and {num}")
# print("{} and {}".format("lunch", 3))

# # food = 'wings'
# # print(food.index('w'))
# # another_food = 'banana'
# # print(another_food.count('a'))
# # lunch = "pizza"
# # print(lunch.replace("za", "zzzzzzzzas"))
# # print(lunch)

# # WHILE LOOP
# i = 0

# while i < 5:
#     if i == 3:
#         print(i, "We got to 3!")
#     else:
#         print(i, "Not 3")
#     i += 1

# i = 0
# while True:
#     print(f"{i}. Hello, world.")
#     if i < 4:
#         i += 1
#         continue
#     print("You've printed 5 times. Goodbye.")
#     break
#     print("who wants wings?")


# FOR LOOPS

foods = [ "Pizza", "Wings", "Salad", "Pita"]

# for food in foods:
#     print(food.upper())

# print("Wrap" in foods)

# for num in range(2,11,2):
#     print(num)


# TRY/EXCEPT
# num = 2

# try:
#     print("In the try block")
#     print(4/num)

# except ZeroDivisionError:
#     print("We divided by zero, oops")

# else:
#     print("we are in the else block, no zero division erro")

# finally:
#     print('You are gonna see me no matter what!')


# FUNCTIONS
def is_even(num):
    return num % 2 == 0

# print(is_even(4))

# even = lambda num: num % 2 == 0

# print(even(4))

# multiply = lambda num1, num2: num1 * num2

# print(multiply(2, 5))

Y = 200
Z = 'wings'

DAYS = ["Monday", "Tuesday", "Wednesday"]

def make_a_five():
    """Assign a variable the value of 5"""
    print("Inside function", DAYS)
    return 

# print(y)
# make_a_five()
# print(y)

# print(make_a_five.__doc__)

def my_function(num, num2, num3 = 5, *args, **kwargs):
    pass

foods = [ "pizza", "wings", "taco", "salad"]

# print(foods[-1])
# print(foods[::2])
# print(len(foods))
# foods.append("steak")
# print(foods)
# foods.extend(["buritto", "chicken nuggets"])
# print(foods)
# foods.remove('buritto')
# print(foods)

vals = [2, 4, 56, 12, 7]
vals.sort()
print(vals)
print(sum(vals))
print(max(vals))
print(min(vals))