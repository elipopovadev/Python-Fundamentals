words = input().split()
len_first = len(words[0])
len_second = len(words[1])
max_len = max(len_first, len_second)

sum = 0
for i in range(0, max_len):
    if i < len_first and i < len_second:
        sum += ord(words[0][i]) * ord(words[1][i])
    elif i < len_first and i >= len_second:
        sum += ord(words[0][i])
    elif i >= len_first and i < len_second:
        sum += ord(words[1][i])

print(sum)        
