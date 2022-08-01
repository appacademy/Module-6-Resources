# DEFINING FUNCTIONS
def divide_numbers(num1, num2):
    average = (num1/num2)
    return average

# print(divide_numbers(6, 2))

def get_average(num1, num2):
    return (num1 + num2)/2

# print(get_average(6, 2))


# # STRINGS
# print("Pizza")
# print('Sandwich')
# print('It\'s my pizza!')
# def my_print():
#     print('''We can write a string
# that goes over many
# many 
# many
# lines''')
# my_print()

lunch = "Salad"

# print(f"My lunch is going to be a {lunch}")

a = 1
b = 4
# print(f"The total is ${a + b}")
# print("Lets add {} and {} together".format(a,b))

a = "pizza"
# print(a * 3)

sentence = "Brad really seems to want a pizza today"
# print(sentence[5:11])
# print(sentence[:-5])
# print(sentence.split())

names = ["Brad", "Blue", "John"]
joiner = ' and '
# print(joiner.join(names))

# print(len(123))



# BOOLEANS
# print(True + 1)
# print(0 == 0)
# print(not True and True)
# print(False and True)
# print(True and not False)

# NUMBERS
# result = 2 * 5
# print(result)
# result2 = int('123')
# print(result2)
# result3 = float("123.45")
# print(result3)

def long_division (num1, num2):
    result = num1 // num2
    remainder =  num1 % num2
    print(result, remainder)
    return f"{result} remainder {remainder}"

# print(long_division(25, 3))

a = 3
a += 1

a = 20
# print(a)
# a = "Pizza"
# print(a)
# bags = cases = 40
# print(bags)
# print(cases)
# b = 50
# print(b)
# print(c)

# IDENTITY VS EQUALITY
# is vs ==

my_int = 4
my_float = 4.0
 
# check if the values are the same
# print(my_int == my_float)  # True
 
# # check if the values are the same and check type
print(my_int == my_float)
print(my_int is my_float)

# print (2 == 2.0)    # => True
# print (2 is 2.0)    # => False
# print ("2" == '2')    # => True
# print ("2" is '2')    # => True


a = None
print(id(a))
b = "Pizza"
print(id(b))

list1 = [1, 2, 3]
print(id(list1))
list2 = list1
print(id(list2))
print( list1 is list2) 
print( list1 == list2) 
# False
