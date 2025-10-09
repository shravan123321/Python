# pass by value and pass by refrence
 #pass by value
# num=5
# def modify_num(num) :
#     num +=1
#     print(num)
# modify_num(num)
# print(f"original number: {num}")

# call by refrence
my_list = [1, 2, 3, 4]

def modify_list(l1):
    l1.append(20)
    print(my_list)

print(f"Before calling fun {my_list}")
modify_list(my_list)
print(f"After calling fun {my_list}")