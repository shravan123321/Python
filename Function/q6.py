#return types 
 #implicity conversion
def add_number(a:int,b:int)->int:
    return a+b
print(add_number(1.5,5.3))

#function nested
def outer() :
    print("Hello sharavan Ji")

    def inner() :
        print("How are you ")
    return inner()
get=outer()
print(get)