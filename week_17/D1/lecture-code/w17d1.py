# FUNCTIONS INTRO

def get_average(num1, num2):
    """This function will accept two
    numbers and return their average """
    average = (num1 + num2) / 2
    print("the average is:", average)
    return average

# ran_average = get_average(4, 6)
# print(ran_average)

# STRING STUFF

lunch = "pizza"
# print(lunch)
# print(len(lunch))

# print("Pizza")
# print('Pizza')
# print("Let's")
# print(""" This is a 
# multi line string filled 
# with lots of great stringy stuff """)

# print(''' This is a multi line string \n filled 
# with lots 
# of great stringy stuff ''')


a = 1
b = 2
# print(a)
# a = 'Pizza'
# print(a)

# LUNCH = "Pizza"

# print(f"Lets add {a} and {b} together to get {a + b} ")
# print("Lets add {} and {} together to get {} ".format(a, b, a + b))
# print("Lets add {thing1} and {thing2} together to get {thing3} ".format(thing3=a+b, thing1=a, thing2=b))


# print("Pizza" + " is" + ' the best')
# print("pizza " * 4)

sentence = "Brad is very much obsessed with pizza today"

# print(sentence[2])
# print(sentence[1:4])
# print(sentence[:-5])
# print(sentence[1:8:2])
# print(len(sentence))

names = ["Brad", "John", "Cesar", 'David'] 
join_str = ' and '
# print(join_str.join(names))


# BOOLEANS

a = True
b = False

# && ||  !
# and or not 
# print(True and False) 
# print(True or False)
# print(False and True)
# print(not False)
# print(True + 1)
# print(False + 1)
# print("pizza" + 1)

# NUMBER STUFF

results = 2 * 4
# print(results)
# print(int('1234'))
# print(float("1235.23"))
# print(float(123))

# data = int(input("Give me some input"))
# print(data)

# + - * / % // **
# 
# print(4**2)  
# print(4/2)
# print(4//2)

def long_division(num1, num2):
    """ function that takes in two values and return the result, and remainder"""
    result = num1 // num2
    remainder = num1 % num2
    print(result, remainder)
    return f'{num1} divided by {num2} equals {result} reaminder {remainder}'


# print(long_division(25, 5))


# IDENTITY vs EQUALITY
#    is    vs    ==

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
# print( a is c)
# d = "pizza"
# print(id(d))
# print(b is d)

print(True == 1)
print(True is 1)
print(True != 1)