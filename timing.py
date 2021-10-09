from time import time


def speed(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        code = fn(*args, **kwargs)
        end_time = time()
        total_time = end_time - start_time
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {round(total_time, 3)}")
        return code
    return wrapper


@speed
def calculation():
    return sum(x for x in range(90000000))


print(calculation())
