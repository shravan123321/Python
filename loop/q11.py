''' you're preparing an order summary with customer names
    and their total bill
    taxk:
     -use two lists: one for names and for bills
     -print: [name] paid [amount]
'''
name=["shravan","shivam","sudhir","sujit","sumit"]
bills =[2000,2100,3000,400,5000]

for names,amount in zip(name,bills) :
    print(f"{names} paid ₹{amount}")