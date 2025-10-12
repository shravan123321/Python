# methods_overloading 
# there are two types of method overloading in python 
 # 1. explicit methods_overloading
 # 2. implicit methods_overloading

'''
 # explicit methods_overloading
class calculater :

    def add(self,a,b) :
        return a+b
    def add(self,a,b,c) :
        return a+b+c
    
cal=calculater()
print(cal.add(1,3,6)) # ager hum data add karana chahta hu to add ho gaye ga but
print(cal.add(2,5))   #overloading karege to nahi hoga qki by default data last wala late hai
'''


# implicit methods_overloading
class calculater :
    def add(self,a,b,c=0) :
        return a+b+c
cal=calculater()
print(cal.add(1,4,7))
print(cal.add(1,5))
