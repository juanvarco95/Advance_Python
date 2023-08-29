class MyContext:
    def __enter__(self):
        print('Entering the context')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print('Exiting the context')
        if exc_type is not None:
            print(f'Exception: {exc_type}, {exc_value}')
        return False

with MyContext() as context:
    print('Inside the context')