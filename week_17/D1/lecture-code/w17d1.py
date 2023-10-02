def get_average(num_1, num_2):
    """this function will take in 2 number and return their average"""
    # This is a comment
    average = (num_1 + num_2) / 2
    print(average)
    return average


# ran_average = get_average(8, 10)
# print(ran_average)

# help(get_average)

# STRING
# lunch = "pizza"
# print(lunch)
# print("pizza")
# print('pizza')
# print("Let's ")
# print('Let\'s')
# print(""" This is a multi
# line string where spaces and 
# new lines get 
# preserved
# """)


a = 1
b = 2
# print(a)
# a = "wings"
# print(a)

# LUNCH = "pizza"

# LUNCH = 3

# print(LUNCH)

# print(f"Let's add {a} and {b} together to get {a+b}!")
# print(f"{'{'}")
# print("Let's add {} and {} together to get {}".format(a, b, a+b))
# print("Let's add {1} and {0} together to get {2}".format(a, b, a+b))
# print("Let's add {thing_1} and {thing_3} together to get {thing_2}".format(thing_1=a, thing_2=a+b, thing_3=b))


# print("Pizza" + " Pizza")
# print("Pizza " * 3)

# sentence = "Brad is very much obsessed with pizza today"

# print(sentence[2])
# print(sentence[-1])
# # print(sentence[start:stop:step])
# print(sentence[4::2])
# print(sentence[::-1])
# print(sentence.split("a"))
# print(list(sentence))
# names = ["Brad", "David", "Andrew"]
# join_str = ", "
# print(join_str.join(names) )


# BOOLEANS
# a = True
# b = False

# && || !
# and or not
# # print(True and False)
# # print(True or False)
# # print(not True)
# # print(False and False)
# print(1 == 2)
# print(1 != 2)

# print(int("4") == 4)
# print(True + 1)
# print(False + 1)
# print(1 == True)
# print(0 == False)
# print(1 is True)
# print(0 is False)


# NUMBERS
# result = 2. * 4
# print(result)
# result_2 = 2 / 4
# print(result_2)
# result_3 = 9 // 2
# print(result_3)
# print(int(3.5))
# print(float(6))
# print(int("7"))
# # print(int("a"))
# print(str(3.4))

# # + - * / % // **

# print(4**2)

# def long_divison(dividend, divisor):
#     """takes in 2 integers and returns thier quotient and remainder"""
#     quotient = dividend // divisor
#     remainder = dividend % divisor
#     print(quotient, remainder)
#     return f'{dividend} divided by {divisor} is {quotient} remainder {remainder}'


# print(long_divison(23, 3))


# brads_age = 45
# brads_age += 1

# BRADS_AGE = 45 

# bags = cases = boxes = cartons = storage_devices = 50
# print(bags, cases, boxes, cases, cartons, storage_devices)


# IDENTITY vs EQUALITY
#     is        ==

# my_int = 4
# my_float = 4.0

# print(my_int == my_float)
# print(my_int is my_float)

# print("2" == '2')
# print("2" is "2")

a = None
print(id(a))
b = "pizza"
print(id(b))
c = None
print(id(c))
d = True
print(id(d))
e = 1
print(id(e))
print(a is c)
print(d == e)