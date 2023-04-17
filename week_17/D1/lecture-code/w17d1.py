# W17 D1

# FUNCTIONS
def get_average(num_1, num_2):
    """This function will take in 2 numbers 
    and return their average"""
    average = (num_1 + num_2) / 2
    # print(average)
    return  average


# ran_average = get_average(20, 40)
# print(ran_average)

# STRINGS

# lunch = "pizza"
# print(lunch)
# print(len(lunch))

# print('pizza')
# print("pizza")
# print("Let's")
# print('Let\'s')
# print(''' This is a multi
# line string so we can 
# habe so so
# so
# so
# so
# so
# many lines!
# ''')

a = 1
b = 2
# print(a)
# dinner = 'taco'
# print(a) 

# LUNCH_NOW = "taco" 
# PI = 3.14

# F STRING / FORMATTING
# print(f"Let's add {a} and {b} together and get {a + b}!")
# print("Let's add {} and {} together to get {}".format(a, b, a+b))
# print("Let's add {thing1} and {thing3} together to get {thing2}".format(thing1=a, thing2 = a + b, thing3=b))


# print("Pizza " + "is " + "Great!")
# print("pizza "*4)


sentence = "Brad is very much obsessed with pizza today!"

# print(sentence[0])
# print(sentence[-5])
# print(sentence[start:stop:step])
# print(sentence[:10])
# print(sentence[::2])
# new_sentence = sentence[::]

# print(sentence.split("a"))
# print(list(sentence))

# names = ['brad', 'david', 'andrew', 'keegan']
# # print(", ".join(names))
# join_str = ', '
# print(join_str.join(names))


# BOOLEANS
a = True
b = False

# &&  ||  !
# and or not 
# print(True and False)
# print(True or False)
# print(not True)
# print(True + 1)
# print(False + 1)
# print(False/True)
# print(1 == 2)
# print(3 != 4)


# NUMBERS
# results = 2 * 4
# print(results)
# my_int = 4
# my_float = 4.0
# print("my int", my_int, 'my_float', my_float)
# print(float(my_int))
# print(int("4567"))
# big_num = 1_000_000_000
# print(big_num)

# + - * / % ** //
# print(4**2)
# print(5 / 2)
# print(5 // 2)

def long_division(dividend, divisor):
    """Takes in 2 number and return their results and 
    any remainder"""
    quotent = dividend // divisor
    remainder = dividend % divisor
    print(quotent, remainder)
    return f'{dividend} divided by {divisor} is {quotent} reaminder {remainder}'


# print(long_division(25, 3))
# help(long_division)

# VARIABLEs

# num_1 = 5
# randint = 5
# print(randint)

# a = 1
# x = 0
# i = 6

# num_1 += 1
# print(num_1)

# num_1 = "wings"
# print(num_1)

# num_1 = []
# print(num_1)

# bags = cases = 50
# print(bags, cases)

# dinner = None
# dinner = "pizza"
# DESSERT = 'ice cream'
# DESSERT = False

# print(DESSERT)


# IDENTITY vs EQULITY
#    is    vs   ==

my_int = 4
my_float = 4.0

# print(my_float == my_int)
# print(my_float is my_int)

# print("2" == '2')
# print("2" is '2')

test_1 = None
print(id(test_1))
test_2 = None
print(id(test_2))
print(test_1 is test_2)
test_3 = 45
print(id(test_3))
test_4 = 45
print(id(test_4))
print(test_3 is test_4)

print(1 == True)

print(True is 1)