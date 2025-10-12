#  there is a three types of methods
# 1. instance methods
# 2. class methods
# 3. static methods

#instance/object methods
'''
class person :
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def showdata(self):
        return self.name , self.age
    
per1=person("shravan kumar",20)
per2=person("dhanjeet kumar",25)
print(per1.name,per1.age)
print(per2.name,per2.age)
'''

# class methods 
'''
class person:
    country="India"
    @classmethod
    def greet(cls) :
        print("hello from the: ",cls.country)
    
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def showdata(self) :
        return self.name,self.age

per1=person("shravan kumar ",20)
per2=person("dhanjeet yadav",28)
print(per1.name,per1.age)
print(per2.name,per2.age)
per1.greet()
'''

# static methods 

class person :
    country = "India"
    @classmethod
    def greet(cls) :
        print("Hello from the: ",cls.country)
    @staticmethod    
    def hello() :
        print("hello ji ") # does not acces the class property and objedect property
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def showdata(self) :
        return self.anme,self.age
    
per1=person("shravan kumar",20)
per2=person("dhanjeet yadav",28)
print(per1.name,per1.age)
print(per2.name,per2.age)
per1.greet()
per1.hello()
person.hello()
