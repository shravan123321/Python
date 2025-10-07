''' you are building a trcket info system for a railway app
     Based on seat type, show features
task:
    -input: "sleeper" , "AC" , "general" , "luxury"
    -match using match-case
    -unknown->show: "invalid seat type"
'''
seat_type = input("enter the seat types (sleeper/AC/general/luxuary)").lower()

match seat_type :
    case "sleeper":
       print("sleeper seat no, AC(air condition)")
    case "AC":
       print("seat AC (air condition)")
    case "general":
       print("general seat no, seat number conform ")
    case "luxuary":
       print("one bogi two seat ")
    case _:
       print("Invalid seat ")