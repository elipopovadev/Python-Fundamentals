start = int(input())
finish = int(input())
list = []

for i in range(start, finish + 1):
    char = chr(i)
    list.append(char)

print(" ". join(list))
