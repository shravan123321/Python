def chai_customer() :
    print("Welcome ! What chai would you like ?")
    order = yield
    while True:
        print(f"preparing:  {order}")
        order = yield

stall = chai_customer()
next(stall) # start the generator
stall.send("masala chai")
stall.send("lemon chai")
stall.send("coffi")