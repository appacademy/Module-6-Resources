# FUNCTIONS

# def get_average(num1, num2):    
#     """accetps 2 numbers and 
#     returns their average"""
#     average = (num1 + num2) / 2
#     # print(average)
#     return average


# print(get_average(5, 10))
# help(get_average)

# STRINGS
# lunch = "pizza"

# print(lunch)
# print(len(lunch))

# print('pizza')
# print("pizza")
# print("let's eat pizza")
# print('lets\'s eat some pizza')

# long_string = """ this is 
# going to preserve all spaces 
# as well       as any
# new lines
# """
# print(len(long_string))

a = 1
b = 2
# print(a)
# a = "pizza"
# print(a)

# LUNCH = "pizza"
# print(LUNCH)
# LUNCH = False
# print(LUNCH)


# string interpolation
# print(f"Let's add {a} and {b} together to get {a + b}")

# print("Let's add {1} and {0} together to get {2} ".format(a, b, a+b))

# print("Let's add {thing1} and {thing3} together to get {thing2}".format(thing2=b, thing1=a, thing3=a+b))


# STRING MATH
# print("Pizza " + "is super" + " duper awesome!" )
# print("Pizza! " * 3)

# INDEXING
# sentence = "Brad is very much obsessed with pizza today"

# # print(sentence[-1])
# # # print(sentence[start:stop:step])
# # print(sentence[:5])
# # print(sentence[::-1])
# print(sentence.split("a"))
# print(list(sentence))
# names = ["Brad", "David", "Andrew", "Dan"]
# join_str = ", "
# print(join_str.join(names))

# BOOLEANS

# a = True
# b = False

# && || !
# and or not 

# print(True and True)
# print(False and True)
# print(True or False)
# print(False or False)
# print(not True)
# print(1 != 2)
# print(1 == 2)

# print('4' == 4)
# print(True is 1)
# print(False is 0)
# print(2*True)


# NUMBERS

# integer = 12
# num = int(123.5)
# my_float = float(integer)
# print(num)
# print(my_float)
# print(int("1234"))
# print(int("hello"))

# + - / * % ** //
# print(4**2)
# print(5/3)
# print(5//3)

# print(6/2)
# print(6//2)


# print(1_000_000_000_000)
# float = 

# def long_division(dividend, divisor):
#     """takes in 2 numbers and returns their results """
#     quotient = dividend // divisor
#     remainder = dividend % divisor
#     print(quotient, remainder)
#     return f"{dividend} divided by {divisor} is {quotient} remainder {remainder}"


# print(long_division(25, 3))

# counter = 1
# counter += 1


# Variables

# dinner = "Tacos"
# a = "tacos"
# x = 4
# meals = 4

# meals = "clock"
# print(meals)
# MEALS_PER_DAY = 3
# PI = 3.145

# bags = cases = boxes = 50
# print(bags, cases, boxes)


# Identity vs Equality

#   is         ==

# print(4 == 4.0)
# print('2' == "2")
# print(True == 1)

a = None
print(id(a))
b = 'pizza'
print(id(b))
c = None
print(id(c))
d = 1
print(id(d))
e = True
print(id(e))
f = 1
print(id(f))

print(e == f)
print(e is f)