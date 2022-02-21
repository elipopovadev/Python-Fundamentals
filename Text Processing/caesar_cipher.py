text = input()
cipher = []

for char in text:
    new_char = chr(ord(char) + 3)
    cipher.append(new_char)

print(''.join(cipher))
