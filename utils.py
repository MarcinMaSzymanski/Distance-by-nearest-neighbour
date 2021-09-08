import time
import functools


def timer(f):
    @functools.wraps(f)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = f(*args, **kwargs)
        end_time = time.perf_counter()
        duration_time = end_time - start_time
        print(f"Finished {f.__name__} in {duration_time} s.")
        return value

    return wrapper_timer
