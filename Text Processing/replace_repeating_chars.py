text = input()

result = []
for i in range(0, len(text) - 1):
    if text[i] == text[i + 1]:
        continue
    else:
        result.append(text[i])

result.append(text[-1])   
print(''. join(result))
