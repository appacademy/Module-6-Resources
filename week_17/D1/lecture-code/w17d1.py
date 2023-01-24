# FUNCTIONS
def get_average(num_1, num_2):
    """This function will accept two numbers
    and return the average"""
    average = (num_1 + num_2) / 2
    print(average)
    return average
    print("Not gonna see this")

# ran_average = get_average(4,6)
# print(ran_average)
# help(get_average)


# STRING STUFF
# lunch = "Pizza"
dinner = 'Wings'
# print(lunch)
# print(dinner)
# print(len(lunch))
# print(""" This is a
# multi line string
# and we can do 
# lots and 
# lots of lines
# cool
# """)

a = 1
b = 2
# print(a)
# a = "Pizza"
# print(a)

LUNCH_TIME = "Pizza"

# print(f"Let's add {a} and {b} together to get {a + b} ")
# print("Let's add {1} and {0} together to get {2}".format(a, b, a+b))
# print("Let's add {thing2} and {thing1} together to get {thing3}".format(thing2=a, thing1=b, thing3=a+b))

# thing1 = "Taco"
# print(thing1)

# print("Pizza" + " is" + " so" + ' delicious')
# print("Pizza is so" + (" very," * 4) + " yummy!" )

# sentence = "Brad is very much obsessed with Pizza today!"

# print(sentence[::-1])
# print(sentence[2:10:1])
# print(sentence.split("a"))
# print(list(sentence))

# names = ["Brad", "David N.", "Andrew", "David D."]
# join_str = ', '
# print(join_str.join(names)) 


# BOOLEANS
a = True
b = False

# && || !
# and or not
# print(True and False)
# print(True or False)
# # print(not False)
# # print(True + 1)
# # print(False + 10)
# print(1 == 2)
# print(1 == True)
# print(1 == 1.0)
# print(1 != 2)


# NUMBERS
results = 2.0 * 4.0
# print(results)
# print(int('1234') + 3)
# print(str(1234))
# print(float(235))
# print(int(2367.8))


# OPERATIONS
# + - * / % // **
# print(4**2)

def long_division(num_1, num_2):
    results = num_1 // num_2
    remainder = num_1 % num_2
    print(results, remainder)
    return f"{num_1} divided by {num_2} is {results} remainder {remainder}"


# print(long_division(253_456, 3_234))


# IDENTITY                      vs          EQUALITY
# JS: === (identity/type and value)            == (value)
# PY:  is                                      ==

# my_int = 4
# my_float = 4.0

# print(my_float == my_int)
# print(my_float is my_int)

# print("2" == '2')
# print("2" is '2')

# a = None
# print('A',id(a))
# b = 'pizza'
# print('B',id(b))
# c = None
# print('C',id(c))
# d = 'pizza'
# print('D',id(d))
# print(a is c)
# print(b is d)

print(True == 1)
print(True is 1)

bags = cases = boxes = barrels = 50

print(bags, cases)

bags = "Bags"
print(bags)

num_4 = 40
num_4 += 1

DESSERT = "ice cream"

DESSERT = "pecan pie"

print(DESSERT)