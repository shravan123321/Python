# Read this file 

file = open("filehandling/firstfile.txt", "r")
'''
methods 1
for line in file:
    print(line)

# methods 2
print(file.read())


# methods 3
with open("filehandling/firstfile.txt","r") as file :
    data=file.read()
    print(data)
'''

# methods 4
# read the minimum file just like 50  index number 
with open("filehandling/firstfile.txt","r") as file :
    data=file.read(50)
    print(data)