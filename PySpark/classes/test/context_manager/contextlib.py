from contextlib import contextmanager

@contextmanager
def my_context():
    print('Entering the context')
    yield 55
    print('Exiting the context')

with my_context() as value:
    print(f'Inside the context: {value}')