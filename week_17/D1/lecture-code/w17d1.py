# FUNCTIONS

def get_average(num1, num2):
    """This function will accept two numbers and return the average"""
    average = (num1 + num2) / 2
    # print(average)
    return f'the average of {num1} + {num2} is {average}'


# run_average = get_average(2, 4)
# print(run_average)


# STRINGS

lunch = "Pizza"
dinner = 'Streak'

# print(lunch + dinner)

# print("""We can have multiple
# lines of strings using triple quotes and 
# they can 
# be many many
# many lines""")

LUNCH = "Wings"

a = 1
b = 2

# print(f"Let's add {a} and {b} to get {a + b}")
# print("Let's add {} and {} to get {}".format(a, b, a + b))
# print("Let's add {thing1} and {thing2} to get {thing3}".format(thing3=a + b, thing1=a, thing2=b ))


sentence = "Brad is rather obsessed with eating pizza for lunch"

# print(sentence[-2])
# # varible[start:stop:step]
# print(sentence.split())

list(sentence)
[*sentence]

instructors = ["Brad", "John", "Cesar", "David"]
join_str = "".join(instructors)
# print("".join(instructors))

# print(sentence.index("d"))

# BOOLEANS
a = True
b = False

#  && || !
# and or not

# print(True and True)
# print(False and True)
# print(True or False)
# print(not True)

# print(True + False)

# print(True == 1)
# print(False == 0)

# NUMBERS
results = 2 * 4
# print(results)

# + - * / %  // **

results2 = 2**4
# print(results2)

def long_division(num1, num2):
    result = num1 // num2
    remainder = num1 % num2
    print(f"{num1} divided by {num2} equals {result} remainder {remainder}")
    return result, remainder


# long_division(25, 3)

# print(int('12345'))
# print(float("12345.60"))
# print(float(6789))
# print(int(147.80))
# print(str(123))

# count = 2
# print(count)
# count += 1
# print(count)
value = None
# print(int(value))

# print("Pizza" * 10)

# print(8 / 4)


# VARIABLES
num_1 = 40
num_1 += 1


age = 40
lunch = 'Salad'

MEALS = ["breakfast", "lunch", "dinner"]
# print(MEALS)
# MEALS = 'PASTA'
# print(MEALS)

bags = cases = 50
# print('bags', bags)
# print('cases', cases)
cases = 60
# print('bags', bags)
# print('cases', cases)
# print(bags == cases)
# print(bags is cases)


# IDENTITY vs EQUALITY
#     is   vs    ==

my_int = 4
my_float = 4.0
# print(my_float == my_int)
# print(my_float is my_int)

# print("21" == '2')
# print("21" is '2')

# a = 3
# print(id(a))
# b = "pizza"
# print(id(b))
# c = 3
# print(id(c))
# print(a is c)

list_1 = [ 1, 2, 3]
print(id(list_1))
list_2 = [ 1, 2, 3]
print(id(list_2))
list_3 = list_1
print(id(list_3))

val = True
print(id(val))
print(id(True))
print(val is True)