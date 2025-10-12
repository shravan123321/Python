class chai:
    temperature = "hot"
    strength = "strong"
    price = "high level "

cutting = chai()
print(cutting.temperature)

cutting.temperature = "mild"
print(f"after changing: ",cutting.temperature)
print(f"dirct llok in to the class: ",chai.temperature)

del cutting.temperature
print(cutting.temperature)

cutting.cup="small"
print(cutting.cup)
del cutting.cup
print(f"deleting the cut: {cutting.cup}")