# Generator comprehension

daily_sales = [5,10,200,100,20,50,60,40]

total_cup=sum(sale for sale in daily_sales if sale > 5)

print(total_cup)