# FUNCTIONS

def get_average(num_1, num_2):
    """ This fucntion will accept 2 
    numbers and print 
    their average    
    """
    average = (num_1 + num_2) / 2
    print("Inside function", average)
    return average


# ran_average = get_average(4, 2)
# print("Outside", ran_average)
# help(get_average)

long_string = '''This is some
long long
multiline text '''
# print(long_string)


a = 4
n = 236
x = "Pizza"

# STRINGS

lunch = "Pizza"
# print(lunch)
# lunch = 1
# print(lunch)
# LUNCH = 2
# print(LUNCH)
# LUNCH = "Sandwich"
# print(LUNCH)

# print(lunch)
# print(len(lunch))


# print("Pizza")
# print('Pizza')
# print("Let's")
# print('Let\'s')
# print(""" THis is a 
# multi
# multi
# multi
# very 
# long string
# """)

a = 1
b = 5

# print(f'Let\'s add {a} and {b} together to get {a + b}')
# print("Let's add {} and {} together to get {}".format(a, b, a + b))
# print("Let's add {thing1} and {thing2} together to get {thing3}".format(thing3=a + b, thing2=b, thing1=a))

# print("Pizza " + "is " + "delicious!" )
# print("Pizza " * 4)

sentence = "Brad is very much obsessed with pizza today!"

# print(sentence[::-1])
# sentence[start:stop:step] # stop is not inclusive
# print(sentence.split())
# print(list(sentence))

# names = ['Brad', 'John', 'David', 'Cesar']
# join_str = ' and '
# print(join_str.join(names))


# BOOLEANS

a = True
b = False

# && || !
# and or not 

# print(True and False)
# print(True or False)
# print(not True)
# print(True + 1)
# print(False + 1)
# print(1 == 1)
# print(1 == 2)
# print(1 != 1)
# print(2 != 1)
# print(int("1") == 1)


# NUMBERS

results = 2 * 4.0
# print(results)
# print(int("1234"))
# print(float("1234.56"))
# print(float(123))


# + - * / % // **
# print(2**4)

def long_division(num_1, num_2):
    result = num_1 // num_2
    remainder = num_1 % num_2
    print(result, remainder)
    return f"{num_1} divided by {num_2} is {result} remainder {remainder}"


# print(long_division(25, 3))

num = 20
num += 1

my_float = 123.45678
# print(round(my_float, 4))


dinner = ['Salad', 'Pizza', 'wings']
dinner = "salad"

num = 30
num += 5

bags = 50
cases = 50

# print(bags)
# print(cases)

DESSERT = 'ice cream'

num = 1

def new_func():
    num = 1
    if true:
        num = 2
    for food in dinner:
        num = 3



# IDENTITY vs EQUALITY
#    is         ==

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
# print(a is b)
# c = None
# print(id(c))
# print(a is c)
# d = 'pizza'
# print(id(d))
# print(d is b)

# print( True == 1)
# print( True is 1)