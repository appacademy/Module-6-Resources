# if 0:
#     print("0 is truthy")

a = "hello"
b = 5

# if b == 6 or a == "hello":
#     print("one of our conditions have been met")

# False and print("hello")

# if a == "bye":
#     print("bye yourslef")
# elif b == 5:
#     print("five is good")
# else:
#     print("nothing is true")


long_quote = """
This is the first line
this is the second line
this is ...
"""

# print(long_quote)


# interp = f"I've said {'spork' if True else 'candle'} {b} times today!"

# print(interp)

b = "b"
an = "an"
a = "a"

# print(b + (9 * an) + a)

sentence = "There are a lot of e's in this sentence, aren't there?"
sentence1 = "There are a lot of e's in this sentence, aren't there?"
# print(sentence is sentence1)
# print(sentence)
# print("".join(["^" if char == "e" else " " for char in sentence]))
# print(sentence[0::6])
# print(len(sentence))


# print(sentence.index("'"))
# print(sentence.count("e"))

# print(sentence.lower())
# print(sentence.upper())
# print(sentence.title())
#
# print("00000000000".join(sentence.split(" ")))

# print(help(str))
# if "x" in sentence:
#     print(sentence.index("x"))

# print(sentence.find("x"))

# print(help(str))

# a, b, c = 0, 0.0, 0j
a = 0
b = 0.0
c = 0j
# print("type a:\t", type(a), "\ntype b:\t", type(b), "\ntype c:\t", type(c))

# print(f"19 divided by 2 is {19//2} with {19%2} remaining")


num = 15

num **= 2

# print(num)

word1 = "Keegan"
word2 = "Keegan"

num1 = 5
num2 = 5

ls1 = [1, 2, 3]
ls2 = [1, 2, 3]

# print(word1 == word2)
# print(word1 is word2)
#
# print(ls1 == ls2)
# print(ls1 is ls2)


# print("word1 id:", id(word1))
# print("word2 id:", id(word2))
# print()
# print("num1 id:", id(num1))
# print("num2 id:", id(num2))
# print()
# print("ls1 id:", id(ls1))
# print("ls2 id:", id(ls2))


a = 5
check = a > 0

# if check is True:
#     print(f"{a} is greater than five")


x = "0"

y = 0

# print(x == y)

# console.log('0' == 0);

# print("abasklasdfas" < "bfdsafadsfafdsa")

# print(id(None))


# def none_func():
#     pass


# print(id(none_func()))

start = 1
end = 10
count = start

# while count < end:
#     if count % 3 == 0:
#         count += 1
#         break
#     print(count)
#     count += 1
#
# print("done with that!")

word = "hello"

# if "h" in word:
#     print("the letter h is indeed in the word hello")

# for i in range(len(word)):
#     print(i)
#     print(word[i])


# try:
#     print(9 // 1)
# except ZeroDivisionError as e:
#     # print("I don't know what nine divided by 0 is")
#     print(e)
# finally:
#     print("and we're done")


i = 0

# try:
#     while True:
#         print(word[i])
#         i += 1
# except IndexError as e:
#     pass


import re


def valid_zip_code(zip_code):
    valid = re.match("[0-9]{5}(-\d{4})?$", zip_code)
    return zip_code if valid else "The zip code you entered is invalid"


zip1 = "47243"
zip2 = "23128-"
zip3 = "01237-1238"
zip4 = "91374-31"
zip5 = "1321-9883"
zip6 = "6320"

# print(valid_zip_code(zip1))  # '47243'
# print(valid_zip_code(zip2))  # "The zip code you entered is invalid"
# print(valid_zip_code(zip3))  # '01237-1238'
# print(valid_zip_code(zip4))  # "The zip code you entered is invalid"
# print(valid_zip_code(zip5))  # "The zip code you entered is invalid"
# print(valid_zip_code(zip6))  # "The zip code you entered is invalid"


# def is_even(num):
#     return num % 2 == 0


# is_even = lambda x: x % 2 == 0

# print(is_even(22))


# print(list(filter(lambda x: x % 2 == 0, ls)))

a = 0


def print_a():
    """
    Defines and the prints a variable in order to
    demonstrate python function scoping
    """
    # print(a)  # UnboundLocalError!
    while True:
        a = 1
        break
    print(a)


# print_a()
# print(print_a.__doc__)

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(ls[9:3:-2])

# print(len(ls))
print(ls.extend([10, 11, 12, 13, 14, 15]))
print(ls)

ls.remove(5)

print(ls)


ls.sort()
# help(ls.sort)
print(ls)
print(max(ls))
print(len(ls))
