class person :
    def __init__(self,name,age,salary) :
        self.name=name
        self.age=age
        self.__salary=salary # define the private data
    def getname(self):
        return self.name
    def setname(self) :
        self.name=name    
    def getage(self) :
        return self.age
    def setage(self) :
        self.age=age
    def getsalary(self) :
        return self.__salary    
    def setsalary(self) :
        self.__salary=salary


pre=person("shravan kumar ",20,20000)
print(pre.name,pre.age)
print(pre.getsalary())

#Change the name and age salary 
pre.setname("shravan kumar yadav")
# pre.setage(21)
# pre.setsalary(30000)
print(pre.getname())
