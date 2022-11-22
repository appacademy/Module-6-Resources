# FUNCTIONS
# this is a comment

average = 0

def get_average(num_1, num_2):
    """
    Take in 2 parameters and return their average 
    """
    average = (num_1 + num_2) / 2
    print(average) 
    if True:
        print("In a if block")
        average += 1

    return average

# got_average = get_average(6, 4)
# print(got_average)
# help(get_average)

# Variabe declarations
n = 78
n = "Turkey"
lunch = "Turkey"


# STRINGS

# lunch = "Turkey"
# print(lunch)
# print(len(lunch))

# print("Pumpkin Pie")
# print('Apple Pie')
# print('Let\\\'s')
# print(''' This is a multi
# line string
# it is so so 
# so many
# lines ''')


# LUNCH = "Turkey"
# print(LUNCH)
# LUNCH = 'Ham'
# print(LUNCH)

a = 1
b = 2
# print(a)
# a = "Gravy"
# print(a)

# print(f"Let's add {a} and {b} together to get {a + b }")

# print("Let's add {2} and {1} together to get {0}".format(1, 2, 1 + 2))

# print("Let's add {thing_1} and {thing_2} together to get {thing_3}".format(thing_3=a + b, thing_1 = a, thing_2 = b ))


# print("Mashed potatoes" + " are" + " great?")
# print("Turkey " * 4)

sentence = "Its almost thanksgiving and Brad is obsessed with turkey"
# print(sentence[-1])
# print(sentence[5:])
# print(sentence[1:13:2])
# print(sentence[::-1])
# print(sentence.split('a'))
# print(list(sentence))

# names = ["Brad", "John", "David", "Andrew"]
# join_str = ' and '
# print(join_str.join(names))


# BOOLEANS

# a = True
# b = False

# # && || !
# # and or not

# print(True and False)
# print(True or True)
# print(True or False)
# print( not True)
# print( 3 != 4)
# print( not "")
# print(True + False)

# new_dict = {
#     "lunch": "Turkey",
#     1: "Gravy"
# }

# NUMBERS - Integers and Floats
results = 2 * 4
# print(results)

# operators + - * / % // **

# print(12 / 7)
# print(12 // 7)

def long_division(num_1, num_2):
    results = num_1 // num_2
    remainder = num_1 % num_2
    print(results, remainder)
    return f"{num_1} divided by {num_2} is {results} remainder {remainder}"

# print(long_division(234, 12))

# print(12 / 6)

# print(int("1235"))
# print(float("1235"))
# print(int(234.78))

# print( 4 * 20 + 40)

# print(2**4)

# num = 14
# num += 1

# num = None

# VARIABLES

brads_age = 44
brads_age += 1

a = 44
a = "potatoes"

DAYS_OF_WEEK = ("Mon", "Tues", "Weds")

bags = cases = 50
# print(bags, cases)

# bags = 50
# cases = 50


# IDENTITY vs EQUALITY
#    is         ==

my_int = 4
my_float = 4.0
my_string = "4"

# print(my_float == my_int)
# print(my_string == my_int)
# print(my_float is my_int )

# print("2" == '2')
# print("2" is '2')

# a = None
# print(id(a))
# b = 'pizza'
# print(id(b))
# c = None
# print(id(c))
# print(a is c)
# d = 'pizza'
# print(id(d))
# print(b is d)

list_1 = [1, 2, 3]
list_2 = [1, 2, 4]
# print(list_1 == list_2)
# print(id(list_1))
# print(id(list_2))
# print(list_1 is list_2)

print(True == 1)
print(True is 1)
