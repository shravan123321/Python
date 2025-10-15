# Aggregation Relationship 
# this Relationship has A Relationship
class car:
    def __init__(self,name,color) :
        self.name=name
        self.color=color
    
class person :
    def __init__(self,name,car) :
        self.name=name
        self.car=car
    
car = car("BMW","Black")
per = person("shravan kumar ",car)

print("print car Details: ")
print(f"Car name: {car.name}  Color: {car.color}")
print("person Details: ")
print(f"person Name: {per.name}  Car purchess: {per.car.name,per.car.color}")