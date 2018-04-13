from functools import wraps

def proper_name(func):
    """Decorator to capipitalize first letter of each name"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        name = func(*args, **kwargs)
        return name.title()
    return wrapper

@proper_name
def get_name():
    return input('What is your name: ')

name = get_name()