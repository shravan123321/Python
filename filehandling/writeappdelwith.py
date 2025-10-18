 # code for the appending/writing to a file using with

with open("filehandling/file3.txt","w") as file:
    file.write("hello shravan ji")

with open("filehandling/file3.txt","a") as file:
    file.write("kaise hai ji")

# delete the file 
# import os
# os.remove("filehandling/file3.txt")