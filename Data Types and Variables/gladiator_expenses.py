fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

count_times_shield_break = 0
total_cost = 0
for i in range(1, fights_count + 1):
    if i % 2 == 0:
        total_cost += helmet_price
    if i % 3 == 0:
        total_cost += sword_price    
    if i % 2 == 0 and i % 3 == 0:
        total_cost += shield_price
        count_times_shield_break +=1
        if count_times_shield_break == 2:
            total_cost += armor_price
            count_times_shield_break = 0

print(f"Gladiator expenses: {total_cost:.2f} aureus")
         