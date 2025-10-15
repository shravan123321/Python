# POLYMORPHISM using inheritance

class Animal:
    def eat(self) :
        print("Animal is eating ")

class Dog(Animal):
    def eat(self) :
        print("dog is eating ")

class Cat(Animal):
    def eat(self):
        print("cat is eating ")

c = Cat()
d = Dog()
a = Animal()

a.eat()
d.eat()
c.eat()