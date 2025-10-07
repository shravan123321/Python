''' some chai flavors are out of stock.
    you want to skip those and stop entirely if 
    someone requests a restricted flavor
    taxk:
     -skip if flavor is out "out of stock"
     -Break if flavor is "Discontinued "
'''
flavors=["Ginger","out of stock","lemon","Discontinued"]

for flavor in flavors :
    if flavor == "out of stock" :
        continue
    if flavor == "Discontinued":
        break 
    print(f"{flavor} item found")
print("out of loop")