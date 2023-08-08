# def get_average(num_1, num_2):
#     """Will take in 2 numbers and return their average"""
#     average =(num_1 + num_2) / 2
#     # print(average)
#     return average


# ran_average = get_average(4, 6)
# print(ran_average)


# String Stuff

# lunch = "Pizza"
# print(lunch)
# print("Pizza")
# print(len(lunch))

# print('Pizza')
# print("Pizza")
# print('Let\'s')
# print(""" This is a multi
# line string where spaces
# and new lines get preserved
# and stuff""")


# a = 1
# b = 2

# print(f"Let's add {a} and {b} together to get {a + b}")
# print("Let's add {} and {} together to get {}".format(a, b, a + b))
# print("Let's add {1} and {0} together to get {2}".format(a, b, a + b))
# print("Let's add {thing_1} and {thing_2} together to get {thing_3}".format(thing_3=a+b, thing_1=a, thing_2=b))

# print("Pizza" + " is " + "very yummy")
# print("Pizza" + " is " + "so " * 3 + "very yummy")

# sentence = "Brad is very much obsessed with pizza today!"

# # print(sentence[2])
# # print(sentence[-2])
# # # print(sentence[start:stop:step])
# # print(sentence[:6])
# # print(sentence[::-1])
# print(sentence.split("a"))
# print(len(sentence))
# print(list(sentence))

# names = ["brad", "david", "andrew"]
# join_str= ", "
# print(join_str.join(names))



# BOOLEANS

# a = True
# b = False

# && || !
# and or not
# print(True and False)
# print(True or False)
# print(False and False)
# print(not True)
# print(True + 1)
# print(False + 1)
# print(True == 1)
# print("4" == 4)

# NUMBERS

# result = 4 * 3
# print(result)
# value = 12345.000
# big_num = 1_000_000_000_000
# other_num =1000000000000
# print(big_num)
# print(int(value))
# integer = 45
# print(float(integer))
# val_2 = "12345"
# print(float(val_2))

# # + - * / % ** //

# print(4**2)

# def long_division(dividend, divisor):
#     """ Take in 2 numbers and return their result and remainder"""
#     quotent = dividend // divisor
#     remainder = dividend % divisor
#     print(quotent, remainder)
#     return f"{dividend} divided by {divisor} is {quotent} reaminder {remainder}"


# print(long_division(25, 3))
# help(long_division)
# count = 40
# count += 1

# VARIABLES

# x = 30

# num_1 = 40

# average_of_sums = 500

# average_of_sums = "taco"

# print(average_of_sums)

# LUNCH = "pizza"

# WORK_DAYS = ["Mon", "Tues", "Wed", "Thurs", "Fri"]


# IDENTITY vs EQUALITY
#    is          ==

my_int = 4
my_float = 4.0

# print(my_float == my_int)
# print(my_int is my_float)

# print('2' == "2")
# print("2" is '2')

rand_var = None
print(id(rand_var))
rand_var_2 = "pizza"
print(id(rand_var_2))
rand_var_3 = None
print(id(rand_var_3))
rand_var_4 = True
print(id(rand_var_4))
rand_var_5 = 1
print(id(rand_var_5))

print(rand_var_4 == rand_var_5)
print(rand_var_4 is rand_var_5)