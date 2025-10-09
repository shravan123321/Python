'''
    you sell diffrent chai size
    Instead of writing formulas everywhere create a function.
    task:
      -Write calculate_bill(cups,price_per_cup)
      -return total bill
      -use this function for multiple order
'''

def calculater_bill(cups,price_par_cup) :
    return cups * price_par_cup

print("price_per_cups tea: ₹15 ")
b=15
a=int(input("enter the cups of tea: "))
total_bill = calculater_bill(a,b)

print(f"total_bill tea: ₹{total_bill}")

