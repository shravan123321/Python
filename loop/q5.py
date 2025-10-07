''' write the python program to print the febonacci series up to n terms
    1,1,2,3,5,8,13.....
'''
num=int(input("enter the number: "))
if(num<=0):
    print("number entered is not currected, it shoud be 0 entered num ",num)
print(1,end=",")
if(num==1):
    pass
else:
    print(1,end=",")
    if(num==2):
        pass
    else:
        #print the remening part of the serize
        prev = 1
        prev_prev = 1
        for value in range(3,num+1) :
            print(prev+prev_prev, end=",")
            prev,prev_prev=prev+prev_prev,prev
     