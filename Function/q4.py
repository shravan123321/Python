'''
# default argument

def great(name,message="Hello kay ho raha hai ") :
    print(name,message)
great("shravan Kumar ")

# keyword arguments
def great(name,age,message):
    print(message,name,f"your age is: {age}")

great(name="shravan kumar ",age=20,message="Hello")

#positional arguments
def add_number(a,b):
    print("x=",a)
    print("y=",b)
    print(a+b)

add_number(2,5)

'''
