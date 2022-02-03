row_number = int(input())
free_chairs = 0
have_free_chairs = True
for i in range(1, row_number + 1):
    line = input().split()
    chairs = [char for char in line[0]]
    visitors = int(line[1])
    
    count_free_chairs = len(chairs) - visitors
    if count_free_chairs > 0:
        free_chairs += count_free_chairs
    elif count_free_chairs < 0:
        chairs_needed = visitors - len(chairs)
        have_free_chairs = False
        print(f"{chairs_needed} more chairs needed in room {i}")
        
if have_free_chairs == True:
    print(f"Game On, {free_chairs} free chairs left")
    