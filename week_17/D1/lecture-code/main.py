# FUNCTIONS

def get_average(num1, num2, num3):
    """
    Takes in three arguments and returns
    the arithmetic mean of the numbers
    """
    print("i'm finding the average")
    avg = (num1 + num2 + num3) / 3
    return avg

print(help(get_average))


avg = get_average(1,2,3)
# print(avg)


# STRINGS

def compare(str1, str2):
  len1 = len(str1)
  len2 = len(str2)
  return len1 == len2

# print(compare("AB", "CD"))              #> True
# print(compare("ABC", "DE"))             #> False
# print(compare("hello", "App Academy"))  #> False


def format_name(f_name, l_name):
  # return f"Hi, my name is {f_name} {l_name}"
  # return "Hi, my name is {0} {1}".format(f_name, l_name)
  return "Hi, my name is {first} {last}".format(last=l_name, first=f_name)

# print("int: {0:d}, hex: {0:x}, bin: {0:b}".format(95))

# print(format_name("Alex", "Ambrose"))  #> Hi, my name is Alex Ambrose
# print(format_name("Amy", "Mayer"))     #> Hi, my name is Amy Mayer
# print(format_name("Rick", "Morty"))    #> Hi, my name is Rick Morty


# BOOLEANS

def And(bool1, bool2):
  return bool1 and bool2

print(And(True, False))    #> False
print(And(True, True))     #> True
print(And(False, True))    #> False
print(And(False, False))   #> False


# NUMBERS

def string_int(num_word):
  return int(num_word)


print(string_int("6"))     #> 6
print(string_int("1000"))  #> 1000
print(string_int("12"))    #> 12

print(type(string_int("111")))

print(isinstance(9, int))



