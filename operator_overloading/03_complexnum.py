# add the two complex numerb 

class complexnum:
    def __init__(self,x,y):
        self.firstnum = x
        self.secondnum =y
    def __add__(self,c1) :
        return self.firstnum +c1.firstnum,self.secondnum+c1.secondnum

obj1 = complexnum(2,5j)
obj2 = complexnum(5,7j)
result=obj1+obj2
print(f"sum of complex number: {result}")