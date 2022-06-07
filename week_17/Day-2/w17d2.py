# IF STATEMENTS
def lunch():
    lunch = "Salad"
    if lunch == "Pizza":
        print("We have Pizza!")
        return
    if lunch == "Sandwich":
        print("Yay sandwich!")
        return
    print("Lunch is not gonna be good...")

# lunch()

# XOR
# print(True ^ True)
# print(True ^ False)
# print(False ^ True)
# print(False ^ False)

# y = 8
# z = 10
# print(y is z)
# print(id(y))
# print(id(z))

# Str.replace
# string = "Pizza"
# new_string = string.replace("za", "zzzzzzas")
# print(new_string)

# WHILE LOOPS
# i = 0
# while i < 5:
#     i += 1
#     if i != 3:
#         continue
#     print("Yay we got to 3!")

# FOR LOOPS
foods = ["Pizza", "Sandwich", "Salad", "Wrap"]

# for food in foods:
#     print(food)
# print("Pita" in foods)


# print(list(nums))
# for i in range(len(foods)):
#     print(f"{i}. {foods[i]}")


# num = 0
# try:
#     print("Trying now...")
#     print(4/num)
# except ZeroDivisionError:
#     print("oops i tried to divide by zero!")
# else:
#     print("yay we didn't divide by zero, we win!")
# finally:
#     print("this happens no matter what")

# FUNCTIONS
# multiply = lambda num, num2: num * num2
 
# print(multiply(2, 5)) # True
# y = 200 
# z = "Pizza"

# def make_a_five():
#     """Assign a variable the value of five """
#     print(z)
#     # z = "Sandwich"
#     # print(z, "Inside the function")
#     return y

# make_a_five()
# print(make_a_five.__doc__)

# if True:
#     x = 10
 
# print(x) #10
# # `x` was created in the global scope
 
# print(y) # NameError: name 'y' is not defined
# # `y` was created in the scope of the make_a_five function


# def brad_wants_pizza(pizza, fries, soda):
#     return f"Brad wants {pizza} slices of pizza, {fries} orders of fries, and {soda} sodas"


# print(brad_wants_pizza(3, 2, soda = 4))


foods = ["Taco", "Burrito", "Pizza", "Salad"]
# print(foods[0:4:2])
# print(len(foods))
# foods.extend(["Chicken Nuggets", "Steak"])
# print(foods)
# foods.remove("Burrito")
# print(foods)
nums = [12, 2, 21, 5, 1]
nums.sort()
print(nums)
