# # FUNCTIONS

# def get_average(num_1, num_2):
    # """This function will accept 2 numbers 
    # and return their average"""
#     average = (num_1 + num_2) / 2
#     print(average)
#     return average


# ran_average = get_average(4, 6)
# print(ran_average)

# help(get_average)

# If we need 
# a multi line comment
# STRINGS

# lunch = "Pizza"
# lunch_2 = 'Sandwich'

# print(lunch)
# print(len(lunch_2))

# print("Let's")
# print('Lets\'s')
# print('''This is a
# multi line
# string so spaces
# and new 
# lines are
# preserved''')


a = 1
b = 2
# print(a)
# a = "Pizza"
# print(a)

# LUNCH = "pizza"
# LUNCH = 2
# print(LUNCH)

# print(f"Let's add {a} and {b} together to get {a + b}")
# print("Let's add {1} and {2} together to get {0}".format(a, b, a+b))
# print("Let's add {thing_1} and {thing_2} together to get {thing_3}".format(thing_3=a+b,thing_1=a, thing_2=b))


# print("Pizza" + " is " + "delicious")
# print("pizza " * 4)

sentence = 'Brad is very much obsessed with pizza and food'
# print(sentence[0])
# print(sentence[-2])
# # print(sentence[start:stop:step])
# print(sentence[1:6])
# print(sentence[:10])
# print(sentence[::2])
# print(sentence[::-1])

# names = ["Brad", "David", "Andrew", "Keegan"]
# join_str = ", "
# print(join_str.join(names))

# DO NOT EDIT - Sample debug for an equality operation
# num = 5
# string = "5"
# print('num {0}, str {1}, equal? {2}'.format(num, string, num==string))

# # STEP 6: Rewrite the print above in an alternate way using f' on the string
# print(f'num {num}, str {string}, equal {num==string}')


# BOOLEAN
a = True
b = False

# && || !
# and or not 
# print(True or False)
# print(False and True)
# print(not True)
# print(True and True)

# print( 1 == 2)
# print( 2 != 3)
# print( 3 == "3")

# print(True + 1)
# print(False + 3)
# print(True == 1)


# NUMBERS
# Integer & Floats
# results = 2 * 4
# print(results)
# value = 23445
# val_2 = 3.14

# print(int("2345"))
# print(float(1234))
# print(int(250.25))
# print(float("23.6"))

# Operators
# + - * / % ** // 
# print(4**2)

def long_division(dividend, divisor):
    """Takes in 2 numbers and calculates the quotient and remainder"""
    quotient = dividend // divisor
    remainder = dividend % divisor
    print(quotient, remainder)
    return f"{dividend} divided by {divisor} is {quotient} reaminder {remainder}"

# print(long_division(25, 3))

# number = 40
# number += 1

# ORDER OF OPERATIONS
# Parenthesis Exponents Multiplication Division Addition Subtraction

#  VARIABLES

# age = 40
# x = 40
# PI = 3.14

# bags = cases = 50
# print(bags)
# print(cases)


# IDENTITY vs EQUALITY
#   is     vs  ==

# my_int = 4
# my_float = 4.0

# print(my_int == my_float)
# print(my_int is my_float)

# print("2" == '2')
# print("2" is '2')

a = None
print(id(a))
b = 'pizza'
print(id(b))
c = None
print(id(c))
d = True
print(id(d))
e = True
print(id(e))
print( a is c)
print(d is e)
print(a is b)
f = 1
g = 0
print(id(f))
print(id(g))
print(f is d)