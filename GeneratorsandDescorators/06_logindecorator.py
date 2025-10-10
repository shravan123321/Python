from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type):
    print(f"Brewing {type} chai")

brew_chai("masala chai")
