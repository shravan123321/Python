# Boolean data types

is_boolean = True  # Corrected spelling from 'is_boilean'
stri_count = 4
total_actions = stri_count + is_boolean  # True is treated as 1 in arithmetic
print(f"Total actions: {total_actions}")  # Output: Total actions: 5

milk_present = 0  # No milk
print(f"Is there milk? {bool(milk_present)}")  # Output: Is there milk? False

milk_present = 2 
print(f"is there milk: {bool(milk_present)}")  #output avlable the milk

# boolean types is a logical operaters just like and,or ,not
water_hot=True
tea_added= True

and_operations=water_hot and tea_added # this water hot
print(f"operation perforn the: {and_operations}")

water_hot=True
tea_added= False

and_operations=water_hot and tea_added
print(f"operation performs the: {and_operations}")

#or logical_operations

or_operations=water_hot or tea_added
print(f"operations performs the: {or_operations}")

water_hot=True
tea_added= True 

or_operations=water_hot or tea_added
print(f"operations performs the: {or_operations}")
#not logical_operations

not_operations=water_hot not tea_added
print(f"operation perform the: {not_operations}")