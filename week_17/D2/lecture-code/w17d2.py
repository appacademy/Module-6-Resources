# print(4.0 == 4)
# print("string" == "string")
# print("4" == 4)

# print(6 ^ 10)
# print(False ^ False)
# print(True ^ False)
# print(False ^ True)
# print(True ^ True)

# zero = bool(0)

# print(zero)

# if 1:
    # print("the number 1 is truthy")


# console.log(true && false)

# print(True and False)

# print(not True)


# if isinstance(True, bool):
#     print("booleans are bool!?!?!?!")
# else:
#     print("booleans are not bools")

x = 25

# if x < 10:
#     print("x is less than ten")
# elif x < 20:
#     print("x is less than twenty")
# else:
#     print("x is big")
#     if x == 25:
#         print("x is twenty five")

my_long_string = """
           you can make
longer strings                    over multiple lines
individual quote characters ' " won't end the string
"""

# x = 'i'm happy'

# print(my_long_string)

my_f_str = f"{x} is a pretty cool number!!!"

# print(my_f_str)


fav_num = "{fav_num} is my favorite number".format(fav_num=x)
# print(fav_num)

b = "b"
a = "a"
an = "an"

# print(b + an * 9 + a)

# print(a * an)

# print("gorilla"[0])
# print("gorilla"[-7])
# print("gorilla"[-8]) # IndexError: string index out of range

# print("longer string"[11:5:9]) # empty string

# print("longest string ever"[-5:3:-2])


str_idx = "portable container".index("p")
str_idx = "portable container".index("cont")
# str_idx = "portable container".index("z")
# print(str_idx)

# print("asdfhosgadshfgdsfasasdasdfasdfads".count("a"))


# print("e".join("the cat is outside eating chipmunks".split("e")))

period = "."

ls = ["1","2","3","4","5","6"]

# print(period.join(ls))


# print("david nash".title())
# print("david nash".upper())

# print(dir(""))

# print(11//4)

a = 1
b = 5

# print(a)
a += b

def is_palindrome(word):
  return word[::-1] == word

# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False

# print(a)

hello = "hello"

reversed_hello = reversed(hello)

backword = "".join(reversed_hello)
# print(backword)

1,1,2,3,5,8,13

def recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)


# print(recursive_fib(-5))

def find_digit_amount(num):
    num_str = str(num)
    if num >= 0:
        return len(num_str)
    else:
        return len(num_str) - 1



# print(find_digit_amount(-19033))
# print(find_digit_amount(0))
# print(find_digit_amount(1999))


# print(0.0 == 0)

# print("hello" == "hello")

# print(True == True)

# print([1,2,3,4] == [1,2,3,4])
# print(type(0))
# print(type(0.0))

# print({"key": "value"} == {"key": "value"})

# print([1,2,3] ^ [1,5,4,3])

# print([1,2,3] > 4)

# print([1,2,3] > [4,5,6])


# print(5 is 5)

a = 5
b = 5
c = 7

# print(a == b)

# print(id(a))
# print(id(b))
# print(id(c))

my_str = "Hello To the people in the zoom room!!!!!!!!!!!!"
another_str = "Hello To the people in the zoom room!!!!!!!!!!!!"

# print(id(my_str))
# print(id(another_str))

# print(my_str is another_str)

ls1 = [1,2,3,4]
ls2 = [1,2,3,4]

# print(ls1 is ls2)

# print(id(ls1), id(ls2))


# print(id(None))
# print(id(None))


ls3 = ls1


ls3.append(5)

# print(ls3)
# print(ls1)
# print(ls2)

my_list = [1,2,3,4,5]

i = 0
while True:
    # print(my_list[i])
    if i < len(my_list) - 1:
        i += 1
        continue
    break

# my_dict = {1: 5, "hello": 0}

# for ele in my_list:
#     print(ele)


# for ele in my_dict:
#     print(ele)
    
# for idx, el in enumerate(my_list):
#     print(idx, el)

hello = "hello"

# for x in hello:
#     print(x)

# print( 6 in my_list)

# print("l" in hello)


# try:
#     print(5/0)
#     print("no exception")
# except Exception as e:
#     print("oh no!!!!")
# else:
#     print("no exception")
# finally:
#     print("i run no matte what")




# print("i'm still running")

# while True:
#     try:
#         num = input("Please enter a number! ")
#         print(f"Five divided by {num} is {5/int(num)}")
#     except ZeroDivisionError:
#         print("you can't divide by zero!!!!")
#     else:
#         print(f" {num} is a good number")


def is_valid_hex_code(the_hex):
    valid_chars = "abcdef1234567890"
    if len(the_hex) != 7 or the_hex[0] != "#":
        return False
    for char in the_hex[1:]:
        if char.lower() not in valid_chars:
            return False
    return True

# print(is_valid_hex_code("#CD5C5C")) #> True
# print(is_valid_hex_code("#EAECEE")) #> True
# print(is_valid_hex_code("#eaecee")) #> True
#
# print(is_valid_hex_code("#CD5C58C"))
# # Prints False
# # Length exceeds 6
#
# print(is_valid_hex_code("#CD5C5Z"))
# # Prints False
# # Not all alphabetic characters in A-F
#
# print(is_valid_hex_code("#CD5C&C"))
# # Prints false
# # Contains unacceptable character
#
# print(is_valid_hex_code("CD5C5C"))
    
filter_list = [1,2,3,4,5,6,7,8,9,10]

def get_evens(el):
    return el % 2 == 0

# print(list(filter(get_evens, filter_list)))
# print(list(filter(lambda x: x % 2 == 0, filter_list)))

hello = lambda: "hello"

def hello():
    return "hello"

# print(hello())

def make_a_five():
    y = 5
    return y

if True:
    y = 0

# print(y)

x = 100

def return_x(x):
    """returns the value being passed in"""
    return x

# print(return_x(90))

# print(help(return_x))

def string_multi_print(word):
    return lambda x: print(x * word)



# say_hello = string_multi_print('hello ')  # Prints "hello hello "
# string_multi_print('wahoo ')(3)  # Prints "wahoo wahoo wahoo "

# say_hello(50)


simple_list = [1,2,3,4,5,6,7,8,9,10]

# print(simple_list[3:8:2])

# print(len(simple_list))
# print(simple_list.append(11))

print(simple_list)

# simple_list.append([11,12,13,14,15])
simple_list.extend([11,12,13,14,15])

# simple_list.remove(19)

print(simple_list)

simple_list.sort(reverse=True)

print(simple_list)

print(sum(simple_list))
print(min(simple_list))
print(max(simple_list))
