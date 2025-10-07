''' A tea Stall offers diffrent price cup size Write the program to calculate price base on size
    - input "smaller" , "medium" , "large"
    - smaller=10 Rupya , medium=15 Rupya , large=20 Rupya
    -if Invalid: show "Unknow cup size "
'''

tea=input("Choose the cup size: (small/medium/large)").large()

if tea=="small":
    print("small cup tea Price: 10 Rupees")
elif tea=="medium":
    print("medium cup tea price: 15 Rupess")
elif tea=="large":
    print("large cup tea Price: 20 Rupees")
else:
    print("Unknow cup size: ")
