# import random
# from random import randint, choice
from random import randint as r
# from package.sub import hello as sub_hello
from package import hello as sub_hello
from package.sub_package.sub_sub1 import hello as subsubsub_hello
from mod import hello
import sys


# print(dir(random))


# print(random.randint(1, 10))

# print(randint(1,10))


# ls = [1,2,3,4,5]

# print(choice(ls))

# print(r(1,10))


hello()
sub_hello()
subsubsub_hello()

# print(dir(sys))


# print(sys.path)
