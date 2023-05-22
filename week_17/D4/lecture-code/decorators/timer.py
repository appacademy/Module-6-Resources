from datetime import datetime


def timer(cb):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        cb(*args, **kwargs)
        end = datetime.now()
        return end - start

    return wrapper


@timer
def say_hello_num_times(num):
    for _ in range(num):
        print("Hello!")
    return "Hello!"


# print(say_hello_num_times(1_000_000))


# hello = timer(say_hello_num_times)
#
# print(hello(1_000_000))
