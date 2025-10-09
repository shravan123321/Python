''' your shop adds a 10% VAT on every order.
    you want this to be consistent and traceable.
    taxk:
      - Write add_vat(price, vat_rate)
      - Use it to compute final prices for 3 order
'''

def add_vat(price,vat_rate) :
    return price * (100+vat_rate)/100

order=[1000,1500,2000]
sum=0
for price in order :
    final_amount = add_vat(price,10)
    print(f"original: {price}, final with Vat: {final_amount}")
