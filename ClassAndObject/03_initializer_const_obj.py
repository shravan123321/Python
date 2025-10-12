#initalized init methods  
''''
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    # def __str__(self) :
    #     return f"name: {self.name}, Age: {self.age}"
per1=person("sonali kaumai",23)
per2=person("mitali kumari",21)
print(per1.name,per1.age)
print(per2.name,per2.age) 

# one person class can not have a multiple init methodes
class person :
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def __init__(self,name) :
        self.name=name

per=person("shravan",20)
print(per.name,per.age)

'''

'''
#default parameter constructor
class person :
    def __init__(self,name,age=20,hobbi="cricket"):
        self.name=name
        self.age=age
        self.hobbi=hobbi
per1=person("shravan kuamr")
per2=person("dhuman sharma",21)
per3=person("shudhir kumar",23,"badminter")
print(per1.age)
print(per1.hobbi)
'''
class person :
    country = "India"
    def __init__(self,name,age):
        self.name=name
        self.age=age
per1 = person("vishwa",50)
per2 = person("shravan",20)
print(per1.name,per1.age,per1.country)
print(per2.name,per2.age,per2.country)