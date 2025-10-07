# Write the python program to count the number of values in a given string

num=input("enter the string value: ").lower()
count=0

for value in num :
    count +=1
print(f"total string number: {count}")