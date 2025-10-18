# write the file 
'''
file = open("filehandling/secondfile.txt","w")

file.write("Hello ji ")
# file.write("My name is Shravan Kumar yadav")
# file.wirte("l am currently learing BCA final year ")
'''

# Ager hum file me appends karte hai o aush time me file me jitna content hai aushaka phir se ripit kar deta hai appends methods
# just like example

file = open("filehandling/secondfile.txt","a")
file.write(" khana huaa kay ho raha hai ji sahi se kam chal raha hai na ji ")

file.close()