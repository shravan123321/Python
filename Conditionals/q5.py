'''You run an online tea store.
   if the order amount is more than 300 Rupya , delivery is free
   otherwise, it costs 30 rupya
   taxk:
    - input: order_amount
    - use ternary operator to decide delivery fee
'''
order_amount = int(input("enter the order amount: "))
 
# delivery_fees =0 if order_amount >300 else 30

# print(f"delivery fees is : {delivery_fees}")

delivery_fees = 0
if order_amount > 300 :
    delivery_fees = 0
else :
    delivery_fees = 30

print(f"delivery fees: {delivery_fees}")