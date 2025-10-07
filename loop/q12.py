''' you want to simulate tea heating 
    it starts at 40 'c can boils at 100 'c.
    task:
     -use a while loop
     -increase temperature by 15 until it reaches or exceeds 100.
     -print each temperature step.
'''
temperature=40

while temperature < 100 :
    print(f"current tempereture is: {temperature}")
    temperature +=15
print("tea is ready to boils:")