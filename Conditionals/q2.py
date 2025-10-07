''' local cafe want to program that suggested a sanck if a customer asked for cookies or samosa it conform the order otherwise it say it's not noavlable
   taxk
     - take snack input
     - if it's "cookies " or "samosa"conform the order
     - Else unavlable 
'''
snack=input("enter the snack item: ").lower()

if snack=="cookies" or snack=="samosa" :
    print("order sucessfully conform")
else:
    print("sorry we only cookies or samosa with tea")