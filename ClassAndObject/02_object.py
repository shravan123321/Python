class chai :
    origin = "India"

print(chai.origin)

chai.is_chai = True 
print(chai.is_chai)

# create object from the class 

masala = chai()
print(f"masala {masala.origin}")
print(f"masala  {masala.is_chai}")

masala.is_chai = False 
print(f"class: {chai.is_chai}")
print(f"masala: {masala.is_chai}")
