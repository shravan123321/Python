# single inheritance 
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def __init__(self,name,type) :
        super().__init__(name)
        self.type=type
    def eat(self):
        print("dog is eating ")

obj=Dog("Moti","doubberman")
obj.eat()
super(Dog, obj).eat()