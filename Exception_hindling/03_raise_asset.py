'''
# raise Exception in python 
arr = [1,3,45]

if len(arr) < 4:
    raise Exception(f"length of the given list is {len(arr)} which is <4")
'''

# asset Exception

def cube_root(num):
    #check if the number is positive and i would raise an exception
    assert (num>=0) , "pass a positive number "
    return num**(1/3)
print(cube_root(8))
# print(cube_root(-8))
# print("last line")

try:
    vak=cube_root(-8)
    print(val)
except:
    print("place provide valid integer for the cube root ")
print("last line")