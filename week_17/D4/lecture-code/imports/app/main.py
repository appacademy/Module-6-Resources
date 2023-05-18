# import random as r
# from random import randint, choice
# import sys
import module1

# from package2 import module1 as mod1
from package2.module1 import say_hello

# from package1.subpackage1.module1 import say_hello as sh
from package1.subpackage1 import say_hello as sh

print(sh())

print(say_hello())

print(module1.say_hello())


# print(sys.path)
#
# print(r.__file__)


# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(randint(0, 10))
# print(randint(0, 10))
# print(randint(0, 10))
# print(randint(0, 10))
# print()
# print(choice(ls))
# print(choice(ls))
# print(choice(ls))
# print(choice(ls))
