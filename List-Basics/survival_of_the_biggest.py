text = input().split(" ")
numbers = list(map(int, text))
count_to_remove = int(input())

for i in range(count_to_remove):
  numbers.remove(min(numbers))

print(*numbers, sep = ", ")
