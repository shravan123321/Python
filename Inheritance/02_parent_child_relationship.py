#Access the parent property
class parent :
    property = 100
    def eat(self) :
        print("parent eating ")
class child(parent) :
    property = 110
    def display(self) :
        print("child property: ",self.property)
        print("parent property: ",super().property)
    def eat(self) :
        print("child eating")
    def calleat(self) :
        self.eat()
        super().eat()
obj = child()
obj.display()
obj.calleat()