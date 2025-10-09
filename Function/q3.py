# add two number within finction 

# def add(n,m) :
#     sum=n+m
#     return sum

# print(f"sum of two number {add(2,6)}")


# user input two number and then print the subtraction ,multiplaction,division,subtaction,additions

a=int(input("enter the first number: "))
b=int(input("enter the second number: "))

def mathematicerule(a,b) :
    sum=a+b
    print(f"sum of number: {sum}",)
    subtract=a-b
    print(f"subtract number(a-b): {subtract} ")
    multiplaction=a*b
    print(f"multiplaction of the two numebr: {multiplaction}")

mathematicerule(a,b)