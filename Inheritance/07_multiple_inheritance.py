# multiple inheritance methods one parent and two child

# Base class
class parent1 :
    def __init__(self,name):
        self.name=name
    def work(self) :
        print("Software Engineer")
# Base class
class parent2 :
    def __init__(self,name) :
        self.name=name
    def work(self) :
        print("Business men")
# Derive class
class child(parent1,parent2) :
    def __init__(self,name,type) :
        super().__init__(name)
        self.type=type
    def work(self) :
        print("l am a Student ")
    def display(self) :
        print("Display child")
        self.work()
        super().work()

# creat the object 
obj = child("Shravan Kumar","dought")
obj.work()
obj.display()
parent2.work(obj)