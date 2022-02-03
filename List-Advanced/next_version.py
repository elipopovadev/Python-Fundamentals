numbers = input().split(".")
current_version = "".join(numbers)
next_version = str(int(current_version) + 1)
print(*next_version, sep = '.')