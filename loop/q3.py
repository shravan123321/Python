# write the python program to find  the all even number between 1 to 20 using a for loop
sum=0
for even in range(1,21) :
    if(even%2==0) :
        sum +=even
print(f"total sum even number: {sum}")
