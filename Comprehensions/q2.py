# set comprehesion 
'''
favourite_chais = [
    "masala chai ","green chai ","masala chai ",
    "Lemon chai", "green chai","Elaichi chai",
    "Coffi masala","milk chai"
]

unique_chai = {My_chai for My_chai in favourite_chais }

print(unique_chai)


'''

num = [1,2,2,3,3,3,5,4,4,5,6,6,7]

res={a for a in num if a%2==0}
print(f"this list even number: {res}")
