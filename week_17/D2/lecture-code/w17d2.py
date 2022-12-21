# XOR

# print( True ^ False)
# print( True ^ True )
# print( False ^ True )
# print( False ^ False)

# IF STATEMENTS

def present(item):
    if item == 'PS5':
        print(f'A {item} is an awesome holiday present!')
    elif item == 'Xbox':
        print(f'Microsoft is awesome! A {item} is a great gift!')
    else:
        print(f'{item} is a great gift too!')

# present('PS5')
# present('Xbox')
# present('Socks')

# XOR PROBLEM
def xor(val1, val2):
    return val1 ^ val2


# print(xor(False, False))   #>  False
# print(xor(True, False))   #>  True
# print(xor(True, True)) #>  False
# print(xor(5, 3))  #> 6
# # print(xor(8, 4))  #> 12
# # print(xor(2, 2))  #> 0
# # print(xor(1, 2))  #> 3
# # print(xor(4, 4))  #> 0
# print(bin(True))
# print(bin(False))
# # 0b1
# # 0b0
# print(bin(5))
# print(bin(3))
# 0b101
# 0b011
#   110
# print(bin(6))


# Write your function, here.
def not_or(bool1, bool2):
    return not bool1 or bool2


# print(not_or(True, False))    #> False
# print(not_or(True, True))     #> True
# print(not_or(False, True))    #> True
# print(not_or(False, False))   #> True


# STRINGS

a = 'a'
b = 'b'
an = 'an'

# print(b + an)
# print(b + a * 7)
# print(b + an * 2 + a)

christmas_dinner = "Turkuuuey"

# print(christmas_dinner[1:3:1])
# print(christmas_dinner[::-5])

# # print(christmas_dinner.index('q'))
# print(christmas_dinner.count('q'))
# print(list(christmas_dinner))

# reindeer = ["Comet", "Donner", "Blitzen"]
# print(', '.join(reindeer))

# Write your function, here.
def recursive_string(string):
    if len(string) == 0:
        return string
    
    return recursive_string(string[1:]) + string[0]

# string      s
# tring       t
# ring        r
# ing         i
# ng           n
# g             g
# gnirts



# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) # noitacilppa

# NUMBERS

# a = 6
# print(a)
# a += 1
# print(a)
# a *= 2
# print(a)


my_int = 4
my_float = 4.0

# print(my_int == my_float)
# print(my_int is my_float)

# print(id(my_int))
# print(id(my_float))

# print( 1 == True)
# print( 1 is True)

string1 = 'word'
string2 = 'word'
# print(id(string1))
# # print(string1.upper())
# print(id(string2))
# string1 += 's'
# print(id(string1))
# print(id(string2))

# print(string1 == string2)
# print(string1 is string2)
# print(id(string1))
# print(id(string2))

# variable = None
# var2 = None

str1 = '1'
str2 = str(1)
# print(id(str1))
# print(id(str2))
# print(str1)
# print(str2)

# STATEMENTS

# WHILE

# days = 5

# while days > 0:
#     if days == 1:
#         print("Tomorrow is Christmas!")
#     else:
#         print(f'{days} days till Christmas!')
    
#     days -= 1


# days = 5

# while True:
#     if days > 1:
#         print(f'{days} days till Christmas!')
#         days -= 1
#         continue

#     print("Tomorrow is Christmas!")
#     break
#     print("You will never see this")


# reindeer = ["Comet", "Cupid", "Donner", "Blitzen", "Rudolf"]

# for deer in reindeer:
#     print(f"{deer} is a cool reindeer!")

# print("Comet" in reindeer)
# print("Greg" in reindeer)

# print(list(range(0,5)))

# for i in range(len(reindeer)):
#     print(f"{i + 1}. {reindeer[i]}")


# TRY/EXCEPT
num = "cookies"
# print(4/0)

# try:
#     print("in the try block")
#     print(4/num)

# except ZeroDivisionError:
#     print("we can not divide by zero!")

# except TypeError:
#     print("we can not do division with strings!")

# else: 
#     print("this will only print if the try block is successful")

# finally:
#     print('we will see this no matter what!')


# SEQUENCE OF NUMBERS
# Write your function, here.
def seq_of_numbers(seq):
    seq += " "
    count = 1
    # i = 0
    results = ''
    
    # while i < len(seq) - 1:
    for i in range(len(seq) - 1):
        if seq[i] != seq[i + 1]:
            results = results + str(count) + seq[i] + ","
            count = 1
        else:
            count += 1

        # i += 1

    return results


# print(seq_of_numbers("1211 "))
# # # This is "one 1, one 2, two 1s"
# # # Prints "11,12,21"

# print(seq_of_numbers("111221"))
# # # This is "three 1s, two 2s, and one 1"
# # # Prints "31,22,11"

# print(seq_of_numbers("31131211131221"))
# # This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
# #    one 3, one 1, two 2s, and one 1"
# # Prints "13,21,13,11,12,31,13,11,22,11"

# FUNCTIONS
def is_even(num):
    """
    takes in a number and returns a boolean 
    if the number is even
    """
    return num % 2 == 0

is_even = lambda num: num % 2 == 0

# print(is_even(5))
# print(is_even(4))

# multiply = lambda num1, num2: num1 * num2
# print(multiply(2, 10))


y = 10

PI = 3.14

# def make_a_five(PI):
#     # y = 5
#     # global PI
#     # PI = 3.14
#     print("inside function", PI)
#     PI += 5
#     # if True:
#     #     y = 15

#     # print("in function after if block", y)

# make_a_five(PI)

# print("global scope", PI)




# LISTS

reindeer = ["Comet", "Cupid", "Donner", "Blitzen", "Rudolf"]

# print(reindeer[1::2])
# print(reindeer[::-1])
# print(len(reindeer))
# reindeer.append("Vixen")
# print(reindeer)
# reindeer.extend(["Dasher", "Dancer"])
# print(reindeer)
# reindeer.insert(1, "Prancer")
# print(reindeer)
# reindeer.remove("Dancer")
# print(reindeer)

vals = [2, 4, 56, 12, 4]
vals.sort()
print(vals)
print(sum(vals))
print(min(vals))
print(max(vals))
