text = input().split(" ")

result = [element for element in text if len(element) % 2 == 0]
print("\n".join(result))
