# W17 D1

# FUNCTIONS
# def get_average(num_1, num_2):
#     """This function will accept two numbers and return 
#     their average"""
#     average = (num_1 + num_2) / 2
#     print(average)
#     return average

# ran_average = get_average(4, 6)
# print(get_average(4, 6))
# help(get_average)


# n = 12
# num = 12
# dividend = 12


# STRINGS
# lunch = "Pizza"
# print(lunch)
# print(len(lunch))

# print('Pizza')
# print("Let's")
# print('Let\'s')
# print(''' This is a very
# very very
# very multi
# line string
# ''')

# LUNCH = "Pizza"

# LUNCH = 5
# print(LUNCH)

# String Formatting
# a = 1
# b = 2

# print(f'Let\'s add {a} and {b} together to get {a + b}')
# print("Let's add {1} and {0} together to get {2}".format(a, b, a+b))
# print("Let's add {thing1} and {thing2} together to get {thing3}".format(thing3=a + b, thing1=a, thing2= b))


# String Math

# print("Pizza" + " is " + "delicious!")
# print("Pizza " * 4 )
# print("Pizza" + 4)


# String Indexing
sentence = "Brad is very much obsessed with pizza today..."

# print(sentence[1])
# print(sentence[-1])
# print(sentence[-5])
# print(sentence[start:stop:step])
# print(sentence[1:7])
# print(sentence[5:])
# print(sentence[8:13])
# print(sentence[::2])
# print(sentence[::-1])
# print(sentence.split('a'))
# print(list(sentence))

# names = ["Brad", "David", "Andrew", "Keegan"]
# join_str = ", "
# print(join_str.join(names))


# Boolean
a = True
b = False

# && || !
# and or not
# !=   ==
# print(False and True)
# print(True or False)
# print(not True)
# print(True + 1)
# print(False + 1)
# print(True is 1)


# Numbers
# result = 2 * 4
# print(result)
# results2 = 2.0 + 5
# print(results2)
# print(int("1234"))
# print(float(234))
# print(int(23.5))

# + - * / % ** //

# print(4**2)

def long_division(dividend, divisor):
    """Take in 2 numbers and returns their result and remainder"""
    quotient = dividend // divisor
    remainder = dividend % divisor
    print(quotient, remainder)
    return f"{dividend} divided by {divisor} is {quotient} remainder {remainder}"


# print(long_division(25, 3))

# print(25 / 3)
# print(25 // 3)


# Variables

num1 = 40
num1 += 1

DINNER = "Wings"

# bags = cases = 50
# print(bags)
# print(cases)


# IDENTITY vs EQUALITY
#  In JS == equality === (type and equality check)

my_int = 4
my_float = 4.0

print( my_float == my_int )
print( my_float is my_int)

# print( "2"  == '2')
# print( '2' is "2")

# a = None
# print(id(a))
# b = None
# print(id(b))
# print(a is b)
# a = "Pizza"
# print(id(a))
# print(a is b)
print(True == 1)
print(True is 1)