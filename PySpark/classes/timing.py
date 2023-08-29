import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Time taken: {end_time - start_time:.4f} seconds')

        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)

slow_function()