 
#? Decorators

def my_decorator(func):
    def wrapper():
        print('Before the function is called')
        func()
        print('After the function is called')
    return wrapper

@my_decorator
def say_hello():
    print('Hello!!!')

say_hello()

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(n = 3)
def greet(name):
    print(f'Hello, {name}')

greet('Juan')

