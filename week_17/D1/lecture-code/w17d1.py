# FUNCTIONS

import random

def naughty_or_nice(person):
    """
    Takes in a person and tells us if they 
    have been naughty or nice
    """
    behavior = ['nauhgty', 'nice']
    return f"{person} is on the {random.choice(behavior)} list!"


# result = naughty_or_nice('Brad')
# print(result)

# help(naughty_or_nice)


# STRINGS
# snack = "Christmas Cookies"
# print(snack)
# print(len(snack))

# print("Candy cane")
# print('Candy cane')
# print("Let's eat candy canes")
# print('Let\'s eat candy canes')
# print("""Happy Holidays
# to everyone and 
# also a
# very very
# very very
# Happy New Year
# """)

a = "glass balls"
b = "lights"
# print(a)
# a = "Christmas cookies"
# print(a)

# SNACK = "Peppermint Bark"
# print(SNACK)
# SNACK = "Eggnog"
# print(SNACK)

# print(f"Let's decorate the tree with {a.upper()} and {'lots of ' + b}!")
# print("Let's decorate the tree with {0} and {1}!".format(a.upper(), b))
# print("Let's decorate the tree with {thing1} and {thing2}!".format(thing2=a.upper(), thing1=b))

# print("Hot Cocoa" + " is" + " delicious!")
# print(" Hot Cocoa " * 3)

sentence = 'Brad is a cotton headed ninny muffin!'

# print(sentence[-3])
# print(sentence[:6])
# print(sentence[:8:2])
# print(sentence[::-1])
# print(sentence.split("a"))
# print(sentence.lower().index("a"))
# print(list(sentence))

names = ["Buddy", "Santa", "Walter Hobbes", "Jovy"]
join_str = ', '
# print(join_str.join(names))

# Write your function, here.
def concat_name(first_name, last_name):
    # return last_name + ', ' + first_name
    return f'{last_name}, {first_name}'


# print(concat_name("First", "Last"))  #> "Last, First"
# print(concat_name("John", "Doe"))    #> "Doe, John"
# print(concat_name("Mary", "Jane"))   #> "Jane, Mary"


# # BOOLEANS

# a = True
# b = False

# # && || !
# # and or not

# print(True and False and True)
# print((True or False) and False)
# print(not True)
# print(True + 1)
# print(False + 1)
# print(False//True)

# # print(len(list1) == 0 )

# if value in [4, 5, 6]:
#     print("do something")


# NUMBERS
result = 4 * 5
# print(result)
# print(12345)
# print(1_000_000_00)
# print(int('1234') + 5)
# print(float('1234.23') + 5.12)
# print(int(1235.35))

# OPERATIONS
# + - * / % // **
# print(4**2)

# def long_division(num1, num2):
#     results = num1 // num2
#     reaminder = num1 % num2
#     print(result, reaminder)
#     return f"{num1} divided by {num2} is {result} reaminder {reaminder}"

# print(long_division(25, 3))

# VARIABLES

num1 = 40
val = 50
lunch = "pizza"

bags = cases = 50
# print(bags)
# print(cases)

num1 = "Christmas Elves"

TREE = "Douglas Fir"

val2 = 5
val2 += 1


# OPERATORS

# IDENTITY vs EQUALITY
#    is    vs  ==

my_int = 4
my_float = 4.0

# print(my_float == my_int)
# print(my_float is my_int)

# print("2" == '2')
# print("2" is '2')

# a = None
# print(id(a))
# b = None
# print(id(b))
# print(a is b)

# print( True == 1)
# print( True is 1)

list1 = [1, 2, 3]
list2 = [2, 2, 3]
print(id(list1))
print(id(list2))

print(list1 == list2)
print(list1 is list2)