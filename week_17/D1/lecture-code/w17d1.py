# FUNCTIONS

# Convention for a constant variable
IMPORTANT_VARIABLE = 3.14
average = "Average"

def get_average(num_1, num_2):
    """This function takes in two number 
    and return their average"""
    average = (num_1 + num_2) / 2
    print(average)
    return average
    print("Never gonna see this")


# ran_average = get_average(4, 6)
# print(ran_average)

# help(get_average)

# STRINGS
lunch = "Pizza"
dinner = 'Hamburger'
# print(lunch)

# print("Let's")
# print('Brad said, "Python version 3.9.4 is the best one!"')
# print('let\'s')
# print("""This is a multi
# line string
# it will preserver new lines
# and such
# """)

# a = 1
# b = 2
# c = []
# # print(a)
# # a = 'Pizza'
# # print(a)
# LUNCH = "Pizza"

# print(f"Let's add {a} and {b} together to get {a + b}")
# print("Let's add {0} and {2} together to get {1}".format(a, a + b, b))
# print("Let's add {thing1} and {thing3} together to get {thing2}".format(thing1=a, thing2=a + b, thing3=b))


# print('{:,}'.format(123_456_789))
# print(123_456_789)

# print("Pizza" + " is" + " great!")
# print("Pizza! " * 4)

sentence = 'Brad is very much obsessed with pizza today!'

# print(sentence[3])
# print(sentence[-4])
# print(sentence[start:stop:step])
# print(sentence[::-1])
# print(sentence.split('a'))
# print(list(sentence))

names = ['Brad', 'David', 'Andrew', 'Keegan']
join_str = ', '
# print(join_str.join(names))

# print(len(sentence))



# BOOLEANS
a = True
b = False

# && || !
# and or not

# print(True and False)
# print(True or False)
# print(not True)
# print(True + 1)
# print(False + 2)
# print(True == 1)
# print(True != 1)

# NUMBERS
# result = 2.0 * 4.0
# print(result)
# print(int(123.45))
# print(float(4))
# print(int("1234"))
# print(str(1234))

# + - * / % // **
# print(4**2)

def long_division(dividend, divisor):
    """Takes in 2 numbers and returns their result and remainder"""
    quotient = dividend // divisor
    remainder = dividend % divisor
    print(quotient, remainder)
    return f'{dividend} divided by {divisor} is {quotient} remainder {remainder}'


# print(long_division(25, 3))

# VARIABLES
# x = 1
# num = 40
# num += 1

# TODAYS_DAY = "Monday"

# TODAYS_DAY = "Wednesday"
# print(TODAYS_DAY)

# bags = 50
# cases = 50
# print(bags)
# print(cases)
# print( (1 + 2) * 3)


# IDENTITY vs EQUALITY
#    is    vs  ==

my_int = 4
my_float = 4.0

# print(my_float == my_int)
# print(my_float is my_int)

# print("2" == '2')
# print("2" is '2')


# a = None
# print(id(a))
# b = None 
# print(id(b))
# print( a is b )
# lunch = "pizza"
# print(id(lunch))
# dinner = 'pizza'
# print(id(dinner))

val = 1
print(val is True)