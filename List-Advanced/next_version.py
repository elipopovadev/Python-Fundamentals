text = input().split(".")
numbers = list(map(int, text))
if numbers[2] < 9:
    numbers[2] += 1
elif numbers[2] == 9:
    numbers[2] = 0
    if numbers[1] < 9:
       numbers[1] += 1
    else:
        numbers[1] = 0
        numbers[0] += 1

print(*numbers, sep = '.')