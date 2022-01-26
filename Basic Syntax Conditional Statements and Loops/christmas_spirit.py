christmas_ornaments = {"set": 2, "skirt": 5, "garlands": 3, "lights": 15}
allwoed_quantity = int(input())
days_left = int(input())

total_cost = 0
christmas_spirit = 0
for i in range(1, days_left + 1):
    if i % 11 == 0:
        allwoed_quantity += 2
    if i % 2 == 0:
        total_cost += christmas_ornaments["set"] * allwoed_quantity 
        christmas_spirit += 5
    if i % 3 == 0:
        total_cost += (christmas_ornaments["skirt"] * allwoed_quantity) + (christmas_ornaments["garlands"] * allwoed_quantity)
        christmas_spirit += 13
    if i % 5 == 0:
        total_cost += (christmas_ornaments["lights"] * allwoed_quantity)
        christmas_spirit += 17
    if i % 3 == 0 and i % 5 == 0:
        christmas_spirit += 30
    if i % 10 == 0:
        christmas_spirit -= 20
        total_cost += christmas_ornaments["skirt"] + christmas_ornaments["garlands"] + christmas_ornaments["lights"]
        
last_days = days_left
if last_days % 10 == 0:
     christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
    