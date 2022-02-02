factor = int(input())
count = int(input())
range_int = factor * count
result = []

for i in range(0, range_int + 1, factor):
    result.append(i)

result.remove(0)
print(result)
