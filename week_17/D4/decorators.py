from datetime import datetime

def print_args(*args):
    for arg in args:
        print(arg)

# print_args("g", 6, "5<", "hello") # *arg are stored as a tuple

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(key1="hello", key2="goodbye")

def print_args_and_kwargs(num1, num2, *args, **kwargs):
    print(num1, num2)
    print(args)
    print(kwargs)

print_args_and_kwargs(1, 2, 3, key="value")


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        val = func(*args, **kwargs)
        end_time = datetime.now()
        time_elapsed = end_time - start_time
        print(time_elapsed)
        return val
    return wrapper

@timer
def say_hi_1_000_000_times():
    for _ in range(1_000_000):
        print("Hello there!")

@timer
def say_hi_x_times(x):
    for _ in range(x):
        print("Hello there!")

# timed_hello = timer(say_hi_1_000_000_times)

# timed_hello()

# timer(say_hi_1_000_000_times)()

say_hi_1_000_000_times()


