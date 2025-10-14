# using super for calling the parent initalizer
class Animal :
    def __init__(self,name): 
        self.name=name
    def eat(self) :
        print(self.name+"animalis eating ")

class Dog(Animal):
    def __init__(self,name,type) :
        # Animal.__init__(self,name)
        super().__init__(name) # call the parent constructor or initalizer
        self.type=type
    def getthenameofdog(self):
        print(self.name)
dog = Dog("Prince ", "Dubberman")
dog.eat()  
dog.getthenameofdog()