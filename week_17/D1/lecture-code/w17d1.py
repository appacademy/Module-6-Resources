# FUNCTIONS & OTHER STUFF...

def get_average(num1, num2):
    """This function will accept two numbers and return their average"""
    average = (num1 + num2) / 2
    print(average)
    return average


# ran_average = get_average(4, 6)
# print(ran_average)
# help(get_average)

# STRING STUFF

lunch = "Pizza"
# print(lunch)
# print(len(lunch))

# print('Pizza')
# print("Pizza")
# print("Let's")
# print(''' This is a
# multiline string
# so 
# so 
# many lines ''')

a = 1
b = 2
# print(a)
# a = "Pizza"
# print(a)

# LUNCH = "Pizza"

# print(f"Let's add {a} and {b} together to get {a + b}")

# print("Let's add {} and {} together to get {}".format(a, b, a+b))

# print("Let's add {thing1} and {thing2} together to get {thing3}".format(thing3=a+b, thing1=a, thing2=b))

# print("Pizza " + "is " + "great")
# print("Pizza" * 4)

# sentence = "Brad is very much obsessed with pizza today!"

# print(sentence[2:10:2])
# print(sentence[:-5])
# print(sentence.split())
# print(len(sentence))

# names = ["Brad", "John", "Cesar", 'David']
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
# print(True + True)
# # print("pizza" + 1)
# print(False/True)
# print(2**False)

# NUMBERS
result = 2 * 4
# print(result)
# print(int('1234'))
# print(float("123435.56"))
# print(float(123))

# + - * / %  // **
# print(4**2)

def long_division(num1, num2):
    results = num1 // num2
    remainder = num1 % num2
    print(result, remainder)
    return f"{num1} divided by {num2} is {result} remainder {remainder}"


# print(long_division(25, 3))

# VARIABLES
num1 = 40
num1 += 1

a = 40
b = 35
lunch = "pizza"
# print(num1)
# print(num1)
# num1 = "donuts"
# print(num1)

bags = cases = 50
# print('bags', bags)
# print('cases', cases)

dinner = None

DESSERT = "ice cream"




# IDENTITY vs EQUALITY
#    is    vs    ==

my_int = 4
my_float = 4.0

# print(my_int == my_float)
# print(my_int is my_float)

# print("2" == '2')
# print("2" is '2')

# a = None
# print(id(a))
# b = "pizza"
# print(id(b))
# c = None
# print(id(c))
# print(a is c)
# d = "pizza"
# print(id(d))
# print(b is d)

list1 = [ 1, 2, 3 ]
print(id(list1))
list2 = [ 1, 2, 3 ]
print(id(list2))
print(list1 == list2)
print(list1 is list2)