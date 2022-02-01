text = input().split(' ')
sequence2 = list(map(int, text))

result = filter(lambda x: x % 2 == 0, sequence2)
print(list(result))
