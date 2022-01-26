tank_capacity = 255
total = 0
lines = int(input())
for i in range(lines):
    literes = int(input())
    if total + literes <= tank_capacity:
        total += literes
    else:
        print("Insufficient capacity!")

print(total)