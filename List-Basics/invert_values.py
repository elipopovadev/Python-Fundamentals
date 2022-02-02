numbers = input().split(" ")
numbers = list(map(int, numbers))
invert_list = []
for num in numbers:
    if num == 0:
        invert_list.append(0)
    elif num < 0:
        new_num = abs(num)
        invert_list.append(new_num)
    else:
        new_num = -num
        invert_list.append(new_num)
        
print(invert_list)
        
    