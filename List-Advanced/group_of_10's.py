text = input().split(", ")
numbers = list(map(int, text))
dict = {}
boundary = 0

while sum(numbers) > 0:
    boundary += 10
    dict[boundary] = list()
    for i in range(0, len(numbers)):
        if numbers[i] <= boundary and numbers[i] != 0:
            current_num = numbers[i]
            numbers[i] = 0
            dict[boundary].append(current_num)         
                    
for key, value in dict.items():
    print(f"Group of {key}'s: {value}")
    