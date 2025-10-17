class Comparisionoverading :
    def __init__(self,x) :
        self.firstnum = x
    def __gt__(self,y) :
        if(self.firstnum>y.firstnum) :
            return True
        else:
            return False
num1 = Comparisionoverading(20)
num2 = Comparisionoverading(10)
print(num1 < num2)