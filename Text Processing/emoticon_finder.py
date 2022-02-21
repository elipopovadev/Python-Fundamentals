text = input()

for i in range(0, len(text) - 1):
    if text[i] == ':':
        print(text[i] + text[i + 1])
