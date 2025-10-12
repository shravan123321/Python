# Access modifier

# public 
class person :
    def __init__(self,name,age,salary) :
        self.name=name # public
        self.age=age  #public
        self.__salary=salary # private ager hu __ ke used kiya to private ho jata hai
    def showdata(self) :
        return self.name,self.age,self.salary
    def getsalary(self) :
        print(self.__salary)
        self.__calculater()
    def __calculater(self) : #private the methods
        print("hello taxk open")
per1 = person("shravan kumar",20,20000)
per2 = person("dhanjeet yadav",28,40000)
print(per1.name,per1.age)
per1.getsalary()
# print(self.__salary)  rong the access methos private data
# print(self.__calculater) ye bhi rong the accesing the data

# so l am accessing the data private out of the class technike using

print(per1._person__salary)
print(per1._person__calculater())
# print(per1._person__salary)
# per1._person__calculater()
