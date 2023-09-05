# FUNCTIONS
# def get_average(num_1, num_2):
#     """This function will accept 2 numbers and return 
#     their average"""
#     average = (num_1 + num_2) / 2
#     print(average)
#     return average

# ran_average = get_average(2, 4)
# print(ran_average)
# help(get_average)

# STRINGS
# lunch = "Pizza"
# print(lunch)
# print(len(lunch))

# print('Pizza')
# print("Pizza")
# print("Let's")
# print('Let\'s')
# print(""" THIS IS 
# a multi line string
# where spaces
# and 
# new lines
# are preserved
# """)

a=1
b=2
# print(a)
# a = "Pizza"
# print(a)

# LUNCH_FOOD = "Pizza"

# print(LUNCH_FOOD)
# LUNCH_FOOD = "Wings"
# print(LUNCH_FOOD)
# print(f"Let's add {a} and {b} together to get {a + b}")
# print("Let's add {1} and {0} together to get {2}".format(a, b, a + b))
# print("Let's add {thing2} and {thing1} together to get {thing3}".format(thing1=2, thing2=3, thing3=3))

# print('Pizza ' + "is " + "so yummy!")
# print("Pizza" * 3)

sentence = "Brad is very much obsessed with pizza today!"

# print(sentence[2])
# print(sentence[-3])
# print(sentence[start:stop:step])
# print(sentence[:5])
# print(sentence[1:-2])
# print(sentence[::-1])
# print(sentence.split("a"))
# print(list(sentence))

# names = ['Dan', "Brad", "Andrew", 'David']
# join_str= ", "
# print(join_str.join(names))

# BOOLEANS
a = True
b = False

# && || !
# and or not 
# print(True and False)
# print(True or False)
# print(False and True)
# print(False and False)
# print(not True)
# print( True + 1 )
# print( False + 1 )
# print( True == 1 )
# print(1 is True)
# # != 
# ==
# print(1==2)
# print(1!=2)
# print(1_000_000_000 == 1000000000)
# print(1_000_000_000)


# NUMBERS 
# result = 2.0 * 4
# print(result)
# print(int(result))
# other_result = 4 / 2
# print(other_result)
# yet_another_result = 5 // 2
# print(yet_another_result)
# print(int('4'))
# print(str(4))
# print(float(5))

# Operators
# + - * / % ** //

# print(4**2)

# def long_division(dividend, divisor):
#     """Takes in 2 numbers and return their result and remainder"""
#     quotient = dividend // divisor
#     remainder = dividend % divisor
#     print(quotient, remainder)
#     return f"{dividend} divided by {divisor} is {quotient} remainder {remainder}"


# print(long_division(25, 3))


# VARIABLES

# num_1 = 40
# print(num_1)
# num_1 += 1
# print(num_1)

# num_1 = "Tacos"
# print(num_1)

# bags = cases = 50
# print(bags, cases)

# DESSERT = "ice cream"

# Identity vs equality
#   is     vs  ==

my_int = 4
my_float = 4.0

# print(my_float == my_int)
# print(my_float is my_int)


# print("2" == '2')
# print('2' is "2")

# a = None
# print(id(a))
# b = "pizza"
# print(id(b))
# c = None 
# print(id(c))
d = True
print(id(d))
e = 1
print(id(e))
f = True
print(id(f))
print(e == f)
print(e is f)
print(d is f)