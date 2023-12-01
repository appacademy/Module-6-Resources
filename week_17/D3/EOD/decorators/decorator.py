
# 🎄🎄🎄 DECORATORS 🎄🎄🎄
from datetime import datetime


def timer(func):
    """decorator definition for timing the execution of the wrapped function"""

    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        val = func(*args, **kwargs)
        print(val)
        end_time = datetime.now()
        time_elapsed = end_time - start_time
        return time_elapsed

    return wrapper

@timer
def say_hi(name="you"):
    return f"Hello {name}!"

@timer
def say_bye():
    return "See ya later!"

# timed_hi = timer(say_hi)
# print(timed_hi())

# print(say_hi())
# print(say_bye())
# print(say_hi("Brad"))
# print(say_bye())


@timer
def do_stuff(num):
    counter = 0
    for val in range(num):
        counter += 1
    return counter

# print(do_stuff(10_000_000))
print(do_stuff(1_000_000_000))
