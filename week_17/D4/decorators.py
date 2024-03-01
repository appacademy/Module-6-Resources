from datetime import datetime

def timer(cb):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        cb(*args, **kwargs)
        end = datetime.now()
        return end - start
    return wrapper


# @timer
# def say_hello_10000000_times():
#     for _ in range(10000000):
#         print("hello")


# hello = timer(say_hello_10000000_times)

# print(hello())

# print(datetime.now())

# print(say_hello_10000000_times())

@timer
def say_hello_x_times(x, y):
    for _ in range(x * y):
        print("hello")


# print(say_hello_x_times(100, 10))

def args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    print(kwargs)

# args_and_kwargs(1,2,3,4,5,6, this="is", a="dictonary")


# @app.routes("/")
# def index():
    # return "<h1>Hello</h1>"

def square_decorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        x = func(*args, **kwargs)
        return x ** 2
    return wrapper

def multiply_by_3_decorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        x = func(*args, **kwargs)
        return x * 3
    return wrapper

@square_decorator
@multiply_by_3_decorator
def add_nums(x, y):
    return x + y

print(add_nums(1, y=9))





