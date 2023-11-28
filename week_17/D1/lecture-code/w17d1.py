# FUNCTIONS

# def get_average(num1, num2):
#     """This function takes in 2 numbers as 
#     arguements and returns their average"""
#     # This is a comment
#     average = (num1 + num2) / 2
#     print(average)
#     return average


# print(get_average(4, 6))
# help(get_average)

# other_get_average = lambda num1, num2: (num1 + num2) / 2
# print(other_get_average(2,4))

# STRINGs
# lunch = "pizza"
# dinner = 'hamburger'
# print(lunch)
# print(len(dinner))

# print("pizza")
# print('pizza')
# print("let's eat pizza")
# print('let\'s eat pizza')
# print(''' This is a multi
# line string that does preserver new 
# lines and
# spac es  !''')

# # STRING FORMATTING
# a = 1
# b = 2
# # print(a)
# # a = "pizza"
# # print(a)

# LUNCH = "pizza"
# LUNCH = "SALAD"
# print(LUNCH)

# print(f"Let's add {a} and {b} together and get {a + b}")
# print("Let's add {} and {} together and get {}".format(a, b, a + b))
# print("Let's add {1} and {0} together and get {2}".format(a, b, a + b))
# print("Let's add {thing1} and {thing3} together and get {thing2}".format(thing3=a, thing2=b, thing1=a + b))

# print("Pizza" + " is " + "awesome!")
# print("Pizza " * 4)

# INDEXING
# sentence = "Brad is very much obsessed with pizza today!"

# print(sentence[-2])
# # print(sentence[start:stop:step])
# print(sentence[5:])
# print(sentence[1:12:2])
# print(sentence[::-1])
# print(sentence.split("s"))
# print(list(sentence))

# names = ["Brad", "David", "Andrew", "Dan"]
# join_str = ", "
# print(join_str.join(names))

# BOOLEANS
a = True
b = False

# && || !
# and or not

# print(True or False)
# print(True and False)
# print(False and True)
# print(not True)

# print(1 == 1)
# print(2 != 1)
# print("The thing JS struggles with...", 4 == "4")

# print(True + 1)
# print(False + 1)

# print(True == 1)
# print(1 is True)

# NUMBERS
# num1 = 123
# num2 = 123.023
# print(str(num1))
# print(int(num2))
# print(float(num1))

# # + - * / % ** //

# print(4**2)

# print(5/2)
# print(5//2)
# print(4/2)
# print(4//2)


# def long_divison(dividend, divisor):
#     """ function that takes in 2 numbers and returns 
#     their quotient and remainder"""
#     quotient = dividend // divisor
#     remainder = dividend % divisor
#     print(quotient, remainder)
#     return f"{dividend} divided by {divisor} is {quotient} remainder {remainder}"


# print(long_divison(25, 3))

# VARIABLES
# integer1 = 34
# integer1 += 1
# print(integer1)

# DINNER = "grilled cheese sandwich"

# bags = cases = boxes = 50

# print(bags, cases, boxes)

# big_num = 1_000_000_000_000

# other_num = 1000000000000
# print(big_num, other_num)


# IDENTITY vs EQUALITY
#    is     vs    ==

# my_int = 4
# my_float = 4.0

# print(my_float == my_int)
# print(my_float is my_int)


# print("2" == '2')
# print('2' is "2")


a = None
print(id(a))
b = "pizza"
print(id(b))
c = None
print(id(c))
print(a is c)
d = True
print(id(d))
e = 1 
print(id(e))
f = True
print(id(f))

print(e is True)
print(e == True)
print(bin(True))

print(None == None)