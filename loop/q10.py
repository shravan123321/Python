''' you're creating a tea menu board,
    each item must be numbered,
    taxk:
      -use enumberate() to print menu items with numbers,
'''
menu = ["Green","lemon","spiced","mint"]

for idx,item in enumerate(menu,start=1) :
    print(f"{idx} : {item} chai")