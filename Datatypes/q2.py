# numbers, boolean and operaters

#integer number
value =2
print(f"types of value {type(value)}") 

black_tea_grams=14
ginger_grams=3

total_grams = black_tea_grams + ginger_grams
print(f"total gams of tea: {total_grams}")

remaning_tea = black_tea_grams - ginger_grams
print(f"remening tea: {remaning_tea}")


total_tea_bag = 7
posts = 4
bags_per_pot = total_tea_bag // posts

print(f"white tea bags per pot: {bags_per_pot}")

total_cardamom =10
pods_per_cup=3

leftover_pods =total_cardamom / pods_per_cup
print(f"leftover c pods: {leftover_pods}")

leftover_pods =total_cardamom % pods_per_cup
print(f"leftover c pods: {leftover_pods}")

base_label =2
scale_factor =3
powerful_falvour = base_label ** scale_factor

print(f"scaled flavour strenght {powerful_falvour}")