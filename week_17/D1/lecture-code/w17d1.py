

def get_average(num1, num2):
  """This function will accept 
  two parameters and return their average"""
  average = (num1 + num2) / 2
  return average



# help(get_average)
# result = get_average(5, 10)
# print(result)



# STRINGS

# lunch = 'pizza'
# print(lunch)
# print('pizza')
# print("pizza")
# print("let's")
# print('let\'s')
# print(''' Also another
# multi line string
# !
# ''')

my_string = """This is a multi
line string preserving spaces and new lines
like
this
and
this"""
# print(my_string)
# print(len(my_string))

a = 1
b = 2
# print(a)
# a = "pizza"
# print(a)

LUNCH = "pizza"

# print(f"Let's add {a} and {b} together to get {a + b}")
# print("Let's add {1} and {0} together to get {2}".format(a, b, a+b))
# print("Lets add {thing1} and {thing2} together to get {thing3}".format(thing3=a+b, thing2=b, thing1=a, thing4="thing"))

# print("Pizza" + " is " + "delicious")
# print("Pizza " * 3)

# # STRING INDEXING
sentence = "Brad is very much obsessed with pizza today!"

# print(sentence[0])
# print(sentence[-4])
# # print(sentence[start:stop:step])
# print(sentence[1::2])
# print(sentence[::-1])
# print(sentence.split("ss"))
# print(list(sentence))

# names = ["Brad", "David", "Andrew"]
# join_str = ", "
# print(join_str.join(names))

# BOOLEANS

# a = True
# b = False

# && || !
# and or not

# print(True and False)
# print(False and _)
# print(True or False)
# print(not True)
# print(1 != 2)

# print(int("3") == 3)

# print(True == 1)
# print(False == 0)
# print(True is 1)
# print(False is 0)

# NUMBERS
# results = 2 * 4
# print(results)
# another_val = 2 * 4.0
# print(another_val)
# # + - * / % ** //

# print(4/2)
# print(4.0**2)
# print(7/2)
# print(7//2)

# def long_division(dividend, divisor):
#     """Take in 2 values and return their quotient and remainder"""
#     quotient = dividend // divisor
#     remainder = dividend % divisor
#     print(quotient, remainder)
#     return f"{dividend} divided by {divisor} is {quotient}, remainder {remainder}"


# print(long_division(200, 23))


# VARIABLES
# a = 40
# count_of_snickers_bars = 40
# count_of_snickers_bars -= 4
# print(count_of_snickers_bars)

# a = "taco"
# a = True
# a = 35

# bags_of_candy = boxes_of_candy = 50
# print("bags", bags_of_candy)
# print("boxes", boxes_of_candy)

# DESSERT = "ice cream"
# DESSERT = "pie"
# print(DESSERT)


# IDENTITY vs EQUALITY
#     is        ==

# my_int = 4
# my_float = 4.0

# print(my_float == my_int)
# print(my_float is my_int)

# print("2" == '2')
# print("2" is '2')

# print(True == 1)
# print(True is 1)

# a = None
# print(id(a))
# b = "pizza"
# print(id(b))
# c = None
# print(id(c))
# d = 'pizza'
# print(id(d))
e = True
# print(id(e))
f = 1
# print(id(f))
g= True
# print(id(g))
print(e is g)
print(e == f)
print(e is f)
