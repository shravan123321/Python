''' print the week all control the number 
  -monday 1 .... satraday 7
'''
day=int(input("enter the number(1,2,3,4,5,6,7):  "))

match day:
    case 1:
       print("Monday")
    case 2:
       print("Tuesday")
    case 3:
       print("Wednesday")
    case 4:
       print("Thrusday")
    case 5:
       print("Friday")
    case 6:
       print("Saturday")
    case 7:
       print("Sunday")
    case _:
       print("Invalide number input: ")  