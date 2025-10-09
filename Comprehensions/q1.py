# list comprehensions 
  
menu=[
    "masala chai",
    "iced lemon tea",
    "Green tea",
    "iced peach tea",
    "Ginger chai"
]
  
iced_tea=[My_tea for My_tea in menu if "iced" in My_tea]

print(iced_tea)
