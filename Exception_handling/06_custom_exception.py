# custom exception class
class EmptyException(RuntimeError):
    def __init__(self, argument):
        self.argument = argument

var = ""

try:
    if var == "":
        raise EmptyException("This variable is an empty string.")
except EmptyException as e:
    print(e.argument)
