# Encapsulation
class person:
    #private methods
    def __init__(self,name,age) :
        self.__name=name #private
        self.__age=age #priavte
    # Access the private methods get and set methods
    def getName(self) :
        return self.__name
    def setname(self,name) :
        self.__name=name
    def getage(self) :
        return self.__age
    def setage(self,age):
        self.__age=age
    
per=person("shravan kumar",20)
print(per.getName(),per.getage()) #Access the private methods get and put methods

# changing the private methods get and put methods
per.setname("shravan Yadav")
per.setage(21)
print(per.getName(),per.getage())
