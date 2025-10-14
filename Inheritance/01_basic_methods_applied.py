class Animal :
    def __init__(self,name):
        self.name=name
    def eat(self) :
        print(self.name+"animalis eating ")

class Dog(Animal):
    def __init__(self,name,type) :
        Animal.__init__(self,name)
        self.type=type
    def getthenameofdog(self):
        print(self.name)
dog = Dog("Prince ", "Dubberman")
dog.eat()  
dog.getthenameofdog()