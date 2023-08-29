from typing import Any


class CustomDecorator:
    def __init__(self, func) -> Any:
        self.func = func
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print('Decorator han been called')
        result = self.func(*args, **kwargs)
        return result
    
@CustomDecorator
def example_function():
    print('Test')