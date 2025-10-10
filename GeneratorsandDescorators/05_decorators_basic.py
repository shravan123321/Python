from functools import wraps

def My_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function Runs")
        func()
        print("After Function Runs")
    return wrapper

@My_decorator
def greet():
    print("Hello from decorator class from chai class")

greet()
print(greet.__name__)
