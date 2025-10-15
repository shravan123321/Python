# Composition Relationship
class Engine :
    def enginedetails(self):
        print("car engine Model ER123EB ")

class Tyres :
    def tyreDetails(self):
        print("tyred is apollo")

class Doors:
    def doorDetails(self):
        print("Doors of the car is automatic: ")

class car:
    def __init__(self):
        self.engine=Engine()
        self.door=Doors()
        self.tyres=Tyres()
    def printdetails(self) :
        self.engine.enginedetails()
        self.tyres.tyreDetails()
        self.door.doorDetails()

obj = car()
obj.printdetails()