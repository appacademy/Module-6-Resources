from timer import say_hello_num_times


def chain_decorator(func):
    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        print(f"In chan decorator, num={num}")
        return num**2

    return wrapper


def mult_three(func):
    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        print(f"In mult three, num={num}")
        return num * 3

    return wrapper


@mult_three
@chain_decorator
def num(a, b):
    print("in num")
    return a + b


print(num(2, 2))
say_hello_num_times(5)
