total_number_electrons = int(input())
shells = []
count_position = 1

while total_number_electrons > 0:
    max_electrons = 2 * count_position**2
    if total_number_electrons >= max_electrons:
       current_electrons = max_electrons
       shells.append(current_electrons)
       total_number_electrons -= max_electrons
    elif total_number_electrons < max_electrons:
        current_electrons = total_number_electrons
        shells.append(total_number_electrons)
        total_number_electrons = 0
        
    count_position += 1

print(shells)
