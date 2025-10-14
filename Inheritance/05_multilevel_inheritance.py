# multi level inheritance 
# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("Animal is eating")

# Derived class 1
class Cat(Animal):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    def eat(self):
        print("Cat is eating")
    def display(self):
        print("Cat Display:")
        self.eat()       # Calls Cat's eat
        super().eat()    # Calls Animal's eat

# Derived class 2 (Pet inherits Cat)
class Pet(Cat):
    def __init__(self, name, type, housename):
        super().__init__(name, type)
        self.housename = housename
    def eat(self):
        print("Pet is eating")
    def display(self):
        print("Pet Display:")
        self.eat()       # Calls Pet's eat
        super().eat()    # Calls Cat's eat

# -------------------------
# Object creation and method calls

# Cat object
cat_obj = Cat("Sitara", "Doberman")
cat_obj.eat()
cat_obj.display()

print("-------------------------")

# Pet object
pet_obj = Pet("Motti", "Bulldog", "Home1")
pet_obj.eat()
pet_obj.display()
