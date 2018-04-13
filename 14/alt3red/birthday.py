from functools import wraps

def european_date(func):
    """Decorator that reverses mmdd date to ddmm"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        date = func(*args, **kwargs)
        return date[::-1]
    return wrapper
        

@european_date
def get_birthday():
    month = input('What month were your born? ')
    day = input('What day were you born on? ')
    return [month, day]

birthdate = get_birthday()