# Exception handel by else statements

def operate(num):
    try:
        result = 5/num
    except ZeroDivisionError :
        print("can't divide a number by 0")
    else:
        print(result)
operate(5)
operate(0)