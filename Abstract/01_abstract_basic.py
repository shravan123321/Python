# abstract class but can't used in this Animal
class Animal:
    def eat(self):
        pass
obj=Animal()
obj.eat()


from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

# Trying to instantiate abstract class will fail
# a = Animal()   # ❌ This will give an error

# Subclass must implement abstract methods
class Dog(Animal):
    def eat(self):
        print("Dog is eating")

    def sleep(self):
        print("Dog is sleeping")

# Create object of Dog
d = Dog()
d.eat() 
d.sleep() 
