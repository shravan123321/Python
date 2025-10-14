class Animal :
    def __init__(self,name):
        self.name=name
    def eat(self) :
        print("Animal is eating ")
class cat(Animal) :
    def __init__(self,name,type) :
        super().__init__(name)
        self.type=type
    def eat(self):
        print("cat is a eating")
    def display(self) :
        self.eat()
        super().eat()
class dog(Animal) :
    def __init__(self,name,type) :
        super().__init__(name)
        self.type=type
    def eat(self) :
        print("dog is a eating ")
    def display(self) :
        self.eat()
        super().eat()


print("#------------------------ ")
#-----------
# cat class
obj = cat("switti ","doubblname")
obj.eat()
obj.display()

print("#------------------------ ")
#----------
obj=dog("price ","doubber")
obj.eat()
obj.display()