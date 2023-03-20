# W17 D1

# FUNCTIONS
def get_average(num_1, num_2):
    """This fucntion will accept two numbers and
    return the average"""
    average = (num_1 + num_2) / 2
    print(average)
    return average

# ran_average = get_average(5, 10)
# print(ran_average)
# help(get_average)
# def do_stuff():
#     pass

# STRINGS
# lunch = "Pizza"
# print(lunch)

# print('pizza')
# print("pizza")
# print("Let's")
# print('Let\'s')
# print(''' This is a multi
# line string where spaces
# and new lines are preserved ''')

a = 1
b = 2 
# print(a)
# a = "Pizza"
# print(a)

# LUNCH_CHOICE = "Pizza"
# print(LUNCH_CHOICE)
# LUNCH_CHOICE = "Salad"
# print(LUNCH_CHOICE)

# STRING FORMATTING

# print(f"Let's add {a} and {b} together to get {a+b}")
# print("Let's add {1} and {0} together to get {2}".format(a, b, a+b))
# print("Let's add {thing_1} and {thing_2} together to get {thing_3}".format(thing_3=a+b, thing_2=b, thing_1=a))


# STRING MATH
# print("Pizza" + " is " + "delicious")
# print("Pizza " * 4)


# INDEXING
sentence = "Brad is very much obsessed with pizza today!"
# print(sentence[1])
# print(sentence[-6])
# print(sentence[:])
# print(sentence[:12:2])
# print(sentence[::-1])
# print(sentence[-10:-2])
# [start:stop:step]
# print(sentence.split())
# print(len(sentence))
# print(list(sentence))


# names = ["Brad", "David R", "David N", "Andrew", "Keegan"]
# join_str = " , "
# print(join_str.join(names))


# DO NOT EDIT - Example of a multiline string
# print('''
# Here is a whole bunch of instruction that you'd better follow if you know what's good for you!

# It even includes blank lines. :)
# ''')

# # STEP 1: Write your own print statement on multiple lines


# # DO NOT EDIT
# print('***BEFORE***')

# # STEP 2: Copy the original multiline print and make it show
# # without blank lines at the beginning and the end
# print('''Here is a whole bunch of instruction that you'd better follow if you know what's good for you! It even includes blank lines. :)
# ''')


# dinner = "Cheeseburger"

# print(dinner.find("pizza"))
# print(dinner.index("pizza"))


# BOOLEANS
a = True
b = False

# && || !
# and or not

# print(True and True)
# print(False and True)
# print(True or False)
# print(not True)
# print(True + 1)
# print(False + 1)
# print(True == 1)
# print(True is 1)

# print(3 == 2)
# print(3 != 4)


# NUMBERS
# result = 2 * 4
# print(result)

# my_int = 4
# my_float = 4.5

# print(int("1234"))
# print(float("123.4"))
# print(int(123.45))
# print(float(15))


# big_number = 1_000_000_000
# print(big_number)

# + - * / % ** //

# print(4**2)
# print(10 / 5)
# print(10 / 3)
# print(10 // 3)


def long_division(dividend, divisor):
    """Take in 2 values and return their quotient and remainder"""
    quotient = dividend // divisor
    remainder = dividend % divisor
    print(quotient, remainder)
    return f"{dividend} divided by {divisor} is {quotient} remainder {remainder}"

# print(long_division(25, 3))

# OPERATORS
# += -= *= /= //= %= **=

# VARIABLES
i = 1
index = 1

x = 0
count = 0

COUNT = 0

bags = cases = 50
# print("bags", bags)
# print('cases', cases)


# IDENTITY VS EQUALITY
#  is      vs    ==

my_int = 4
my_float = 4.0

# print(my_float == my_int)
# print(my_float is my_int)

# print("2" == '2')
# print("2" is '2')

# a = None
# print(id(a))
# b = 'pizza'
# print(id(b))
# c = None
# print(id(c))
# d = 'pizza'
# print(id(d))

e = True
print(id(e))
f = 1
print(id(f))
print(e == f)
print( e is f)