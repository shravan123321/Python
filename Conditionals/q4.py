''' you building the smart thermostat alter system
   - if the device_status is "active"
   - and temprature > 35 -> Warn: Hight temprature
   - Else: Normal temprature
   if device is off -> device is offline
'''
# int=input("enter the temprature: ")

device_status = "active"
temperature=38

if device_status == "active" :
   if temperature > 35 :
      print("High temperature alert! ")
   else:
      print("temprature normal ")
else :
   print("device is of")

s2=set(["greek","for","greek"])
print("set with the used of the list: ",s2)