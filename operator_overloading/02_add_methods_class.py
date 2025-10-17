class sum :
    def __init__(self,num) :
        self.number=num
    def __add__(self,u):
        return self.number+u.number
    
obj1 = sum(20)
obj2 = sum(40)
result=obj1+obj2
print(f"sum the total number: {result}") 