import functools
import time


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        res = func(*args, **kwargs)
        end = time.perf_counter_ns()
        print('{} took {} ms'.format(func.__name__, (end - start) / 1000))
        return res
    return wrapper

@log_execution_time
def calculate_similarity(items):
    pass

