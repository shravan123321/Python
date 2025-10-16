# used by the finally exception keybord
# the finally_Exception keybord ager hum used karte hai to progam me Exception ho ya na ho hamesh program excuted hoga
def operate(num):
    try:
        result= 5/num
    except ZeroDivisionError:
        print("can't division by the 0")
    finally:
        print("this portion of the code will always be excuted ")

operate(5)
operate(0)