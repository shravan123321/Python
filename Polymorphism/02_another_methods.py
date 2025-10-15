class Birdfly :
    def filyBired(self,Bird) :
        Bird.Fly()

class Parrot :
    def Fly(self) :
        print("Parrot is Flying")
    
class Crow:
    def Fly(self) :
        print("Crow is Flying")

p=Parrot()
c=Crow()

obj=Birdfly()

obj.filyBired(p)
obj.filyBired(c) 