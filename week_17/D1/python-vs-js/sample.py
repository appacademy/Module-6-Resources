# Ternary Operators
python_rules = False
# print("python is better") if python_rules else print("python is still better")

# if condtionals
# if python_rules:
#     print("python is better")
#     print("because it just is")
# else:
#     print("javscript honestly isn't that bad either")
#     print("but python is still better")

# multiline strings and comments

multi_line_str = """
this is a 
multiline string!!!!
"""

# print(multi_line_str)

"""
This is a multiline
comment
"""

# random numbers
import random
teachers = ["Andrew", "David", "Krishna"];
random_idx = random.randint(0, len(teachers) - 1)
# print(teachers[random_idx])
# print(dir(random))
# print(random.choice(teachers))


# asking for user input

# name = input("What is your name, traveler? ")
# print(f"Welcome to mod 6, {name}. It's going to be fun")

# filter built-in and lambda syntax
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_odds(x):
    return x % 2 != 0

# odds = filter(lambda x: x % 2 != 0, nums)
odds = filter(get_odds, nums)

# lambda_get_odds = lambda x: x % 2 != 0
# odds = filter(lambda_get_odds, nums)

# print(list(odds))

# classes
class Student:
    def __init__(self, name, python_knowledge):
        self.name = name
        self.python_knowledge = python_knowledge

    def get_student_info(self):
        return f"{self.name} knows {self.python_knowledge} about python!"

andres = Student("Andres", "a good amount")

print(andres.get_student_info())


